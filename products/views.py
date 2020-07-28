from django.shortcuts import render
from .models import Product


# View to return all poroducts, including sorting & search queries
def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
