from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^', include('llts.urls')),
    url(r'^api-auth/$', views.obtain_auth_token),
]