price = int(input('price: '))
discount = int(input('discount %: ')) / 100


print(f'price: {price} discount: {discount*100}% discounted price: {price - price * discount} reduction: {price * discount}')