import Shop.sklep.produсts
from Shop.sklep.order import total_price

def run_shop():
    total = 0
    while True:
        product = input("What product do you need? Finish: 'X'\n")
        if product == 'X':
            print('Thanks for shopping =)')
            break

        if product not in Shop.sklep.produсts.amount_products:
            print('Product is out of stock!')
            continue

        amount = input(f'How much {product} do you need?\n')

        total += total_price(product, amount)
    print(f'Total price: {total:.2f} PLN\n')


if __name__ == '__main__':
    run_shop()

