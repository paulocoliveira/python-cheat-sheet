# Type Conversion Functions

# Converting a string to an integer

age_str = "25"
age_int = int(age_str)
print(age_int)  # Output: 25

# Converting a float to an integer

price_float = 9.99
price_int = int(price_float)
print(price_int)  # Output: 9

# Converting a string to a float:

price_str = "9.99"
price_float = float(price_str)
print(price_float)  # Output: 9.99

# Converting an integer to a string:

quantity_int = 10
quantity_str = str(quantity_int)
print(quantity_str)  # Output: "10"

# Converting a string to an integer using a specific base

binary_str = "101010"
decimal_num = int(binary_str, 2)
print(decimal_num)  # Output: 42