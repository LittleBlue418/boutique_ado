from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ A view to return all products, including sorting & search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        # Filter by category (split where multiple)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Filter by search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                    'You have not entered a search criteria')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


# View to show individual product details
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
