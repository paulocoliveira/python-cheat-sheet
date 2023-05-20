#Conditional Statement: Basic example if-else

selenium_version = float(input("Enter your selenium version: "))


if selenium_version >= 4:
    print("Your selenium version is updated.")
else:
    print("Your selenium version is deprecated.")

#Conditional Statement: Basic example if-elif

selenium_version = float(input("Enter your selenium version: "))

if selenium_version == 4.9:
    print("Your selenium version is the latest.")
elif selenium_version >= 4:
    print("Your selenium version is updated.")
else:
    print("Your selenium version is deprecated.")

#Loops: For basic example
for number in range(1, 6):
    print(number)

#Loops: While factorial example

number = int(input("Enter a number: "))
factorial = 1
count = 1

while count <= number:
    factorial = factorial * count
    count += 1

print("The factorial of", number, "is", factorial)