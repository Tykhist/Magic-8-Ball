import random

'''
Eventually I would like to make this 
a function to be called and used in other 
programs, maybe a collection of randomizers?'''

name = input("Who are you?\n")
question = input("What would you like to know?\n")
answer = ""

random_number = random.randint(1, 12)

if name == "":
  name = "This person"
if question == "":
  question = "???"
  random_number = 0

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "What do you think?"
elif random_number == 11:
  answer = "Not in the good timeline."
elif random_number == 12:
  answer = "Only if you believe."
else:
  answer = "Error"

print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")
