from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from llts import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^organizations/$', views.OrganizationList.as_view()),
    url(r'^organizations/(?P<pk>[0-9]+)/$', views.OrganizationDetail.as_view()),
    url(r'^households/$', views.HouseholdList.as_view()),
    url(r'^households/(?P<pk>[0-9]+)/$', views.HouseholdDetail.as_view()),
    url(r'^members/$', views.MemberList.as_view()),
    url(r'^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    url(r'^districts/$', views.DistrictList.as_view()),
    url(r'^districts/(?P<pk>[0-9]+)/$', views.DistrictDetail.as_view()),
    url(r'^companionships/$', views.CompanionshipList.as_view()),
    url(r'^companionships/(?P<pk>[0-9]+)/$', views.CompanionshipDetail.as_view()),
    url(r'^assignments/$', views.AssignmentList.as_view()),
    url(r'^assignments/(?P<pk>[0-9]+)/$', views.AssignmentDetail.as_view()),
    url(r'^visits/$', views.VisitList.as_view()),
    url(r'^visits/(?P<pk>[0-9]+)/$', views.VisitDetail.as_view()),
    url(r'^api-auth-create/$', views.Register.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
