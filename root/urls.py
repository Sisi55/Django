"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import CreateUserView, RegisteredView, index

urlpatterns = [
    path('admin/', admin.site.urls),




    # 로그인 -- models,views 작성 필요없다
    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),

    # 로그아웃 후 홈으로 리다이렉트
    # path(
    #     'logout/',
    #     auth_views.logout,
    #     {'next_page':'/'}
    # ),

    # 별도의 로그인 템플릿 지정
    # path(
    #     'login/',
    #     auth_views.login,
    #     {'template_name':'login.html'}
    # ),

    # 회원가입
    path(
        'accounts/signup/', # 회원가입 ? 아무튼 커스텀 ?
        CreateUserView.as_view(), 
        name='signup'
    ),
    # 여기로 폼이 전달된다

    path(
        'accounts/login/done/',
        RegisteredView.as_view(),
        name='create_user_done'
    ),
    path(
        '', index
    ),
]
