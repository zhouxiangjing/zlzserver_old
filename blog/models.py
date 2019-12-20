from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from blog.utils import *


class User(models.Model):

    gender_val = (
        (0, "保密"),
        (1, "男"),
        (2, "女"),
    )

    role_val = (
        (0, "普通会员"),
        (1, "管理员"),
    )

    id = models.CharField(primary_key=True, max_length=50, default=next_id)
    phone = models.CharField(verbose_name='手机号', max_length=128)
    username = models.CharField(verbose_name='用户名', max_length=128, default=get_name)
    password = models.CharField(verbose_name='密码', max_length=128, default="")
    avatar = models.CharField(verbose_name='头像', max_length=256, default="")
    email = models.EmailField(verbose_name='邮箱', max_length=256, default="")
    gender = models.IntegerField(verbose_name='性别', choices=gender_val, default=0)
    role = models.IntegerField(verbose_name='角色', choices=role_val, default=0)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)

    def __str__(self):
        return self.username + ' ' + self.phone

    class Meta:
        ordering = ["-created"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-created"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


class SmsCode(models.Model):
    phone = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-updated"]
        verbose_name = "验证码"
        verbose_name_plural = "验证码"


class Article(models.Model):

    title = models.CharField(verbose_name='文章标题', max_length=50)
    desc = models.CharField(verbose_name='文章描述', max_length=255)
    content = RichTextUploadingField(verbose_name='文章内容')

    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    up_count = models.IntegerField(verbose_name='点赞数', default=0)
    down_count = models.IntegerField(verbose_name='踩踩数', default=0)

    user = models.ForeignKey(verbose_name='作者', to='User', to_field='id', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    category = models.ManyToManyField(verbose_name='分类', to='Category', through='Article2Category', through_fields=('article', 'category'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Category(models.Model):

    title = models.CharField(verbose_name='分类标题', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Article2Category(models.Model):
    article = models.ForeignKey(verbose_name='文章ID', to="Article", to_field='id', on_delete=models.CASCADE)
    category = models.ForeignKey(verbose_name='分类ID', to="Category", to_field='id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章-分类'
        verbose_name_plural = '文章-分类'
        unique_together = [
            ('article', 'category'),
        ]

    def __str__(self):
        v = self.article.title + "---" + self.category.title
        return v


class Comment(models.Model):

    content = models.CharField(verbose_name='评论内容', max_length=255)
    article = models.ForeignKey(verbose_name='文章ID', to="Article", to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='作者ID', to='User', to_field='id', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='评论级别', default=1)
    parent_id = models.IntegerField(verbose_name='评论父级ID', default=0)
    created = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.content
