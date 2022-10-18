from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from products.models import Product
from .cart import Cart
from .forms import ProductAddToCartForm

def cart_detail_view(request):
    """
    We use this function for make a cart_detail page  
    """
    cart = Cart(request)
    
    for item in cart:
        item['update_product_quantity_form'] = ProductAddToCartForm(initial={
            'quantity' : item['quantity'],
            'inplace' : True,
        })
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})


# We use this decorator because we need this function as POST request in product_detail
@require_POST
def product_add_to_cart_view(request, product_id):
    """
    We use this function for add the product to the cart by form in product_detail page 
    """
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    form = ProductAddToCartForm(request.POST)
    
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = int(cleaned_data['quantity'])
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])
    
    return redirect('cart:cart_detail')

# We use this function as GET request in cart_detail
def product_remove_from_cart_view(request, product_id):
    cart = Cart(request)
    """
    We use this function for remove the product from the cart by GET request in cart_detail page
    """
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)
    
    return redirect('cart:cart_detail')

def clear_cart(request):
    """
    We use this function to clear the cart by form in cart_detail page
    """
    cart = Cart(request)
    
    cart.clear()

    return redirect('cart:cart_detail')
