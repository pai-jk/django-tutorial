from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        # 계정 생성 코드
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')
        email = request.POST.get('email')
        region = request.POST.get('region')
        phone_number = request.POST.get('phone_number')
        if password == check_password:
            CustomUser.objects.create(username=userid,
                                      password=password,
                                      email=email,
                                      region=region,
                                      phone_number=phone_number,
                                      )
            return HttpResponse("계정 생성 완료")
        else:
            return HttpResponse("확인 비밀번호가 다릅니다.")
    elif request.method == "GET":
        # 계정 생성 화면 보여주기
        return render(request, 'accounts/signup.html')


@csrf_exempt
def signup_form(request):
    if request.method == "POST":
        # 계정 생성 코드
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("계정 생성 완료")
        else:
            return render(request, 'accounts/signup_form.html', context={'errors': form.errors})
    elif request.method == "GET":
        # 계정 생성 화면 보여주기
        form = CustomUserCreationForm()  # <-바뀐 부분
        return render(request, 'accounts/signup_form.html', context={'form': form})


def login(request):
    if request.method == "POST":
        # 로그인하는 코드
        # Quest index 화면으로 전달
        return HttpResponse(200)
    elif request.method == "GET":
        # 로그인 화면 보여주기
        return render(200)


def delete(request):
    return HttpResponse(200)
