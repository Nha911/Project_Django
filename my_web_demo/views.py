# --- Login View ---
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .models import Product, Wishlist, CartItem, Order, OrderItem, CustomUser

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Invalid login
            return render(request, 'include/account/login.html', {'login_error': 'Invalid phone number or password.', 'show_login': True})
    return render(request, 'include/account/login.html', {'show_login': True})

# Create your views here.
def Home(request):
    from django.db.models import Q
    # Fetch products for different sections
    discounted_products = Product.objects.filter(discount__gt=0).order_by('-discount')[:8]
    # Sort by descending ID to get the newest products
    new_arrivals = Product.objects.order_by('-id')[:8]
    # Filter for women's fashion items by common keywords in the name
    womens_fashion = Product.objects.filter(Q(name__icontains='Dress') | Q(name__icontains='Top') | Q(name__icontains='Skirt') | Q(name__icontains='Heels')).order_by('?')[:8]
    footwear = Product.objects.filter(Q(name__icontains='shoe') | Q(name__icontains='sneaker') | Q(name__icontains='boot') | Q(name__icontains='sandal')).order_by('?')[:8]
    context = {
        'discounted_products': discounted_products,
        'new_arrivals': new_arrivals,
        'womens_fashion': womens_fashion,
        'footwear': footwear,
    }
    return render(request, 'homeclone.html', context)


# --- Product View ---
def product_list_view(request):
    products = Product.objects.all()
    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    context = {
        'products': products,
        'wishlist_product_ids': wishlist_product_ids
    }
    return render(request, 'product/product_list.html', context)

# --- Wishlist Views ---

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'include/Cart/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # The 'get_or_create' method prevents duplicate entries
    Wishlist.objects.get_or_create(user=request.user, product=product)
    # Redirect back to the page the user was on
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# --- Bag/Cart Views ---

@login_required
def bag_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    # Calculate the total cost of all items in the bag
    total_cost = sum(item.total_price for item in cart_items)
    return render(request, 'order/bag.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def add_to_bag(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        size = request.POST.get('size')
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            size=size,
            # Add color if you have it, for now, we'll leave it out
            # color=request.POST.get('color'), 
            defaults={'quantity': quantity}
        )

        if not created:
            # If the item is already in the cart, just update the quantity
            cart_item.quantity += int(quantity)
            cart_item.save()

        return redirect('bag_view')
    # Redirect to home if not a POST request
    return redirect('home')

@login_required
def move_to_bag(request, wishlist_item_id):
    # This view should only handle POST requests
    if request.method == 'POST':
        wishlist_item = get_object_or_404(Wishlist, id=wishlist_item_id, user=request.user)
        
        # Get color and size from the form submitted on the wishlist page
        color = request.POST.get('color')
        size = request.POST.get('size')
        
        # Create a new cart item
        # Note: You might want more complex logic here, like checking if a similar item
        # (same product, color, size) is already in the cart and just increasing the quantity.
        CartItem.objects.create(
            user=request.user,
            product=wishlist_item.product,
            color=color,
            size=size
        )
        
        # Delete the item from the wishlist
        wishlist_item.delete()
        
        # Redirect the user to their bag to see the newly added item
        return redirect('bag_view')
    
    # If not a POST request, just redirect to the wishlist
    return redirect('wishlist_view')

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.total_price for item in cart_items)

    if not cart_items:
        return redirect('bag_view')

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total_cost)
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                size=item.size,
                color=item.color,
            )
        
        cart_items.delete()
        
        # Redirect to order history to see the new order
        return redirect('order_history')

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost
    }
    return render(request, 'order/checkout.html', context)

def section_view(request):
    return render(request, 'include/Cart/section.html')

def men_extra(request):
    products = Product.objects.all() # You can filter this later, e.g., by category
    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    context = {
        'products': products,
        'wishlist_product_ids': wishlist_product_ids
    }
    return render(request, 'product/men-extra.html', context)

def women_extra(request):
    products = Product.objects.all()
    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    context = {
        'products': products,
        'wishlist_product_ids': wishlist_product_ids
    }
    return render(request, 'product/women-extra.html', context)

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.none()
    
    wishlist_product_ids = []
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)

    context = {
        'query': query,
        'products': products,
        'wishlist_product_ids': wishlist_product_ids
    }
    return render(request, 'product/search_results.html', context)


@login_required
def account_view(request):
    # Ensures the correct template is rendered for the user's account page.
    return render(request, 'account/account.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_history.html', {'orders': orders})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    similar_products = []
    if product.brand:
        similar_products = Product.objects.filter(brand=product.brand).exclude(id=product_id)[:4]
    context = {
        'product': product,
        'similar_products': similar_products
    }
    return render(request, 'product/product_detail.html', context)

def extra_discounts(request):
    # Get products with a discount (assuming we'll add a discount field to the Product model)
    # For now, we'll just get all products and simulate a discount
    products = Product.objects.all()
    
    # Add a discount to each product for demonstration
    # In a real app, you would have a discount field in your Product model
    for product in products:
        # Simulate a random discount between 20% and 50%
        import random
        product.discount_percent = random.randint(20, 50)
        product.original_price = float(product.price) * (1 + product.discount_percent / 100)
        product.discount_amount = product.original_price - float(product.price)
    
    # Sort by discount percentage (highest first)
    products = sorted(products, key=lambda x: x.discount_percent, reverse=True)
    
    return render(request, 'product/extra-discounts.html', {
        'products': products,
        'title': 'Up to 50% Off - Limited Time Offer!',
        'subtitle': 'Hurry, these deals won\'t last long!',
    })

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        if CustomUser.objects.filter(username=phone).exists():
            return render(request, 'include/account/login.html', {'register_error': 'Phone already registered.', 'show_register': True})
        
        user = CustomUser.objects.create_user(
            username=phone, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name,
            gender=gender,
            phone=phone,
            country=country,
            city=city
        )
        # Log the user in automatically
        login(request, user)
        # Redirect to the new account page
        return redirect('account')
    return redirect('/')