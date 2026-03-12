while True:
 try:
  current = int(input("Current floor: "))
  break
 except(ValueError):
  print("That's not a number!")
while True:
 try:
  destination = int(input("Destination floor: "))         
  break
 except(ValueError):
  print("That's not a number!")
for i in range(destination - current + 1):
 print(f"Level {str(current + i)}")