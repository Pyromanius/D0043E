def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5) + 32)


def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * (5 / 9))

print("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ")

while True:
    choice = input()
    if choice not in ['C', 'F']:
        continue
    temp = float(input("Enter the temperature: "))
    if choice == 'C':
        # result = celsius_to_fahrenheit(temp)
        print(f"{temp:.1f}°C is {celsius_to_fahrenheit(temp):.2f}°F")
        break     
    else:
        # result = fahrenheit_to_celsius(temp)
        print(f"{temp:.1f}°F is {fahrenheit_to_celsius(temp):.2f}°C")
        break
    