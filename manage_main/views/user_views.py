from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
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

        # 로그인 로직
        user = User.objects.filter(id=user_id).first() or False
        if (user == False) or (user.password != password):
            # 로그인 실패 응답
            return JsonResponse({"error": "아이디 또는 비밀번호가 없거나 잘못되었습니다"}, status=400, json_dumps_params={'ensure_ascii': False})

        # 로그인 성공: 쿠키에 { id: 등록된 유저 id } 추가
        success_response = JsonResponse({"message": "로그인 성공"}, status=201, json_dumps_params={'ensure_ascii': False})
        success_response.set_cookie(
            'id', user_id, httponly=True, samesite='Strict', max_age=600  # 유효시간 10분 (600초)
        )
        return success_response

    # 잘못된 요청 처리
    return JsonResponse({"error": "잘못된 요청입니다"}, status=405, json_dumps_params={'ensure_ascii': False})

# 레지스터 보여주는 뷰
def register_showing_view(request):
    return render(request, 'users/register.html')

def register_process_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        password = request.POST.get('password')

        # 중복 계정 확인
        if User.objects.filter(id=user_id).exists():
            return JsonResponse({"error": "이미 존재하는 계정입니다."}, status=400, json_dumps_params={'ensure_ascii': False})

        # 새로운 계정 생성
        new_user = User(id=user_id, password=password)
        new_user.save()

        return JsonResponse({"message": "계정이 성공적으로 등록되었습니다."}, status=201, json_dumps_params={'ensure_ascii': False})

    return JsonResponse({"error": "잘못된 요청입니다."}, status=405, json_dumps_params={'ensure_ascii': False})
