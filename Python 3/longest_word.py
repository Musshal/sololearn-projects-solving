# problem solver: musshal

txt = input()

txtList = txt.split()
length = [len(i) for i in txtList]
maximum = max(length)
txtIndex = length.index(maximum)
print(txtList[txtIndex])
