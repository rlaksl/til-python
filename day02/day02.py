# function
print(True)
print("hello")
print(12)
print(True, "hello", 12)

# def
def say_hello():
  print("hello how r u?")
  
say_hello()

#
def say_hello(user_name, user_age):
  print("hello", user_name)
  print("you are", user_age, "years old")

say_hello("hwanhui", 8)

# 마무리
def tax_calculator():
  print(1500000000 * 0.35)

tax_calculator()

# 
def tax_calculator(money):
  print(money * 0.35)

tax_calculator(250000)
tax_calculator(25000)
tax_calculator(2500)