from django.shortcuts import render
from products.models import Product
from django.contrib import messages

# Create your views here.
def do_search(request):
    # a view to find products that match the search word entered by user
    products = Product.objects.filter(name__icontains=request.GET['q'])
    messages.success(request, "Search results:")
    return render(request, "products.html", {"products": products})