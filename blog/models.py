from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class User(models.Model):

    gender = (
        (0, "保密"),
        (1, "男"),
        (2, "女"),
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.IntegerField(choices=gender, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-create_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


class Article(models.Model):

    title = models.CharField(verbose_name='文章标题', max_length=50)
    desc = models.CharField(verbose_name='文章描述', max_length=255)
    content = RichTextUploadingField(verbose_name='文章内容')

    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    up_count = models.IntegerField(verbose_name='点赞数', default=0)
    down_count = models.IntegerField(verbose_name='踩踩数', default=0)

    user = models.ForeignKey(verbose_name='作者', to='User', to_field='id', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
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

