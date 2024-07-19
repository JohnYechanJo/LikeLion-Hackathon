from django.shortcuts import render
import urllib.parse
import urllib.request
import json
import re
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SearchResult  # 모델을 임포트합니다.

# 클라이언트 ID와 시크릿 키는 환경 변수로 설정하는 것이 좋습니다.
import os
client_id = os.getenv('5xqa38sj2upsYMMShhe1')
client_secret = os.getenv('ZlpBR5K8cr')

@csrf_exempt
def search(request):
    if request.method == 'GET':
        return render(request, 'search_form.html')
    
    elif request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            return HttpResponse("검색 질의를 입력해 주세요.", status=400)

        idx = 0
        display = 100
        start = 1
        end = 1000

        # URL 인코딩
        query = urllib.parse.quote(query)
        web_df = pd.DataFrame(columns=("Title", "Link", "Address"))

        for start_index in range(start, end, display):
            url = f"https://openapi.naver.com/v1/search/local?query={query}&display={display}&start={start_index}"

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            
            try:
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                if rescode == 200:
                    response_body = response.read()
                    response_dict = json.loads(response_body.decode('utf-8'))
                    items = response_dict['items']
                    for item_index in range(len(items)):
                        remove_tag = re.compile('<.*?>')
                        title = re.sub(remove_tag, '', items[item_index]['title'])
                        link = items[item_index]['link']
                        address = re.sub(remove_tag, '', items[item_index]['address'])
                        web_df.loc[idx] = [title, link, address]

                        # SearchResult 모델에 데이터 저장
                        SearchResult.objects.create(title=title, link=link, address=address)

                        idx += 1
                else:
                    return HttpResponse(f"Error Code: {rescode}", status=rescode)
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}", status=500)
        
        # DataFrame을 JSON으로 변환하여 반환
        json_records = web_df.reset_index().to_json(orient='records')
        data = json.loads(json_records)
        return JsonResponse(data, safe=False)
