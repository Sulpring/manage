from django.shortcuts import render

# 초기화면(=로그인 화면) 보여주기
def index_view(request):
    return render(request, 'users/login.html')

# 로그인 로직
def login_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        password = request.POST.get('password')
        print('아이디 비번')
        print(user_id, " ", password)
        # 로그인 처리 로직 (예: 사용자 인증)
        # if user_id == "admin" and password == "password123":
        #     return redirect('home')  # 인증 성공 시 홈으로 리다이렉트
        # else:
        #     return render(request, 'user_product/login.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    return render(request, 'user_product/login.html')

