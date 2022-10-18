from .cart import Cart

# We use this function to have access to the cart object in all templates and we must add it in settings TEMPLATES
def cart(request):
    return {'cart' : Cart(request) }
