from django import template

register = template.Library()

country_codes = {}
# @register.filter(name='get_postage_cost')
# def get_postage_cost(country,price):
#     # import address model and get the country
#     #match country with postage zone
#     #find the postage price for country and add it to devlivery
#     return price

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity