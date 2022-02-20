from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/ftp', views.ftp_view, name='ftp_view'),
    path('pages/common', views.common_view, name='common_view'),
    path('signup', views.signup_view, name='signup'),
    path('error', views.no_authorization, name='no_authorization')
]
