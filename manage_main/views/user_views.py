from django.shortcuts import render, redirect
from django.http import JsonResponse
# 모델
from manage_main.models import User

# 초기화면(=로그인 화면) 보여주기
def index_view(request):
    return redirect('login')

# 로그인 화면 보여주기
def login_showing_view(request):
    return render(request, 'users/login.html')

# 로그인 로직
def login_process_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        password = request.POST.get('password')
        # 데스트
        print('아이디: ', user_id)
        print("비번: ", password)

        # 로그인 로직
        user = User.objects.filter(id=user_id).first() or False # 없으면 False
        if((user == False) or user.password != password): # 아이디가 없거나 비번이 잘못되면
            response = {"error": '아이디 또는 비밀번호가 없거나 잘못되었습니다'}
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        else:
            # return redirect('home')  # 인증 성공 시 홈으로 리다이렉트
            return JsonResponse({"message": "로그인 성공"}, json_dumps_params={'ensure_ascii': False})
    return render(request, 'users/login.html')

# 레지스터 보여주는 뷰
def register_showing_view(request):
    return render(request, 'users/register.html')

def register_process_view(request):
    if(request.method == 'POST'):
        user_id = request.POST.get('id')
        password = request.POST.get('password')

        print("하이")
        user = User.objects.filter(id=user_id).first() or False # 없으면 False
        if(user == False): # 없으면 정상작동
            new_user = User(
                id = user_id,
                password = password
            )
            new_user.save()
            return JsonResponse({"message": "생성이 완료 되었습니다."}, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"message":"이미 존재하는 계정입니다."}, json_dumps_params={'ensure_ascii': False})

