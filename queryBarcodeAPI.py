response = requests.get("https://api.barcodelookup.com/v2/products?barcode=065633134423&key=<api_key>")
print(response.json())