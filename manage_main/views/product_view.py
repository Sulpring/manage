from django.shortcuts import render, get_object_or_404, redirect
from manage_main.models import User, Product

def product_list_showing_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if(user_id is None):
        print('응애')
        return redirect('login')

    products = Product.objects.filter(user_id=user_id)
    # 배열 형태로 변환
    product_list = [
        {
            "name": product.name,
            "code": product.code,
            "img_url": product.img_url,
            "description": product.human_text or product.ai_text  # human_text가 없으면 ai_text 사용
        }
        for product in products
    ]

    # 결과 확인
    print(product_list)

    # 렌더링 데이터
    render_data = {
        'username': user_id,  # user_id가 없으면 Guest로 표시
        'products': product_list
    }

    return render(request, 'products/product_list.html', render_data)

def product_add_showing_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if(user_id is None):
        return redirect('login')


    # 렌더링 데이터
    render_data = {
        'username': user_id,  # user_id가 없으면 Guest로 표시
        'products': []
    }

    return render(request, 'products/product_add.html', render_data)
    
def product_add_process_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    print(user_id)

    # 저장 로직
    user = User.objects.filter(id=user_id).first() or False

    if(user == False):
        return redirect('login')
    
    new_product = Product(
        user=user,
        name=request.POST.get('name'),
        code=str(request.POST.get('code')),
        img_url=request.POST.get('img_url'),
        human_text=request.POST.get('description'),
        ai_text=None
    )

    new_product.save()

    return redirect('product_list')

    
