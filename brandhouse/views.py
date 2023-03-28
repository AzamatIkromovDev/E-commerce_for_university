from django.shortcuts import render
from store.models import Product


def home(request):
    product = Product.objects.all().filter(is_available=True)
    contex  = {
        'products' :product,
    }
    return render(request,'home.html',contex)