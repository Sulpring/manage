from django.urls import path
from manage_main.views.user_views import (
    login_view, # 로그인 뷰
)
# from manage_main.views.product_view import 

urlpatterns = [
path('login/', login_view, name='login'),
]
