from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('about', views.about, name="about"),
    path('', views.home, name="home"),
    path('generate_password/', views.password, name='password')   
]
