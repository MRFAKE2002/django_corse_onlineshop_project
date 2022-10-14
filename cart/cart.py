from products.models import Product

class Cart:
    def __init__(self, request):
        """
        Initializes the Cart.
        """

        self.request = request   # We use this code to get the request that user come in Cart Pages
        
        self.session = request.session  # We use this code to get the user's session
        
        cart = self.session.get('cart')  # We use this code to get all data(products) that are in user's cart
        
        if not cart:
            cart = self.session['cart'] = {} # We use this code to make a empty cart for user
            # cart = self.session['cart']
            
        self.cart = cart
        
    def add(self, product, quantity=1):
        """
        Add the specified product to the cart if it already exists.
        """
        
        product_id = str(product.id) 
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : quantity}
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
        
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
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
        
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product_object'] = product
            
        for items in self.cart.values():
            yield items

    def __len__(self):
        """
        We use this method to get the number of products in the cart.
        """
        
        return len(self.cart.keys())
    
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
        
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        return sum(product.price for product in products)

