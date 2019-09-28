import os
from bs4 import BeautifulSoup
import random


def init_db():
    # user = 'admin'
    # pwd = 'admin'
    # is_staff = 1
    # is_active = 1
    # is_superuser = 1
    # email = 'admin@163.com'
    # avatar_obj = 'avatar'
    # extra = {}
    # UserInfo.objects.create_user(username=user, password=pwd, is_superuser = is_superuser, is_staff=is_staff, is_active=is_active, email=email, **extra)
    #
    # article_list = []
    #
    # for i in range(1, 100):
    #     for c in range(1, 7):
    #         with open(os.path.join('', 'static/superme/%s.txt' % c), 'r', encoding='utf-8') as f:
    #             content = f.read()
    #         soup = BeautifulSoup(content, "html.parser")
    #         for tag in soup.find_all():
    #             if tag.name == "script":
    #                 tag.decompose()
    #         desc = soup.text[0:150] + "..."
    #         c_id = 13 * (i - 1) + random.randrange(1, 9)
    #
    #         article_list.append(Article(desc=desc, title='article_%s' % c_id, content=content, user_id=1))
    #
    # Article.objects.bulk_create(article_list)
    #
    # category_titles = ['生活感悟',
    #                    '编程开发',
    #                    '转载区',
    #                    'Windows/Linux',
    #                    '开源研究']
    #
    # category_list = []
    # for category in category_titles:
    #     category_list.append(Category(title=category))
    #
    # Category.objects.bulk_create(category_list)
    #
    # a2c_list = []
    # a2c_list.append(Article2Category(article_id=1, category_id=1))
    # a2c_list.append(Article2Category(article_id=2, category_id=1))
    # a2c_list.append(Article2Category(article_id=3, category_id=1))
    # Article2Category.objects.bulk_create(a2c_list)
    #
    # tag_title = ['BASIC', 'C',
    #              'C++', 'PASCAL', 'FORTRAN', 'LISP', 'Prolog', 'CLIPS', 'OpenCyc', 'Fazzy', 'Python', 'PHP', 'Ruby',
    #              'Lua']
    #
    # category_list = list(Category.objects.annotate(count=Count('article')))
    # print(category_list)

    nn = 0


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives
    subject = '来自 [ZLZ 个人博客] 的认证邮件'
    from_email = '865295386@qq.com'
    email_to = '865295386@qq.com'
    text_content = '欢迎访问www.xxxxx.com，这里是xx站点，专注于xx技术的分享！'
    html_content = '<p>欢迎注册<a href="http://{}/confirm/?code={}" target="blank">www.xxx.com</a>，这里是xx的站点，专注于xx技术的分享！</p>'.format('127.0.0.1:8000', code, 7)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email_to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zlzserver.settings") #加载项目环境，"BMS.settings"为项目配置文件
    import django
    django.setup()

    from blog.models import *
    from django.db.models.aggregates import Count

    from django.core.mail import send_mail

    # send_email('', 'zxj')

    init_db()