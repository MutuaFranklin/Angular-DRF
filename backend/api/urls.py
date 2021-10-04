from django.urls.conf import include
from . import views
from .views import ProfileList, SearchServiceAPIView, ServiceList
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'users', views.CustomAuthToken)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/',obtain_auth_token),
    path('profiles/', views.ProfileList.as_view()),
    path('services/', views.ServiceList.as_view()),
    path('search/', views.SearchServiceAPIView.as_view()),
    # path('profile/username/',views.ProfileList.as_view()),
    re_path(r'profile/(?P<pk>[0-9]+)/$',views.SingleProfile.as_view()),
    re_path(r'service/(?P<pk>[0-9]+)/$',views.SingleService.as_view()),





]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



