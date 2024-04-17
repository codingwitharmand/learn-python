# String manipulation

greeting = "Hello"
name = "Armand"
message = greeting + ", " + name
print(message)

separator = "-" * 10
print(separator)

first_char = message[0]
print(first_char)

sub_message = message[0:5]
print(sub_message)

print(message.lower())

print(message.replace("Hello", "Bonjour"))

date = "02/05/2005"
tab = date.split("/")
print(tab)

print("/".join(tab))

