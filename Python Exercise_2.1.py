# Ask for an input integer
x = int(input('Enter an integer bigger than 1: '))

# Exhaustive Enumeration: Divide the input number by every integer smaller than x from 2
i = 2
prime_check = True

# Find the Smallest and the Largest Divisor of X
while i < x:
    if x <= 1:
        print ("Error : Number less or equal to 1")
        break
    elif x % i == 0:
        print("Smallest divisor:", i)
        print("Largest divisor:", int(x / i))
        prime_check = False
        break
    i += 1

if prime_check:
    print(x, "is prime")
else:
    print("Therefore", x, "is not prime")

# Function to check if a number is prime
def is_prime_number(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

# Adding all prime numbers between 2 and n
sum_of_primes = 0
prime_list = []
i = 2 #i is defined to 2 as the 2 is the first prime number

while i <= x:
    if is_prime_number(i) == True:
        sum_of_primes += i
        prime_list.append(i)
    i += 1

print("Sum of all prime numbers between 2 and", x, "is:", sum_of_primes)
print("List of all prime numbers between 2 and", x, "is:", prime_list)