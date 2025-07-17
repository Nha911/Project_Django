from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, ProductImage, Wishlist, CartItem, CustomUser, Brand, Order, OrderItem

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender', 'phone_number', 'country', 'city')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount', 'category')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'about')
        }),
        ('Pricing and Category', {
            'fields': ('price', 'discount', 'category', 'brand')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Wishlist)
admin.site.register(CartItem)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(OrderItem)

