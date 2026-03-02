from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.LogoPage, name='LogoPage'),
    path('welcome/', views.welcome, name='welcome'),
]