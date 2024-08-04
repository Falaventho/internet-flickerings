from django.contrib import admin
from django.urls import path
from flicker_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('browse/', views.browse),
    path('watch/<int:media_id>/', views.watch),
    path('devwatch/', views.devwatch)
]
