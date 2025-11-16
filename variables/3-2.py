###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

random_int = random.randint(1, 6)
print(f"Randomowa liczba to {random_int}")


random_uniform = random.uniform(1.0, 6.0)
print(f"Random float between 1.0 and 6.0: {random_uniform}")