from django.views import generic
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _ # we use this function to translate our CommentCreateView
from django.contrib import messages 


from .models import Product, Comment
from .forms import CommentForm
# from cart.forms import ProductAddToCartForm


class ProductListView(generic.ListView):
    # model = Product
    # We use queryset for add or change something that are in our databases in our code
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'    


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    # For show our CommentForm in product_detail in class we must overwrite a method to send our comment_form as a context
    # We use get_context_data for add or change anything in our code 
    # This method in django by default just get Product and comment from our model
    def get_context_data(self, **kwargs):
        # This code is default in django for get Product and Comment form model
        context = super().get_context_data(**kwargs)
        # We use this code to add CommentForm in the context and use it in our product_detail
        context['comment_form'] = CommentForm()
        # # We use this code to add ProductAddToCartForm in the context and use it in our product_detail        
        # context['cart_form'] = ProductAddToCartForm()
        return context


# After we send our CommentForm in product_detail now we want to let user to send his comment for our product
class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    
    # Now for add user comment in database we must overwrite a method
    def form_valid(self, form):
        # get the comment body and stars from user request by CommentForm but we don't want to save it in database
        user_comment = form.save(commit=False)
        # get the comment user from the user that login
        user_comment.author = self.request.user
        
        # For get the comment product we must get the product id from the url that we POST the " product.id " by comment that user send it
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        user_comment.product = product
        
        messages.success(self.request, _('comment created successfully.' ))         
        
        return super().form_valid(form)
    
