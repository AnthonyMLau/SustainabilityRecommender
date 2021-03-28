#this file will calculate the carbon offset required to ...

import json

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def get_item_weight(barcode):
    item_dict = json.loads(barcode)
    item_dict = item_dict['products'][0]
    if item_dict['weight']:
        weight = item_dict['weight']
    else:
        weight = item_dict['description']

    weight = ''.join([num for num in weight if is_integer(num)])
    return int(weight)

if __name__ == "__main__":
    barcode_test = '''{"products": [{"barcode_number": "4005924706256", "barcode_type": "EAN", "barcode_formats": "EAN 4005924706256", "mpn": "", "model": "", "asin": "", "product_name": "Plochman's Greek Style Seasoning", "title": "", "category": "Food, Beverages & Tobacco > Food Items > Seasonings & Spices > Herbs & Spices", "manufacturer": "", "brand": "Plochman's", "label": "", "author": "", "publisher": "", "artist": "", "actor": "", "director": "", "studio": "", "genre": "", "audience_rating": "", "ingredients": "", "nutrition_facts": "", "color": "", "format": "", "package_quantity": "", "size": "", "length": "", "width": "", "height": "", "weight": "", "release_date": "", "description": "Volume/Quantity - 85g.", "features": [], "images": ["https://images.barcodelookup.com/9665/96659398-1.jpg"], "stores": [{"store_name": "Walmart Canada", "store_price": "3.97", "product_url": "http://www.walmart.ca/en/ip/plochmans-greek-style-seasoning/6000198006065", "currency_code": "CAD", "currency_symbol": "$"}], "reviews": []}]}'''
    print(get_item_weight(barcode_test))