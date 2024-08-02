from django.contrib import admin
from django.urls import path
from flicker_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('browse/', views.browse),
    path('watch/<str:media>', views.watch)
]
