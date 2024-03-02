# Understand loops with factorial algorithm
print("Loops")

value = int(input("Enter value: "))
factorial = 1

for i in range(1, value + 1):
    factorial = factorial * i

print("Factorial is ", factorial)