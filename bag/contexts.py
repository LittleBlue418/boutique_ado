from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
        Context for shopping bag for use cross-site
        - Access anywhere
        - Calculates shipping & free shipping threashold
        - Sses session to store and calculate users purchases
        - Returns data + product objects
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Calculating the contentse of the bag
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            # For items that have no size
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product
            })

        else:
            # For items that have a size
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THREASHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THREASHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threashold': settings.FREE_DELIVERY_THREASHOLD,
        'grand_total': grand_total,
    }

    return context
