import math

while True:
    try:
        decimal_limit = int(input("Enter a number (max 15): "))
        if 0 <= decimal_limit <= 15:
            break
        else:
            print("Please enter a number between 0 and 15.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

pi = math.pi
str_pi = str(pi)
truncated_pi = str_pi[:decimal_limit+2]
print(truncated_pi)


# Alternate solution
# print(f"π to {decimal_limit} decimal places: {pi:.{decimal_limit}f}")
