from django.shortcuts import render, redirect
# Create your views here.

def mapview(request):
    return render(request, "result.html")

def re_list(request):
    name = "샐러드"
    return render(request, 'list.html', {"name": name})

def map_salad(request):
    return render(request, 'result_salad.html')


def test(request):
    result = None
    if request.method == "POST":
        if "button1" in request.POST:
            result = "버튼 1이 클릭되었습니다."
        elif "button2" in request.POST:
            result = "버튼 2가 클릭되었습니다."
    
    return render(request, 'test.html', {'result': result})
