import urllib.request
import ssl
import json
import pandas as pd
import re
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import SearchResult

ssl._create_default_https_context = ssl._create_unverified_context

client_id = "5xqa38sj2upsYMMShhe1"
client_secret = "ZlpBR5K8cr"

def search(request):
    if request.method == 'GET':
        return render(request, 'search_form.html')
    
    if request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            return HttpResponse("검색 질의를 입력해 주세요.", status=400)

        idx = 0
        display = 100
        start = 1
        end = 1000

        query = urllib.parse.quote(query)
        web_df = pd.DataFrame(columns=("Title", "Link", "Address"))

        for start_index in range(start, end, display):
            url = "https://openapi.naver.com/v1/search/local?query=" + query \
                  + "&display=" + str(display) \
                  + "&start=" + str(start_index)

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                response_dict = json.loads(response_body.decode('utf-8'))
                items = response_dict['items']
                for item_index in range(0, len(items)):
                    remove_tag = re.compile('<.*?>')
                    title = re.sub(remove_tag, '', items[item_index]['title'])
                    link = items[item_index]['link']
                    address = re.sub(remove_tag, '', items[item_index]['address'])
                    web_df.loc[idx] = [title, link, address]
                    if not SearchResult.objects.filter(link=link).exists():
                            SearchResult.objects.create(title=title, link=link, address=address)

                    idx += 1
            else:
                return HttpResponse(f"Error Code: {rescode}", status=rescode)
        
        # Returning the DataFrame as JSON response
        json_records = web_df.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        return JsonResponse(data, safe=False)