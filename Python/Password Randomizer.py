import random

#Character Shuffling
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

def createPassword():
    #Character Generating
    ucLetter1 = chr(random.randint(65,90))
    ucLetter2 = chr(random.randint(65,90))
    lcLetter1 = chr(random.randint(97,122))
    lcLetter2 = chr(random.randint(97,122))
    digit1 = chr(random.randint(48,57))
    digit2 = chr(random.randint(48,57))
    puncSign1 = chr(random.randint(33,47))
    puncSign2 = chr(random.randint(33,47))

    #Password Compiling and Shuffling
    password = ucLetter1 + ucLetter2 + lcLetter1 + lcLetter2 + digit1 + digit2 + puncSign1 + puncSign2
    password = shuffle(password)
    print(password)
    return password

tpassword = createPassword()
print("Is this a password you will use? Answer by typing yes or no.")
while True:
    answer = input()
    if answer == "yes":
        print("Retype password to confirm.")
        cPassword = input()
        while cPassword != tpassword:
            print("Sorry! Try typing the password again.")
            cPassword = input()
        print("Congratulations on your new password! Make sure to save this somewhere!")
        break
    elif answer == "no":
        print("Generating new password.")
        tpassword = createPassword()
        continue
    else:
        print("Did not answer with yes or no. Make sure to answer by typing \"yes\" or \"no\"")
        continue