numbers = [1, 5, 10, 15, 20]

largest_number = numbers[0]

for number in numbers:
  if number > largest_number:
    largest_number = number
print(largest_number)