# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Read the value of N from the user
N = int(input("Enter the number of primes to find: "))

# List to store the first N primes
primes = []
number = 2  # Starting from the first prime number

# Loop until we find N primes
while len(primes) < N:
    if is_prime(number):
        primes.append(number)
    number += 1

# Print the prime numbers
print("Prime numbers:", ' '.join(map(str, primes)))
