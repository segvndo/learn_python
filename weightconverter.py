# kg = input("enter your weight in kg: ")
# lbs = int(kg) * 2.2
# print(int(lbs))

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
  converted = int(weight) * 0.45
  print(f"You are {converted} kilos")
elif unit.upper() == "K":
  converted = int(weight) // 0.45
  print(f"You are {converted} pounds")