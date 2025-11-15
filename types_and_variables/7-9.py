import random

computer = random.randint(1,6)
you = int(input('Guess dice (1-6): '))
print(f'You won: {you == computer}')