# reading and writing file
f = open("caractacus.txt", "r")
text = f.read()
#print(text)

text = "hi guys" + text
print(text)


f1 = open("modified.txt", "w")
f1.write(text)
f1.close()

