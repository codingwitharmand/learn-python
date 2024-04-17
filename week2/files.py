# Understand files
import os

current_dir = os.getcwd()
print(current_dir)

with open('dummy.txt', 'w') as file:
    file.write('I love C++\n')
    file.write('I love Java\n')
    file.write('I love Javascript\n')

with open('dummy.txt', 'a') as file:
    file.write('I prefer Java')

with open('dummy.txt', 'r') as file:
    for line in file:
        print(line.strip())
