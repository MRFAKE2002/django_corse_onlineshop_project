from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _ # we use this function to translate our verbose_name

from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart

@login_required
def order_create(request):
    order_form = OrderForm()
    cart = Cart(request)
    
    if len(cart)==0:
        messages.warning(request, _("You can not proceed to checkout page because you cart is empty"))
        return redirect('product_list')
        
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
    
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            
            for item in cart:

                OrderItem.objects.create(
                    order = order_obj,
                    product = item["product_object"],
                    quantity=item['quantity'],
                    price=item["product_object"].price,
                )
            
            cart.clear()
            
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            
            messages.success(request, _("Your order has successfully placed"))

        
    
    return render(request, 'orders/order_create.html', context={
        'order_form' : OrderForm(),
    })