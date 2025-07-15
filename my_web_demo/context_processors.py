from .models import CartItem

def cart_context(request):
    cart_items = []
    total_cost = 0
    cart_item_count = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_cost = sum(item.total_price for item in cart_items)
        cart_item_count = cart_items.count()
    return {
        'cart_items': cart_items,
        'cart_total_cost': total_cost,
        'cart_item_count': cart_item_count
    }
