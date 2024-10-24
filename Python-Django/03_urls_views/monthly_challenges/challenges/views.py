from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# ---------view 可能為 function 或是 class  ，這裡先從function開始------------------
# def january(request):  #接受請求
#     return HttpResponse("Eat no meat entrie month!")  #回傳響應

# def february(request):  #接受請求
#     return HttpResponse("Walk at least 30 minutes every days!")  #回傳響應

# def march(request):     #接受請求
#     return HttpResponse("Learn Django at least 30 minutes!")  #回傳響應


# ---------若有很多月份要添加，可能會讓route過於繁多，可以使用 dynamic 動態方法來解決--------------------
# 傳入的 month 參數名稱必須要和 urls配置的一樣

# def monthly_challenges(request , month):
#     response_text = None
#     if month == "january":
#         response_text = "Eat no meat entrie month!"
#     elif month == "february":
#         response_text = "Walk at least 30 minutes every days!"
#     elif month == "march":
#         response_text = "Learn Django at least 30 minutes!"
#     else:   # 回傳找不到此頁面 404
#         return HttpResponseNotFound("This month is not supported! ")
    
#     return HttpResponse(response_text)



# 利用字典來代替 if elif 判斷式
dic_monthly_challenges = {
    "january": "Eat no meat entrie month!",
    "february": "Walk at least 30 minutes every days!",
    "march": "Learn Django at least 30 minutes!",
    "april": "Learn Django at least 30 minutes!",
    "may": "Learn Django at least 30 minutes!",
    "june": "Learn Django at least 30 minutes!",
    "july": "Learn Django at least 30 minutes!",
    "august": "Learn Django at least 30 minutes!",
    "september": "Learn Django at least 30 minutes!",
    "october": "Learn Django at least 30 minutes!",
    "november": "Learn Django at least 30 minutes!",
    "december": "Learn Django at least 30 minutes!",
}


# 傳入為數字 (1~12)  會重新導向至對應的月份
def monthly_challenges_by_number(request , month):
    months = list(dic_monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("404 ! Page not found!")
    
    
    redirect_month = months[month-1]  # 取得月份  -1 因為python是從0開始數
    redirect_path = reverse("month-challenge" , args=[redirect_month])     # /challenges/january

    # 重新導向
    return HttpResponseRedirect(redirect_path)
    return HttpResponseRedirect("/challenges/" + redirect_month)   # 會有問題的寫法，因為 urls 是在 monthly_chanllenges.urls.py 設定的，若有修改，很多地方會需要更動



def monthly_challenges(request , month):
    try:
        response_text = dic_monthly_challenges[month]

        response_data = f"<h1>{response_text}</h1>"    # 回傳簡易的html格式
        return HttpResponse(response_data)
        return HttpResponse(response_text)
    except:   # 回傳找不到此頁面 404
        return HttpResponseNotFound("This month is not supported! ")

# 建立首頁，能夠點擊各月份連結就能連接到該月份的網址
def index(request):
    items_context = ""
    months = list(dic_monthly_challenges.keys())

    for month in months:
        month_capitalize = month.capitalize()
        month_path = reverse("month-challenge" , args=[month])

        items_context += f"<li><a href=\"{month_path}\">{month_capitalize}</a></li>"

    
        # <ul>
        #     <li><a href="">January</a></li>
        #     ......
        # </ul>
    

    response_data = f"<ul>{items_context}</ul>"
    return HttpResponse(response_data)
