
# 회원가입 폼
# 장고 내장 UserCreationForm을 상속하여 구현한다

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# CreateUserView 에서 사용한다
class CreateUserForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User # 장고 내장 User
        fields = (
            'username', "email", "password1", "password2"
        )

    # 저장 함수 오버라이딩
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        # 부모를 호출해서 저장하겠다

        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user # 저장하고 반환하는구나


