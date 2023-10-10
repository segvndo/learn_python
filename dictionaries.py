# use dictionary to define key-value pair
# each key must be unique

customer = {
  "name": "John Smith",
  "age": 27,
  "is_verified": True
}

print(customer.get("name"))

# use .get() to assign a key value pair if it does not exist.
print(customer.get("birthdate", "Mar 15, 1996"))

# convert numbers to strings
phone = (input("Phone: "))
numbers = {
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine",
  "0": "Zero"
}

output = ""
for number in phone:
  output += numbers.get(number, "Not a valid input") + " "
print(output)
