from .produсts import amount_products, price

def total_price(product, amount):
    global total
    total = 0
    if product in amount_products.keys():
        if amount_products[product] < int(amount):
            print('There is no such amount!\n')
            return total
        else:
            if product in price.keys():
                total = float(amount) * price[product]
                amount_products[product] -= int(amount)
                return total

