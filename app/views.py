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

# SIGNUP VIEW
def signup_page(request):

    # check form submit
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

         # validations
        if "@" not in email:
            messages.error(request, "Email must contain @")
            return redirect("register")

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect("register")
        
        # check username already exist
        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists")
            return redirect("register")


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
        login(request, user)


        messages.success(request, "Signup successful")
        return redirect("brands")


    return render(request, "app/signup.html")




def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        # authenticate user
        user = authenticate(request, username=username, password=password)


        if user is not None:

            login(request, user)

            return redirect("brands")

        else:

            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "app/login.html")


# Show all brands
def brands(request):

    # Get all brands from database
    brands = Brand.objects.all()

    return render(request, "app/brands.html", {"brands": brands})


# Show products of selected brand
def products(request, brand_id):

    products = Product.objects.filter(brand_id=brand_id)

    return render(request, "app/product.html", {"products": products})

# Product Details Page
def product_details(request, id):

    # selected product
    product = Product.objects.get(id=id)

    # related products
    related_products = Product.objects.filter(
        brand=product.brand
    ).exclude(id=id)

    return render(request, "app/product_details.html", {

        'product': product,

        'related_products': related_products
    })


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

    if product_id in cart:
        cart.remove(product_id)

    request.session['cart'] = cart

    return redirect('cart')

# Buy Now
def buy_now(request, product_id):

    # single product store
    request.session['buy_now'] = product_id

    return redirect('payment')

def payment(request):

    if request.method == "POST":

        return redirect('order_success')

    return render(request, "app/payment.html")


def order_success(request):

    return render(request, "app/order_success.html")

def compare_products(request):

    brands = Brand.objects.all()
    products = Product.objects.all()

    product1 = None
    product2 = None

    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')

    if p1:
        product1 = Product.objects.get(id=p1)

    if p2:
        product2 = Product.objects.get(id=p2)

    return render(request, "app/compare.html", {
        'brands': brands,
        'products': products,
        'product1': product1,
        'product2': product2,
    })

def logout_view(request):
    logout(request)
    return render(request, "app/logout.html")