# project solver: musshal

import re

phoneNumber = r"^[189][0-9]{7}$"
inputPhoneNumber = input()
match = re.match(phoneNumber, inputPhoneNumber)

if match:
  print("Valid")
else:
  print("Invalid")
