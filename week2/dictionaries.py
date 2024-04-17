# Understand dictionaries

my_dict = {"name": "John", "age": 25, "city": "Paris"}
print(my_dict)
print(my_dict["age"])
my_dict["email"] = "john@gmail.com"
print(my_dict)
my_dict["age"] = 35
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(f"{key}: {value}")

print(my_dict.get("job"))

other_dict = {"city": "Boston", "hobby": "photography"}
my_dict.update(other_dict)
print(my_dict)
