from random import choice

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 12

######### TUNED GENERATOR #######

chars = (DIGITS + LOWERCASE_LETTERS + UPPERCASE_LETTERS + PUNCTUATION)


def expel_mix_symbols(string):
    for i in "il1Lo0O":
        string = string[:string.index(i)] + string[(string.index(i)) + 1:]
    return string


chars = expel_mix_symbols(chars)


############ MAIN CODE ##########


def force_valid():
    print("\n" + "Yes = 1 , No = 0")
    inpt = input()
    if inpt == "1":
        return True
    elif inpt == "0":
        return False
    else:
        force_valid()


def force_valid2(Min=1, Max=10):
    while True:
        print("\n" + "Type number from", Min, "to", Max)
        inpt = input()
        if inpt.isdigit():
            if Min <= int(inpt) <= Max:
                return int(inpt)


def initializtion():
    while True:
      string = ""
      print("\n" + "Will your password contain numbers?" + "\n")
      if force_valid():
          string += DIGITS
      print("Will your password contain lowercase letters?" + "\n")
      if force_valid():
          string += LOWERCASE_LETTERS
      print("Will your password contain uppercase letters?" + "\n")
      if force_valid():
          string += UPPERCASE_LETTERS
      print("Will your password contain punctuations(!#$%)?" + "\n")
      if force_valid():
          string += PUNCTUATION
      if len(string) == 0:
          print("No, you cant make password out of no symbols!!!" + "\n")
          continue
      else:
        print("Will your password expel mix symbols(il1Lo0O)?" + "\n")
        if force_valid():
            string = expel_mix_symbols(string)
        return string


def generate_password(length, symbols):
    result = ""
    for j in range(length):
        result += choice(symbols)
    print("\n" + result)


######### PROGRAM RUN #############

print("Welcome to safe password generating programm")
while True:
    print("\n" + "All safe parameters are ON, would you like to change it?")
    if force_valid():
        chars = initializtion()
    print("\n" + "Please type how many passwords you need?")
    for i in range(force_valid2()):
        print("\n" + "Please type length of the password ?")
        generate_password(force_valid2(PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH), chars)
    print("\n" + "Do you want more passwords to be generated?")
    if force_valid():
        continue
    else:
        print("\n" + "Then I am off!!!")
        break