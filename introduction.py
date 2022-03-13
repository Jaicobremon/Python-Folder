Name = 'Jaicob'
Grade = 9
Friends = ['friend1','friend2','friend3']


print(Friends[1])

print(Name)

Introstring = input("Enter your introduction: ")
print(Introstring)

charactercount = 0
wordcount = 1

for i in Introstring:
    charactercount = charactercount + 1
    if(i == ' '):
        wordcount = wordcount + 1

print(charactercount)
print(wordcount)

pocketmoney = int(input("What's your pocket money ?"))

print(pocketmoney)

if pocketmoney > 100:
    print("You have alot of pocket money !")

elif pocketmoney > 50:
    print("That's a good amount of pocket money !")

else:
    print("Ask your parents for more :)")

count = 5

while (count >= 0):
    print(count)
    count = count - 1


