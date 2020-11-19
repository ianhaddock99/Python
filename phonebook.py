phonebook = {}

def printMenu():
    print("""
    Electronic Phone Book
    ++++++++++++++++++++
    1. Look up an entry
    2. Add an entry
    3. Remove a entry
    4. List all numbers
    5. Quit""")

menuChoice = 0
printMenu()

def lookupNum(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"

def addNum(numbers, name, number):
    numbers[name] = number

def removeNum(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," was not found")

def printNum(numbers):
    for k, v in numbers.items():
        print("Name:", k, "\nPhone Number:", v)
    print()

while True:
    menuChoice = int(input("Type in a number (1-5): "))
    if menuChoice == 1:
        print("Lookup Number")
        name = input("Name: ")
        print(lookupNum(phonebook, name))
        printMenu()
    elif menuChoice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        addNum(phonebook, name, phone)
        print("Entry stored for", name)
        printMenu()
    elif menuChoice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        removeNum(phonebook, name)
        printMenu()
    elif menuChoice == 4:
        printNum(phonebook)
        printMenu()
    elif menuChoice == 5:
        break
    else:
        printMenu()

print("Bye")



