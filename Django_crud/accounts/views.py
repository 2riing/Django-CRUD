from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_GET, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

# 로그인과 로그아웃 가져오기 
from django.contrib.auth import login as auth_login, logout as auth_logout

# 로그인 양식(원래 있는데서 가져옴)
from django.contrib.auth.forms import AuthenticationForm
# 회원가입 양식(내가 만든 accounts/forms.py에서 가져옴)
from .forms import CustomUserCreationFrom

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'movies:index') # 여기도 잘 모르겠음  or next 왜쓰는지 
        else:
            form = AuthenticationForm()
        context = {'form' : form}
        return render(request, 'accounts/login.html', context)
    else:
        # 이미 is_authenticated된 user가 접근하면 인덱스로 보내준다. 
        return redirect('movies:index')
                

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationFrom(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('movies:index')
        else: 
            form = CustomUserCreationFrom()
            # 왜 GET요청도 signup을 하는지 모르겠음
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('movies:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    pass

@login_required
@require_POST
def delete(request):
    pass

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    pass