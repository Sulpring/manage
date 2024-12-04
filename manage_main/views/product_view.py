from django.shortcuts import render, get_object_or_404, redirect
from manage_main.models import User, Product
from django.http import JsonResponse

def product_list_showing_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if(user_id is None):
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

    # 렌더링 데이터
    render_data = {
        'username': user_id,  # user_id가 없으면 Guest로 표시
        'products': product_list
    }

    return render(request, 'products/product_list.html', render_data)

# 수정 뷰
def product_edit_view(request):
    if request.method == "POST":
        print("잉")
        print(request.POST)
        # 원래 값
        original_name = request.POST.get("original_name")
        original_code = request.POST.get("original_code")
        original_img_url = request.POST.get("original_img_url")

        # 새 입력 값
        input_name = request.POST.get("input_name")
        input_code = request.POST.get("input_code")
        input_img_url = request.POST.get("input_img_url")
        input_description = request.POST.get("input_description")

        print(original_name, " ", original_code, " ", original_img_url)
        print(input_name, input_code, input_img_url, input_description)

        # 기존 Product 검색 및 수정
        product = Product.objects.filter(name=original_name, code=original_code, img_url=original_img_url).first()
        if product:
            product.name = input_name
            product.code = input_code
            product.img_url = input_img_url
            product.human_text = input_description
            product.save()
            return redirect('product_list')  # 수정 완료 후 목록 페이지로 리다이렉트
        else:
            return JsonResponse({"message":"Product not found"}, status=404)


# 삭제 뷰
def product_delete_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if(user_id is None):
        return redirect('login')
    
    name = request.POST.get('name')
    code = request.POST.get('code')
    img_url = request.POST.get('img_url')

    # 조건에 맞는 Product 객체 필터링 및 삭제
    products = Product.objects.filter(name=name, code=code, img_url=img_url)
    
    if products.exists():
        products.delete()
        return redirect('product_list')
    else:
        return JsonResponse({"error": "No matching product found."}, status=404)



def product_add_showing_view(request):
    # 요청 헤더에서 쿠키의 'id' 값 가져오기
    user_id = request.COOKIES.get('id', None)

    if(user_id is None):
        return redirect('login')


    # 렌더링 데이터
    render_data = {
        'username': user_id,  
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

    
