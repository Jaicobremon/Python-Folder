import math

def greet (name):
    print("Hello " + name + ", how are you ?")

greet("Jaicob")

def squareroot():
    number = int(input("What is your number ?:"))
    sqr = math.sqrt(number)
    print(sqr)

def check():
    number2 = int(input("What is your number?:"))
    if (number2 % 2 == 0):
        print("The given number is even")
    else:
        print("Your number is not even")

def wordcount():
    filename = "Textfile.txt"
    numberofwords = 0
    file = open(filename,'r')
    for line in file:
        word = line.split()
        numberofwords += 1
    print(numberofwords)

#squareroot()
#check()
wordcount()
