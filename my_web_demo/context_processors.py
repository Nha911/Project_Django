from .models import CartItem, Wishlist
from decimal import Decimal

def cart_context(request):
    cart_items = []
    total_cost = Decimal('0.00')
    cart_item_count = 0
    wishlist_product_ids = []
    total_original_price = Decimal('0.00')
    total_savings = Decimal('0.00')

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        cart_item_count = cart_items.count()
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)

        if cart_items:
            total_cost = sum(item.total_price for item in cart_items)
            total_original_price = sum(item.product.price * item.quantity for item in cart_items)
            total_savings = total_original_price - total_cost

    return {
        'cart_items': cart_items,
        'cart_total_cost': total_cost,  # Amount to pay
        'cart_item_count': cart_item_count,
        'wishlist_product_ids': wishlist_product_ids,
        'cart_total_original_price': total_original_price,
        'cart_total_savings': total_savings,
    }
