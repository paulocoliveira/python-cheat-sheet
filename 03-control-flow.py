#Conditional Statement: Basic example if-else

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#Conditional Statement: Basic example if-elif

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#Loops: Basic for example

for number in range(1, 6):
    print(number)

#Loops: Basic while example

number = int(input("Enter a number: "))
factorial = 1
count = 1

while count <= number:
    factorial = factorial * count
    count += 1

print("The factorial of", number, "is", factorial)
