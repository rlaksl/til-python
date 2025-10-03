# Methods

name = "hwanhui"

print(name.upper()) # 전부 대문자
print(name.capitalize()) # 앞 글자만 대문자로
print(name.startswith("n")) # False

mon = "Mon"
tue = "Tue"
wed = "Wed"

# List
# days_of_week = "Mon,Tue,Wed,Thu,Fri"
days_of_week = ["Mon","Tue","Wed","Thur","Fri"]
print(days_of_week)
days_of_week.append("Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)
days_of_week.remove("Fri")
print(days_of_week)

#Tupls
days = ("Mon", "Thu", "Wed")

print(days[0])

#Dicts
player = {
  'name': 'hwanhui',
  'age': 12,
  'alive': True,
  'fav_food':["🍟","🍤"]
}
print(player)
print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
