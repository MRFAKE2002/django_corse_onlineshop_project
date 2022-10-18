from django import forms

class ProductAddToCartForm(forms.Form):
    QUANTITY_CHOICES = ((i, str(i)) for i in range(1, 30))

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)    

    # We use this field in our form because we can overwrite product quantity in cart_detail
    # We use widget in our field to don't show this field to user
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput) 
    