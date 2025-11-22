import random

def rand_elem(array):
    return random.choice(array)

array = [10, 20, 30, 40, 50, 60, 70]

for _ in range(5):
    print(rand_elem(array))
