from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    phone = forms.CharField(label="手机号", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = forms.CharField(label="验证码", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        (0, "保密"),
        (1, "男"),
        (2, "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), )
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

# class UserForm(forms.Form):
#     user = forms.CharField(max_length=32,
#                            error_messages={"required": "该字段不能为空"},
#                            label="用户名",
#                            widget=widgets.TextInput(attrs={"class": "form-control"}, ))
#     pwd = forms.CharField(max_length=32,
#                           label="密码",
#                           widget=widgets.PasswordInput(attrs={"class": "form-control"}, ))
#     re_pwd = forms.CharField(max_length=32,
#                              label="确认密码",
#                              widget=widgets.PasswordInput(attrs={"class": "form-control"}, ))
#     email = forms.EmailField(max_length=32,
#                              label="邮箱",
#                              widget=widgets.EmailInput(attrs={"class": "form-control"}, ))
#
#     def clean_user(self):
#         val = self.cleaned_data.get('user')
#         user = UserInfo.objects.filter(username=val).first()
#         if not user:
#             return val
#         else:
#             raise ValidationError('该用户名已被注册')
#
#     def clean(self):
#         pwd = self.cleaned_data.get('pwd')
#         re_pwd = self.cleaned_data.get('re_pwd')
#         if pwd and re_pwd:
#             if pwd == re_pwd:
#                 return self.cleaned_data
#             else:
#                 raise ValidationError('两次密码不一致')
#         else:
#             return self.cleaned_data