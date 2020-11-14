# project solver: musshal

n = int(input())

for x in range(1, n, 2):
  if x % 3 == 0 and x % 5 == 0:
    print("Sololearn")
   elif x % 3 == 0:
    print("Solo")
   elif x % 5 == 0:
    print("Learn")
   else:
    print(x)
