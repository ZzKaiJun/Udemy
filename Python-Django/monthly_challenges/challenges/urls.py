
from django.urls import path
from . import views

# ------每個月份的url設置------
# urlpatterns = [
#     path('january', views.january),
#     path('february', views.february),
#     path('march', views.march),
# ]

# ------若有很多月份要添加，可能會讓route過於繁多，可以使用 dynamic 動態方法來解決，會將抓到的 month 放到視圖 views ------
urlpatterns = [
    path("", views.index),
    path('<int:month>', views.monthly_challenges_by_number),    # 輸入數字1~12也能對應到該月份
    # name="month-challenge"  為 keyword argument ，讓url創建特定路徑給它
    path('<str:month>', views.monthly_challenges , name="month-challenge"),    # <>  placeholder ，<month> 可能被替換成 january、february、march 等等...  
]




