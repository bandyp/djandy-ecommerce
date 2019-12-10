from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def earrings(request):
    earrings = Product.objects.earrings()
    return render(request, {"products": earrings})
    
def rings(request):
    rings = Product.objects.rings()
    return render(request, {"products": rings})
    
def harmony_bells(request):
    harmony_bells = Product.objects.harmony_bells()
    return render(request, {"products": harmony_bells})

def bracelets(request):
    bracelets = Product.objects.bracelets()
    return render(request, {"products": bracelets})

def necklaces(request):
    necklaces = Product.objects.necklaces()
    return render(request, {"products": necklaces})