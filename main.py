import random
from letters import letters
from symbols import symbols
from numbers import numbers

print("Random Password Generator\n")

run = True
while run:
  length = int(input("Preferred length of password (characters): "))

  let = input("Letters in your password? (Y/N): ").upper()
  sym = input("Symbols in your password? (Y/N): ").upper()
  num = input("Numbers in your password? (Y/N): ").upper()

  password = []
  if let == "Y" and sym == "Y" and num == "Y":
    for i in range(length):
      password.append(random.choice(letters))
      password.append(random.choice(symbols))
      password.append(random.choice(numbers))
  elif let == "Y" and sym == "Y" and num == "N":
    for i in range(length): 
      password.append(random.choice(letters))
      password.append(random.choice(symbols))
  elif let == "Y" and sym == "N" and num == "Y":
    for i in range(length):
      password.append(random.choice(letters))
      password.append(random.choice(numbers))
  elif let == "N" and sym == "Y" and num == "Y":
    for i in range(length):
      password.append(random.choice(symbols))
      password.append(random.choice(numbers))
  elif let == "N" and sym == "Y" and num == "N":
    for i in range(length): 
      password.append(random.choice(symbols))
  elif let == "N" and sym == "N" and num == "Y":
    for i in range(length): 
      password.append(random.choice(numbers))
  elif let == "Y" and sym == "N" and num == "N":
    for i in range(length):  
      password.append(random.choice(letters))
  else:
    password.append("You chose no for all options.")

  random.shuffle(password)

  display_password = ""

  for c in password[:length]:
    display_password += c

  print(f"\nPassword: {display_password}\n")

  again = input("Generate another password? (Y/N): ").upper()
  print()
  if again == "Y":
    continue
  else:
    print("Thanks for trying this out!")
    break
