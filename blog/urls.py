from django.urls import path, include
from blog import views as blog_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('favicon.ico', RedirectView.as_view(url=r'static/blog/img/favicon.ico')),

    path('captcha', include('captcha.urls')),

    path('', blog_views.index),
    path('index/', blog_views.index),
    path('login/', blog_views.login),
    path('register/', blog_views.register),
    path('logout/', blog_views.logout),
    path('confirm/', blog_views.email_confirm),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article_detail/<int:id>/', blog_views.article_detail, name='article_detail'),

    # path('', blog_views.index, name='index'),
    # path('index/', blog_views.index, name='index'),
    # path('register/', blog_views.register),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)