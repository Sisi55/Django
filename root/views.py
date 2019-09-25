
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from django.shortcuts import render


class CreateUserView(CreateView):
    # form 혹은 model 과 연결되서 새로운 데이터를 넣을 때 사용

    template_name = 'registration/signup.html'
    # 폼만 달랑있는 화면. 다시 여기로 전송되네
    form_class = CreateUserForm # 내장 회원가입 폼 커스터마이징한다
    # 사용할 폼

    success_url = reverse_lazy('create_user_done') # url name
    # 성공하면 이동


class RegisteredView(TemplateView):

    template_name = 'registration/signup_done.html'
    # 성공하면 이동하는 화면
    # 달랑 환영 문자 출력


def index(request):
    
    return render(request, 'base.html', {})






