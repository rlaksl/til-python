# 파라미터에 기본값 지정
def say_hello(user_name="홍길동"):
  print("Hello", user_name)

say_hello("nico")
say_hello()

# 덧셈
def plus(a=0,b=0):
  print(a+b)

plus(12,1)
plus()

# 뺄셈
def minus(a=0,b=0):
  print(a-b)

minus(1,2)
minus()

# 곱셈
def multiple(a=0,b=0):
  print(a*b)

multiple(3,4)
multiple()

# 나눗셈
def divide(a=0,b=1):
  print(a/b)

divide(12,6)
divide()

# 제곱
def powerof(a=2,b=0):
  print(a**b)

powerof(2,10)
powerof()

# return
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

to_pay = tax_calc(15000000)
pay_tax(to_pay)

# format
my_name = "hwanhui"
my_age = 8
my_color_eyes = "black"

print(f"Hello I'm {my_name}, I have {my_age} years in the Korea, {my_color_eyes} is my eye color")

def make_juice(fruit):
  return f"{fruit}+🍹"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍭"

juice = make_juice("🍏")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)

# if
if 10 > 5:
  print("Corrrect!")

a = "hwanhui"
if a == "hwanhui":
  print("True!")

# Else
password_correct = False

if password_correct:
  print("Here is your money")
else:
  print("Wrong password")

# Elif
winner = 6

if winner >10:
  print("Winner is greater than 10")
elif winner < 10:
  print("Winner is less than 10")
else:
  print("Winner is 10")