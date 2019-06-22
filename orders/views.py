from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from orders.models import (Pasta, Salad, Pizza, Order, OrderItem, Platter, Sub, Topping)
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
        "Pasta": Pasta.objects.all(),
        "Salad": Salad.objects.all(),
        "Pizza": Pizza.objects.all(),
        "Platter": Platter.objects.all(),
        "Sub": Sub.objects.all(),
        "Topping": Topping.objects.all(),
    }
    return render(request, "orders/index.html", context)

def checkout(request):
    #try:
    #testvalue = request.POST.get["checkoutlist", "defaultvalue"]
    #except MultiValueDictKeyError:
       # testvalue = False
    #print(testvalue)
    currentorder = Order.objects.create(username=request.user.get_username())
    currentdish = Salad.objects.first()
    OrderItem.objects.create(orderID=currentorder,  DishID=currentdish)
    return render(request, "orders/login.html", {"message": "You have ordered succesfully"})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/index.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})
