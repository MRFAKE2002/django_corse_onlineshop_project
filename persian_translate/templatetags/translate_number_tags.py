from django import template

register = template.Library()

# We use this template tag to translate english numbers to persian
@register.filter
def translate_persian_number(value):
    number = str(value)
    
    english_to_persian_number = number.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    
    return number.translate(english_to_persian_number)

