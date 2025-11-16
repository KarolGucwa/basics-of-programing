def f(amount_to_pay):
    coins = [5, 2, 1]
    num_coins = 0
    for coin in coins:
        num_coins += amount_to_pay // coin 
        amount_to_pay %= coin
    return num_coins
