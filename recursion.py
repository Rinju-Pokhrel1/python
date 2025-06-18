# Prints factorial of number n

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

# Example usage
print(fact(5))  # Output: 120
