# imports required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import  messages
from app.models import  *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import  login_required


# home page
def index(request):
    context = {
    'products': Product.objects.all(),
    }
    return render(request,"index.html",context)


# users urls
# login page
def login_page(request):
    return render(request,"login.html",{})

# login function
def login_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect("app:index")
    else:
        messages.info(request,"username or password incorrect[login failed]")
        return redirect("app:login_page")

# logout function
@login_required()
def logout_view(request):
    logout(request)
    messages.info(request,"[logout success]")
    return redirect("app:index")

# signup page
def signup_page(request):
    if request.user.is_authenticated==True:
        return render(request,"index.html",{})
    else:
        return render(request,"signup.html",{})

# signup function
def signup_view(request):
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        image=request.FILES['picture']
        slug=request.POST['slug']
        if User.objects.filter(username=username):
            messages.info(request,"faild ..user already exists")
            return redirect("app:signup_page")
        elif User.objects.filter(email=email):
            messages.info(request,"failed...email already taken")
            return redirect("app:signup_page")
        elif password1!=password2:
            messages.info(request,"failed...password not mached")
            return redirect("app:signup_page")
        else:
            user=User.objects.create_user(username=username,email=email,password=password2,picture=image,slug=slug)
            user.save();
            messages.info(request,"signup successful")
            return redirect("app:login_page")
    else:
        return redirect("app:signup_page")

# reset page
def reset_page(request):
    return render(request,"reset.html")

# reset function
def reset_password_view(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        res=User.objects.filter(email=email)
        if res:
            user=User.objects.get(email=email)
            user.set_password(password)
            user.save();
            messages.info(request,"password reset successful")
            return redirect("app:login_page")
        else:
            messages.info(request,"email not matched")
            return redirect("app:reset_page")
    else:
        return redirect("app:reset_page")

@login_required()
def update_profile_page(request):
    return render(request,"update_profile_page.html")

@login_required()
def update_profile(request,slug):
    user=User.objects.get(slug=slug)
    if request.method=='POST'and request.FILES['picture']:
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        image=request.FILES['picture']
        username=username
        user.email=email
        user.phone=phone
        user.address=address
        user.picture=image
        user.save()
        return redirect("app:index")


def save_contact(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        contact=Contacts.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone,address=address)
        contact.save()
        return redirect("app:index")

@login_required()
def detail(request,id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, "detail.html", context)

@login_required()
def add_cart(request, id):
    product=Product.objects.get(id=id)
    user=request.user
    if Cart.objects.filter(product=product, customer=user):
        Cart.objects.filter(product=product, customer=user).delete()
    cart=Cart(product=product,customer=user)
    cart.save()
    return redirect("app:view_cart")

@login_required()
def view_cart(request):
    return render(request, "cart_detail.html")

@login_required()
def add_order(request, id):
    product = Product.objects.get(id=id)
    user = request.user
    Order(product=product, customer=user).save()
    if Cart.objects.filter(product=product, customer=user):
        Cart.objects.filter(product=product, customer=user).delete()
    return redirect("app:view_order")

@login_required()
def view_order(request):
    return render(request, "order_detail.html")

@login_required()
def remove_order(request,id):
    Order.objects.get(id=id).delete()
    return redirect("app:view_order")

@login_required()
def remove_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect("app:view_cart")



