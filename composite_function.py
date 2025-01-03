def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            return True
    return False
def print_composite_numbers(n):
    for i in range(4, n + 1):  # Composite numbers start from 4
        if is_composite(i):
            print(i)

# Request input from the user
n = int(input("Enter a number: "))

# Print composite numbers up to n
print_composite_numbers(n)
