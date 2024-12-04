from django.urls import path
from manage_main.views.user_views import (
    index, # 초기화면
    login_view, # 로그인 뷰
    
)
# from manage_main.views.product_view import 

urlpatterns = [
    path('/', index),
    path('login/', login_view, name='login'),
]
