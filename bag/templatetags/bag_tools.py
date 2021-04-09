from django import template

reqister = template.Library()

country_codes = {}
def get_postage_cost(country,price):
    # import address model and get the country
    #match country with postage zone
    #find the postage price for country and add it to devlivery
    return price