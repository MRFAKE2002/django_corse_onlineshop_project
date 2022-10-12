from django.contrib import admin

from .models import Product, Comment


# We can use TabularInline or StackedInline in admin to display comments in product line 
class ProductCommentInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active',]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active',]
    
    inlines = [
        ProductCommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active',]

