while True:
 try:
  num_one = int(input("Number 1: "))
  break
 except(ValueError):
  print("That's not a number!")
while True:
 try:
  num_two = int(input("Number 2: "))
  break
 except(ValueError):
  print("That's not a number!")
print(f"{num_one} plus {num_two} is {num_one + num_two}")
print(f"{num_one} times {num_two} is {num_one * num_two}")