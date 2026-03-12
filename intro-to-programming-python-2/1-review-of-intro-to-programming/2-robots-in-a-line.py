line = input("Line: ")
words = line.split()
lowwords = []
for word in words:
 lowwords.append(word.lower())
if "robot" in words:
 print("There is a small robot in the line.")
elif "ROBOT" in words:
 print("There is a big robot in the line.")
elif "robot" in lowwords:
 print("There is a medium sized robot in the line.")
else:
 print("No robots here.")