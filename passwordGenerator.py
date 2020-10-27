import random


def passwordGenerator(length, num):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_?"
    password = ""
    listOfPassword = []
    for i in range(num):
        for i in range(length):
            password += random.choice(characters)
        listOfPassword.append(password)
        password = ""
    return listOfPassword


def listPrinter(list):
    for elt in list:
        print(elt)


def inputNum(statement):
  while True:
    try:
       userInput = int(input(statement))
    except ValueError:
       print("Hey, I only except numbers!")
       continue
    else:
       return userInput
       break


def main():
    print("Hello User! Welcome to the Password Generator.\nTierd of taking the time to think of a password? \nUse this program instead!")

    userNum = inputNum(
        "Give me the number of passwords that you want me to generate: ")

    userLength = inputNum("What's the length of the password? ")

    listOfPassword = passwordGenerator(int(userLength), int(userNum))
    return(listPrinter(listOfPassword))


if __name__ == '__main__':
  main()
