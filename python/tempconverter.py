#this program converts temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit

def main():
    temp = input("Enter a temperature: ")
    temp = float(temp)
    unit = input("Enter a unit of measurement, either C or F: ")
    if unit.lower() == "f":
        print(temp, "Fahrenheit is", (temp - 32) * 5 / 9, "Celsius")
    elif unit.lower() == "c":
        print(temp, "Celsius is", (temp * 9 / 5) + 32, "Fahrenheit")
    else:
        print("Invalid unit of measurement! Try again.")

main()