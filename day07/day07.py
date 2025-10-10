# OOP (Object Oriented Programming, 객체지향프로그래밍)
# 데이터를 기반으로 동작하는 함수로 데이터를 캡슐화할 수 있음
"""
aksl = {
  "name": "rlaksl",
  "XP": 1000,
  "team": "Team X"
}

def intrduce_player(player):
  name = player["name"]
  team = player["team"]
  print(f"Hello! My name is {name} and I play for {team}")

intrduce_player(aksl)
"""
def create_player_for_team(name, xp, team):
  pass

def create_player(name, xp, team):
  return {
    "name": name,
    "XP": xp,
    "team": team,
  }

def intrduce_player(player):
  name = player["name"]
  team = player["team"]
  print(f"Hello! My name is {name} and I play for {team}")

aksl = create_player("rlaksl", 1500, "Team X")
lynn = create_player("Lynn", 1500, "Team Blue")

teams = {
  "Team X": [aksl],
  "Team Blue": [lynn]
}

# Classes
"""
class Puppy: 
  
  def __init__(potato):
    print(potato)
    print("Puppy is born!")

ruffus = Puppy()

print(ruffus)
"""

"""
class Puppy: 
  
  def __init__(self):
    self.name = "Ruffus"
    self.age = 0.1
    self.breed = "Beagle"

ruffus = Puppy()

print(
  ruffus.name,
  ruffus.age,
  ruffus.breed,
)

print(
  ruffus.name
)
"""
# Methods
# 메소드: 클래스 안에 있는 함수
"""
class Puppy: 
  
  def __init__(self, name, breed):
    self.name = name
    self.age = 0.1
    self.breed = breed

  def __str__(self):
    return f"Puppy named {self.name}, breed: {self.breed}."
  
  def __str__(self):
    return f"{self.breed} puppy named {self.name}."



ruffus = Puppy(
  name = "Ruffus", 
  breed = "Beagle",
)
bibi = Puppy(
  name = "Bibi",
  breed = "Dalmatian",
)

print(
  bibi.name,
  ruffus.name
)

print(
  bibi,
  ruffus,
)
"""

# Inheritance(상속)
class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzZzZZ...")

class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(
      name,
      breed,
      5,
    )
    self.aggressive = True
  
  def rrrr(self):
    print("으르렁")

class Puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(
      name,
      breed,
      0.1,
    )
    self.spoilde = True

  def woof_woof(self):
    print("멍멍")

ruffus = Puppy(
  name = "Ruffus", 
  breed = "Beagle",
)
bibi = GuardDog(
  name = "Bibi",
  breed = "Dalmatian",
)

ruffus.sleep()

bibi.sleep()
