# SMALL ------------------------------------------------------------

#1. Hello You!
#name = input("What is your name?")
#print("Hello " + name + "!")

#2. HELLO YOU!
#name = input("What is your name?")
#print("Hello " + name.upper() + "!")
#print("Your name has", len(name), "letters in it!")

#3. Madlib
#print("Fill in the blanks below:\n(Name) ran towards the (Animal).")
#name = input("What is the name?")
#animal = input("What is the animal?")
#print("%s ran towards the %s." % (name, animal))

#4. Day of the Week
#day = int(input('Day (0-6)? '))
#if day == 0:
    #print("Sunday")
#elif day == 1:
    #print("Monday")
#elif day == 2:
    #print("Tuesday")
#elif day == 3:
    #print("Wednesday")
#elif day == 4:
    #print("Thursday")
#elif day == 5:
    #print("Friday")
#elif day == 6:
    #print("Saturday")
#else:
    #print("Not a valid number")



#5 Work or Sleep In
#day = int(input('Day (0-6)? '))
#if day == 0:
    #print("Sleep in")
#elif day == 1:
    #print("Go to work")
#elif day == 2:
    #print("Go to work")
#elif day == 3:
    #print("Go to work")
#elif day == 4:
    #print("Go to work")
#elif day == 5:
    #print("Go to work")
#elif day == 6:
    #print("Sleep in")
#else:
    #print("You did not enter a number between 0 and 6")


#6 Celsius to Fahrenheit
#celsius = int(input('Temperature in C? '))
#fahrenheit = (celsius * 9/5) + 32
#print(fahrenheit)

#7 Looping from 1 to 10
# count = 0
# while(count < 10):
#     count += 1
#     print(count)

#8 n to m
# start = int(input("Start from: "))
# end = int(input("End at: "))
# for x in range(start, end + 1):
#     print(x)




#MEDIUM -----------------------------------------------------------------------------
#1 Tip Calculator

# bill = float(input("Total bill amount: "))
# level_service = input("Level of service? ")
# good = bill * .20
# good_total = bill + good
# fair = bill * .15
# fair_total = bill + fair
# bad = bill * .10
# bad_total = bill + bad
# if level_service == "good":
#     print("Tip amount: $%.2f" % good)
#     print("Total amount $%.2f" % good_total)
# elif level_service == "fair":
#     print("Tip amount: $%.2f" % fair)
#     print("Total amount $%.2f" % fair_total)
# elif level_service == "bad":
#     print("Tip amount: $%.2f" % bad)
#     print("Total amount $%.2f" % bad_total)

#2 Advanced Tip Calculator

# bill = float(input("Total bill amount: "))
# level_service = input("Level of service? ")
# split1 = int(input("Split how many ways? "))
# good = bill * .20
# good_total = bill + good
# good_per_p = good_total/split1
# fair = bill * .15
# fair_total = bill + fair
# fair_per_p = fair_total/split1
# bad = bill * .10
# bad_total = bill + bad
# bad_per_p = bad_total/split1
# if level_service == "good":
#     print("Tip amount: $%.2f" % good)
#     print("Total amount $%.2f" % good_total)
#     print("Amount per person $%.2f" % good_per_p)
# elif level_service == "fair":
#     print("Tip amount: $%.2f" % fair)
#     print("Total amount $%.2f" % fair_total)
#     print("Amount per person $%.2f" % fair_per_p)
# elif level_service == "bad":
#     print("Tip amount: $%.2f" % bad)
#     print("Total amount $%.2f" % bad_total)
#     print("Amount per person $%.2f" % bad_per_p)


#3 How many coins?

# number = 0
# print(f"You have {number} coins.")
# while (True):
#     yesorno = input("Do you want another, yes or no?").lower()
#     if yesorno == "yes":
#         number += 1
#         print(f"You have {number} coins.")
#     elif (yesorno == "no"):
#         break
#     else:
#         print("Invalid Input")
# print("Bye")

#4 Print a Box
# row = int(input("Enter row:"))
# col = int(input("Enter col:"))
# for i in range(row):
#     for j in range(col):
#         if i == 0 or i ==(row-1) or j == 0 or j ==(col-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    



#5 Print a Triangle
# j = 9 #spaces
# for i in range(1,8,2):  #1 star up to 8 increment by 2
#     print(" "*j+i*"*")
#     j=j-1 #subtract 1 space from each row

#6 MULTIPLICATION TABLES
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

#THURSDAY HOMEWORK SMALL ---------------------------------------------------------------

#1 SUM THE NUMBERS

# x = [1,2,3,4]
# print(sum(x))

#2 LARGEST NUMBER

# x = [1,2,3,4,5]

# print(max(x))

#3 SMALLEST NUMBER

# x = [1,2,3,4,5]

# print(min(x))

#4 EVEN NUMBERS

# oldnum = [1,2,3,4,5]

# for i in oldnum:
#     if i % 2 == 0: #Divides number in list by 2, if remainder is 0, it is even number
#         print(i)

#5 POSITIVE NUMBERS

# xs = [-3,-2,-1,0,1,2,3]
# for i in xs:
#     if i >= 0:
#         print(i)

#6 POSITIVE NUMBERS 2

# px = [-3,-2,-1,0,1,2,3]
# px1 = []

# for i in px:
#     if i >= 0:
#         px1.append(i)
# print(px1)

#7 MULTIPLY LIST BY SINGLE FACTOR

# list1 = [1,2,3,4]
# list2 = 2
# list3 = []

# for i in list1:
#     list3.append(i*list2)
# print(list3)

#8 REVERSE A STRING

# txt = "Hello World" [::-1] #Slice, start at end of string and end at beginning which is 0 place.
# print(txt)



#THURSDAY HOMEWORK MEDIUM -----------------------------------------------------

#1 Multiply Vectors

# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# c=[]

# for i in range(0, len(list1)):
#     c.append(list1[i]*list2[i])
# print(c)

#2 Matrix Addition

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]


# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j]=(X[i][j] + Y[i][j])

# for r in result:
#     print(r)


#4 Remove duplicates from list
# oldlist = [1,1,2,2,3,4,4,5,5]
# newlist = []

# for i in oldlist:  
#     if i not in newlist: # if any elements not in oldlist add them
#         newlist.append(i) 
# print(newlist)

#5 Leet speak translator
# string = input('Enter some text: ').upper()

# for char in string:
# 	if char == 'A':
# 		string = string.replace('A','4')
# 	elif char == 'G':
# 		string = string.replace('G','6')
# 	elif char == 'E':
# 		string = string.replace('E','3')
# 	elif char == 'I':
# 		string = string.replace('I','1')
# 	elif char == 'O':
# 		string = string.replace('O','0')
# 	elif char == 'S': 
# 		string = string.replace('S','5')
# 	elif char == 'T':
# 		string = string.replace('T','7')
# 	else:
# 		pass

# print(string)

#6 Long-long vowels

# letter = input("Enter a word")

# letter = letter.replace('aa', 'aaaaa')
# letter = letter.replace('ee', 'eeeee')
# letter = letter.replace('ii', 'iiiii')
# letter = letter.replace('oo', 'ooooo')
# letter = letter.replace('uu', 'uuuuu')

# print(letter)

# SMALL FRIDAY ------------------------------------------------------------------

#1 MADLIB FUNCTION

# def madlib(name, subject):

#     print(f"{name} likes to study {subject}")

# madlib("Ian", "history")

#2 FAHRENHEIT TO CELSIUS CONVERSION

# def celsius(f):

#     return (f - 32) * .5556 #returns value of celsius

# f = int(float(input("Enter a temp in fahrenheit: ")) #input of temp in farhen
# print(celsius(f)) #call of celsius

#3 CELSIUS TO FAHRENHEIT

# def farhenheit(c):

#     return (c*9/5) + 32 #returns value of farhenheit

# c = int(float(input("Enter a temp in celsius: "))) #input of temp in celsius
# print(farhenheit(c))

#4 IS EVEN FUNCTION

# def is_even():
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# x = int(input("Enter a number: "))
# print(is_even())

#5 IS ODD FUNCTION

# def is_even():
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# def is_odd():
#     if not is_even():
#         return True
#     else:
#         return False

# x =int(input("Enter a number"))
# print(is_odd())

#6 ONLY EVENS LISTS #NOT USING OTHER FUNCTION

# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# def only_evens(list1):
#     evens = []
#     for x in list1:
#         if is_even(x) != 0:
#             evens.append(x)
#     return evens

# list1 = [11, 20, 42, 97, 23, 10]
# print(only_evens(list1))

#7 ONLY ODDS LIST

# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# def is_odd(x):
#     if not is_even(x):
#         return True
#     else:
#         return False

# def only_evens(list1):
#     evens = []
#     for x in list1:
#         if is_even(x) == 0:
#             evens.append(x)
#     return evens

# list1 = [11, 20, 42, 97, 23, 10]
# print(only_evens(list1))

# x =int(input("Enter a number"))
# print(is_odd())


# MEDIUM 

#1 FIND THE SMALLEST NUMBER

# def smallest(x):
#     x.sort()
#     print(x[:1])
# smallest([15,3,21,34,22,6])

# def smallest(list1):
#     small = list1[0]
#     for x in list1:
#         if x <= small:
#             small = x
#     return small

# print(smallest([4,3,2,7,5]))

#2 FIND THE LARGEST NUMBER

# def largest(x):
#     x.sort()
#     print(x[-1])
# largest([15,3,21,34,22,6])

# def largest(list1):
#     large = list1[0]
#     for i in list1:
#         if i > large:
#             large = i
#     return large

# print(largest([4,3,2,7,5]))


#3 FIND THE SHORTEST STRING

# def shortest(x):
#     print(min(x))
# shortest(["abc","abcd","abcde","abcdef"])

#4 FIND THE LONGEST STRING

# def longest(x):
#     print(max(x))
# longest(["abc","abcd","abcde","abcdef"])

# PHONEBOOK ==========================================================

# phonebook = {}

# def printMenu():
#     print("""
#     Electronic Phone Book
#     ++++++++++++++++++++
#     1. Look up an entry
#     2. Add an entry
#     3. Remove a entry
#     4. List all numbers
#     5. Quit""")

# menuChoice = 0
# printMenu()

# def lookupNum(numbers, name):
#     if name in numbers:
#         return "The number is " + numbers[name]
#     else:
#         return name + " was not found"

# def addNum(numbers, name, number):
#     numbers[name] = number

# def removeNum(numbers, name):
#     if name in numbers:
#         del numbers[name]
#     else:
#         print(name," was not found")

# def printNum(numbers):
#     for k, v in numbers.items():
#         print("Name:", k, "\nPhone Number:", v)
#     print()

# while True:
#     menuChoice = int(input("Type in a number (1-5): "))
#     if menuChoice == 1:
#         print("Lookup entry")
#         name = input("Name: ")
#         print(lookupNum(phonebook, name))
#         printMenu()
#     elif menuChoice == 2:
#         print("Add Name and Number")
#         name = input("Name: ")
#         phone = input("Number: ")
#         addNum(phonebook, name, phone)
#         print("Entry stored for", name)
#         printMenu()
#     elif menuChoice == 3:
#         print("Remove entry")
#         name = input("Name: ")
#         removeNum(phonebook, name)
#         printMenu()
#     elif menuChoice == 4:
#         printNum(phonebook)
#         printMenu()
#     elif menuChoice == 5:
#         break
#     else:
#         printMenu()

# print("Bye")









