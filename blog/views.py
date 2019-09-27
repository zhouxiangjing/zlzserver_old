from django.shortcuts import render, redirect

import os
import json

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.conf import settings

from blog.form import *
from blog.models import *
from bs4 import BeautifulSoup
from zlzserver.settings import BASE_DIR
import hashlib
import datetime


def hash_code(s, salt='zlz'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # update方法只接收bytes类型
    return h.hexdigest()


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.username, now)
    ConfirmString.objects.create(code=code, user=user,)
    return code


def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives
    subject = '来自www.xxxxx.com的测试邮件'
    from_email = settings.EMAIL_HOST_USER
    email_to = settings.EMAIL_HOST_USER
    text_content = '欢迎访问www.xxxxx.com，这里是xx站点，专注于xx技术的分享！'
    html_content = '<p>欢迎注册<a href="http://{}/confirm/?code={}" target="blank>www.xxx.com</a>，这里是xx的站点，专注于xx技术的分享！</p>'.format('127.0.0.1', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email_to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def my_paginator(request, article_list):
    paginator = Paginator(article_list, 15)
    page = request.GET.get('page', 1)
    currentPage = int(page)

    #  如果页数十分多时，换另外一种显示方式
    if paginator.num_pages > 11:
        if currentPage - 5 < 1:
            pageRange = range(1, 11)
        elif currentPage + 5 > paginator.num_pages:
            pageRange = range(currentPage - 5, paginator.num_pages + 1)
        else:
            pageRange = range(currentPage - 5, currentPage + 5)
    else:
        pageRange = paginator.page_range
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return pageRange, paginator, article_list


def email_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'blog/confirm.html', locals())

    create_time = confirm.create_time
    now = datetime.datetime.now()
    if now > create_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'blog/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'blog/confirm.html', locals())


def base(request):
    pass
    return render(request, 'blog/base.html')


def index(request):
    article_list = Article.objects.order_by('pk').all().reverse()
    category_list = list(Category.objects.annotate(count=Count('article')))
    page_range, paginator, article_list = my_paginator(request, article_list)

    return render(request, 'blog/index.html',
                  {'article_list': article_list,
                   'category_list': category_list,
                   'paginator': paginator,
                   'pageRange': page_range})


def login(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    if request.method == "GET":
        login_from = request.META.get('HTTP_REFERER', '/')
        if '/login' not in login_from:
            request.session['login_from'] = login_from
        login_form = UserForm()
        return render(request, 'blog/login.html', locals())
    elif request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                # if not user.has_confirmed:
                #     message = "该用户还未通过邮件确认！"
                #     return render(request, 'login/login.html', locals())
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return HttpResponseRedirect(request.session['login_from'])
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'blog/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'blog/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'blog/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'blog/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往注册邮箱，进行邮件确认！'
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'blog/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    login_from = request.META.get('HTTP_REFERER', '/')
    request.session.flush()
    return HttpResponseRedirect(login_from)


def article_detail(request, id):

    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article_id=id)

    response_data = {
        'article_id': id,
        'article': article,
        'comments': comments,
        'comment_api': '/api/comment/',
    }

    return render(request, 'blog/detail.html', response_data)






# def index(request):
#
#     article_list = Article.objects.order_by('pk').all().reverse()
#     category_list = list(Category.objects.annotate(count=Count('article')))
#     pageRange, paginator, article_list = my_paginator(request, article_list)
#
#     if request.method == 'POST':
#         if request.POST:
#             username = request.POST.get('username', '')
#             nn = 0
#
#         return render(request, 'blog/index.html',
#                       {'article_list': article_list,
#                        'category_list': category_list,
#                        'paginator': paginator,
#                        'pageRange': pageRange})
#
#     return render(request, 'blog/index.html',
#                   {'article_list': article_list,
#                    'category_list': category_list,
#                    'paginator': paginator,
#                    'pageRange': pageRange})
#
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = UserInfo.objects.filter(username=username, password=password)
#         print(user)
#         print(user)
#         if user:
#             #登录成功
#             # 1，生成特殊字符串
#             # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
#             # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
#             request.session['is_login']='1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
#             # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
#             # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
#             request.session['user_id']=user[0].id
#             return redirect('/index/')
#
# def register(request):
#
#     ret_code = 200
#     error_msg = 'ok'
#     if request.method == 'POST':
#         if request.POST:
#             username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
#             re_password = request.POST.get('re_password', '')
#             sex = request.POST.get('sex', '')
#             birthday = request.POST.get('birthday', '')
#             phone = request.POST.get('phone', '')
#             email = request.POST.get('email', '')
#
#             while True:
#                 if password != re_password:
#                     error_msg = '密码不一致'
#                     break
#
#                 user = UserInfo.objects.filter(username=username).first()
#                 if user:
#                     error_msg = '该用户名已被注册'
#                     break
#
#                 break
#
#             UserInfo.objects.create(username=username,
#                 password=password,
#                 sex=sex,
#                 birthday=birthday,
#                 telephone=phone,
#                 email=email)
#
#             ret_data = {'ret_code': ret_code, 'error_msg': error_msg, 'username': username}
#
#             return HttpResponse(json.dumps(ret_data, ensure_ascii=False),
#                                 content_type='application/json; charset=utf-8')
#
#     return HttpResponse(json.dumps({'ret_code': ret_code, 'error_msg': error_msg}, ensure_ascii=False),
#                         content_type='application/json; charset=utf-8')
