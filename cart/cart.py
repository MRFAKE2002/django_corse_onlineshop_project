from django.contrib import messages
from django.utils.translation import gettext as _ # we use this function to translate our messages

from products.models import Product

class Cart:
    def __init__(self, request):
        """
        Initializes the Cart.
        """

        # We use this code to get the request that user come in Cart Pages  
        self.request = request   
        
        # We use this code to get the user's session
        self.session = request.session  
        
        # We use this code to get all data(products) that are in user's cart
        cart = self.session.get('cart')  
        
        # We use this code to make a empty cart for user
        if not cart:
            cart = self.session['cart'] = {} 
            # cart = self.session['cart']
            
        self.cart = cart
        
    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it already exists.
        """
        
        product_id = str(product.id)    
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0}
                
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        messages.success(self.request, _('Product successfully added to cart') )
        
        self.save()
        
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('Product successfully remove from cart') )
            self.save()
    
    def save(self):
        """
        Mark the session as being saved changes to the cart.
        """
        self.session.modified = True 
        
    def __iter__(self):
        """
        We overwrite this method to Iterable.
        """
        
        # We get all of the products that are in the cart
        product_ids = self.cart.keys()
        
        # We get all of the product's details by model from database that are in the cart
        products = Product.objects.filter(id__in=product_ids)
        
        # We use this code to make a copy from our cart's details to don't change the cart
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product_object'] = product
            
        for items in self.cart.values():
            items['total_price'] = items['quantity'] * items['product_object'].price
            yield items

    def __len__(self):
        """
        We use this method to get the number of products in the cart.
        We use this key method in header of site in _base.html
        """
        
        return sum(items['quantity'] for items in self.cart.values())
    
    def clear(self):
        """
        We need to clear the cart after finish the process.
        """
        
        del self.session['cart']
        
        self.save()
        
    def get_total_price(self):
        """
        We use this method to get the total product's price in the cart
        """

        # We get all of the products that are in the cart
        product_ids = self.cart.keys()

        # We use this code to get the total price of the product 
        return sum(items['quantity'] * items['product_object'].price for items in self.cart.values())

