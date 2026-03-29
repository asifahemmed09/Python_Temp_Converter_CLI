print("Welcome to Temperature Converter!")

type = input("Type 'C' to convert from Fahrenheit to Celsius, or 'F' to convert from Celsius to Fahrenheit: ")
temp = float(input("Enter the temperature you want to convert: "))

if type == 'C':
    converted = (temp * 9.0/5.0) + 32
    print(f"{temp} degrees Celsius is equal to {converted} degrees Fahrenheit.")
elif type == 'F':
    converted = (temp - 32) * 5.0/9.0
    print(f"{temp} degrees Fahrenheit is equal to {converted} degrees Celsius.")
else:
    print("Invalid input. Please enter 'C' or 'F'.")
