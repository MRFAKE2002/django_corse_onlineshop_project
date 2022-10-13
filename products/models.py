from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ # we use this function to translate our verbose_name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
    

# We can make a custom manager here for set our queryset for models 
# In " Comment.objects " objects is manager and its work is get something from Comment model
# This custom manager give us all comments that they are active
# default manager " comments.objects.filter(active=True) "
class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)



class Comment(models.Model):
    PRODUCT_STAR = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Very Good'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Comment Text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STAR, blank=True, verbose_name=_('What is your score?'))
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
        
    active = models.BooleanField(default=True)
    
    # Manager
    # This is default code
    objects = models.Manager()
    # Now we can use this code " comments.active_comment_manager " instead of " comments.objects.filter(active=True) "
    active_comment_manager = ActiveCommentManager()
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

