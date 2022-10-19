from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


# We can use TabularInline or StackedInline in admin to display comments in product line 
class ProductCommentInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active',]
    
    inlines = [
        ProductCommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active',]

