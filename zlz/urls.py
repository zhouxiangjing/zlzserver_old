from django.urls import path
from zlz import views as zlz_views
from zlz import restapi as zlz_restapi

# router = routers.DefaultRouter()
# router.register(r'devices' , zlz_restapi.DevicesViewSet)

urlpatterns = [

    path('', zlz_views.index, name='index'),
    path('media/', zlz_views.media),

    path('api/devices/', zlz_restapi.DevicesAPIView.as_view()),
]