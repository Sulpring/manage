from django.urls import path
from manage_main.views.user_views import (
    index_view, # 초기화면
    login_showing_view, # 로그인 템플릿 뷰
    login_process_view, # 로그인 처리 뷰
    register_showing_view, # 계정등록 템플릿 뷰
    register_process_view, # 계정등록 처리 뷰
)
from manage_main.views.product_view import (
    product_list_showing_view, # 프로덕트 리스트 템플릿 뷰
    product_add_showing_view, # 프로덕트 추가 템플릿 뷰
    product_add_process_view, # 프로덕트 추가 처리 뷰
    product_delete_view, # 프로덕트 삭제 뷰
    product_edit_view, # 프로덕트 수정 뷰
)

urlpatterns = [
    path('', index_view, name='index'), # 초기화면
    path('login/', login_showing_view, name='login'), # 로그인 화면
    path('login/process/', login_process_view), # 로그인 처리
    path('register/', register_showing_view), # 계정등록 화면
    path('register/process/', register_process_view), # 계정등록 화면

    path('product/list/', product_list_showing_view, name='product_list'), # 프로덕트 리스트 화면
    path('product/add/', product_add_showing_view), # 프로덕트 추가 화면
    path('product/add/process/', product_add_process_view), # 프로덕트 추가 뷰
    path('product/delete/', product_delete_view), # 프로덕트 삭제 뷰
    path('product/edit/', product_edit_view), # 프로덕트 수정 뷰
]
