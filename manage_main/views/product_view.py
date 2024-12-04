from django.shortcuts import render, get_object_or_404, redirect
from manage_main.models import User

def product_list_showing_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if user_id:
        print(f"요청 헤더에서 가져온 user_id: {user_id}")
    else:
        print("user_id 쿠키가 존재하지 않습니다.")

    # 렌더링 데이터
    render_data = {
        'username': user_id if user_id else 'Guest',  # user_id가 없으면 Guest로 표시
        'products': []
    }

    return render(request, 'products/product_list.html', render_data)