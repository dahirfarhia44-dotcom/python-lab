from utils import square, is_even, celsius_to_fahrenheit, greet
number = float(input("Enter a number: "))
name = input("Enter your name: ")

square_result = square(number)
even_result = is_even(number)
fahrenheit_result = celsius_to_fahrenheit(number)

print("square:", square_result)
if even_result:
    print("The number is even.")
else:
    print("The number is odd.")

print(greet(name))
print("Fahrenheit:", fahrenheit_result)

