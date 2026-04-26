from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.LogoPage, name='LogoPage'),
    path('welcome/', views.welcome, name='welcome'),

    path('signup/', views.signup_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('brands/', views.brands, name="brands"),
    path('products/<int:brand_id>/', views.products, name="products"),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('checkout/', views.checkout, name='checkout'),
]