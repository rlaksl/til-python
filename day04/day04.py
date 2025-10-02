from random import randint

# input
# input은 오직 하나의 argument만 받음

age = int(input("How old are you?"))

# And & or

if age < 18:
  print("You can't drink.")
elif age >= 18 and age <= 35:
  print("You drink beer")
elif age == 60 or age == 70:
  print("Birthday party")
else:
  print("Go ahead")

print("user answer", age)
print(type(age))

True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False

"""
user_choice = int(input("Choose number."))
pc_choice = randint(1,50) # imported this

if user_choice == pc_choice:
  print("You won")
elif user_choice > pc_choice:
  print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
  print("Higher! Computer chose", pc_choice)
"""

# While
distance = 0
while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1

print("Welcome to Python Casino")
pc_choice = randint(1,100)

playing =True

while playing:
  user_choice = int(input("Choose number(1~100): "))
  if user_choice == pc_choice:
    print("You won")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")

 