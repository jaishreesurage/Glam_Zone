from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.LogoPage, name='LogoPage'),
    path('welcome/', views.welcome, name='welcome'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.login_page, name='login_page'),
    path('login/',views.login_success, name='login_success'),
    path('brands/', views.brands, name="brands"),
    path('products/<int:brand_id>/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),

]