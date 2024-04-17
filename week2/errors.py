try:
    number = int(input("Enter a number: "))
    result = number / 0
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print("No exceptions")
finally:
    print("Execute no matter what")

if number < 0:
    raise ValueError("The number can not be negative")