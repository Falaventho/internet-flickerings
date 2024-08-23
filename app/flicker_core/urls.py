from django.contrib import admin
from django.urls import path
from flicker_core import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('watch/<int:media_id>/', views.watch, name='watch'),
    path('accounts/signup/', views.signup, name='signup'),
]
