file = open("/usercode/files/books.txt", "r")

bookName = file.readlines()
length = len(bookName)

for i in range(length):
  firstLetter = bookName[i][0]
  lengthLetter = len(bookName[i])
  if (i == (length-1)):
    print(firstLetter + str(lengthLetter))
  else:
    print(firstLetter + str(lengthLetter-1))
    
file.close()
