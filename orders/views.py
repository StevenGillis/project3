from django.http import HttpResponse
from django.shortcuts import render
from orders.models import (Pasta, Salad)
# Create your views here.
def index(request):
    context = {
        "Pasta": Pasta.objects.all(),
        "Salad": Salad.objects.all(),
    }
    return render(request, "orders/index.html", context)
