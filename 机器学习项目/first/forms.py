from django import forms
from first.models import *
from django.core import validators


# 注册界面
class RegisterForm(forms.ModelForm):
    user_password2 = forms.CharField(validators=[validators.MinLengthValidator(6, message='最小长度为6'),validators.MaxLengthValidator(16, message='最大长度为16')])
    user_phone=forms.CharField(validators=[validators.MaxLengthValidator(11,message='手机号码长度为11位'),validators.MinLengthValidator(11,message='手机号码长度为11位')])
    class Meta:
        model=User
        fields="__all__"

    def clean_user_phone(self):
        phone = self.cleaned_data.get('user_phone')
        if User.objects.filter(user_phone=phone).exists():
            raise forms.ValidationError("用户名已存在")
        else:
            return phone
    # 用户名唯一
    def clean_user_name(self):
        name=self.cleaned_data.get('user_name')
        if User.objects.filter(user_name=name).exists():
            raise forms.ValidationError("用户名已存在")
        else:
            return name

    # 密码是否一致
    def clean(self):
        password = self.cleaned_data.get("user_password")
        password2 = self.cleaned_data.get("user_password2")
        if password!=password2:
            raise forms.ValidationError("两次密码不一致")

    #报错数据结构优化
    def get_simple(self):
        e_dict=self.errors.get_json_data()
        r_dict={}
        for k,v in e_dict.items():
            r_list=[]
            for e in v:
                msg=e['message']
                r_list.append(msg)
            r_dict[k] = r_list
        return r_dict


# 登录界面
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["user_name","user_password"]

    # 电话号码唯一
    def clean_user_phone(self):
        name = self.cleaned_data.get('user_name')
        if User.objects.filter(user_phone=name).exists():
            raise forms.ValidationError("电话号码已存在")
        else:
            return name



