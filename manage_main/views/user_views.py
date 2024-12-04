from django.shortcuts import render

# 초기화면(=로그인 화면) 보여주기
def index(request):
    return render(request, 'user_product/login.html')

# 로그인 로직
def login_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        password = request.POST.get('password')

        # 여기에 로그인 로직
        # 그냥 user_id로 찾고, password가 일치하면 확인
        print("로그인 완료에요")
        return 'hi'

        # return redirect('home')  # 로그인 성공 시 홈으로 리다이렉트
    return render(request, 'user_product/login.html')
