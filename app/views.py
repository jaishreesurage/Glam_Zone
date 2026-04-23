from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .models import Profile
from django.shortcuts import render, get_object_or_404
from .models import Product,Brand
# Create your views here.

# logo view 
def LogoPage(request):
    return render(request,"app/logo.html")

#welcome view 
def welcome(request):
    return render(request, "app/welcome.html")

# =========================
# SIGNUP VIEW
# =========================
def signup_page(request):

    # check form submit
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")


        # check username already exist
        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists")
            return redirect("signup_page")


        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        # create profile
        Profile.objects.create(
            user=user,
            full_name=full_name,
            email=email,
            
        )


        messages.success(request, "Signup successful")
        return redirect("login_page")


    return render(request, "app/signup.html")



# =========================
# LOGIN VIEW
# =========================
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        # authenticate user
        user = authenticate(request, username=username, password=password)


        if user is not None:

            login(request, user)

            return redirect("login_success")

        else:

            messages.error(request, "Invalid username or password")
            return redirect("brands")


    return render(request, "app/login.html")



# =========================
# LOGIN SUCCESS VIEW
# =========================
def login_success(request):

    return render(request, "app/login_success.html")


# Show all brands
def brands(request):

    # Get all brands from database
    brands = Brand.objects.all()

    return render(request, "app/brands.html", {"brands": brands})


# Show products of selected brand
def products(request, brand_id):

    products = Product.objects.filter(brand_id=brand_id)

    return render(request, "app/product.html", {"products": products})


# Add to Cart (sirf product add karega)
def add_to_cart(request, product_id):

    cart = request.session.get('cart', [])   # session se cart lo

    cart.append(product_id)                  # product add karo

    request.session['cart'] = cart           # save karo

    return redirect('cart')                  # cart page par bhejo


#  Cart Page (sirf show karega)
def cart(request):

    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)

    total = sum(product.price for product in products)

    return render(request, "app/cart.html", {
        'products': products,
        'total': total
    })

def remove_from_cart(request, product_id):

    cart = request.session.get('cart', [])

    # अगर product cart में है → remove करो
    if product_id in cart:
        cart.remove(product_id)

    request.session['cart'] = cart

    return redirect('cart')

# Buy Now
def buy_now(request, product_id):

    # single product store
    request.session['buy_now'] = product_id

    return redirect('checkout')

def checkout(request):
    product_id = request.session.get('buy_now')

    product = None

    if product_id:
        product = get_object_or_404(Product, id=product_id)

    return render(request, "app/checkout.html", {'product': product})