# .insert() takes two parameters: the index of where the new value is going to be and the new value itself
numbers = [5, 3, 7, 4, 2]
numbers.insert(0, 5)
print(numbers)

# .remove() takes one parameter and takes out the item you want to remove
numbers.remove(7)
print(numbers)


# .pop() removes the LAST ITEM in the list
numbers.pop()
print(numbers)

# .clear() doesn't take any values, but clears the list when called
numbers.clear()
print(numbers)

# .index() checks the existence of a value in a list
numbers = [5, 3, 7, 4, 2]
  # print(numbers.index(10))
# Results in error because 10 is not in numbers
# Can also check via boolean expression:

print(50 in numbers)
#Outcome of False

# .count() takes the value of the item that you want to count the occurrence of
numbers = [5, 5, 5, 3, 7, 4, 2]
print(numbers.count(5))

# .sort() takes no value, sorts the list in ascending order
# .reverse() takes no value, sorts the list in descending order(call .sort() before .reverse())
numbers = [5, 3, 7, 4, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers = [5, 3, 7, 4, 2]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)


print("Exercise")
# Remove duplicates in a list
letters = ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'f']
unique_letters = []

for letter in letters:
    if letter not in unique_letters:
        unique_letters.append(letter)
print(unique_letters)
# returns ['a', 'b', 'c', 'd', 'e', 'f']

for letter in letters:
    if letter not in unique_letters:
        unique_letters.append(letter)
        print(unique_letters)
# returns : 
# 'a']
# ['a', 'b']
# ['a', 'b', 'c']
# ['a', 'b', 'c', 'd']
# ['a', 'b', 'c', 'd', 'e']
# ['a', 'b', 'c', 'd', 'e', 'f']