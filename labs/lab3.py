def info_day(today, weather, temperature):
    str(temperature)
    s = "{} is a {} day. The temperature is {} degrees Celsius.".format(today,weather,temperature)
    print(s)

def letter_grade(grade):
  print("Your grade is",grade)

def average_of_two(x,y):

  x=float(input("Give me 1st number: "))
  y=float(input("give me 2nd number: "))

  average=(x+y)/2

  print("The average of", x, "and", y,"is", average)

def pay(wage,hour):

  if hour<=40:
    return wage * hour
  elif 40<hour<=60:
    return 40*wage + (hour-40)*1.5*wage
  elif 60<hour:
    return 40*wage + 20*1.5*wage+(hour-60)*2*wage

def rps(p1,p2):

  if p1 == p2:
    return 0

  elif p1 == "R":
    if p2 == "S":
      return -1
    else:
      return 1

  elif p1 == "S":
    if p2 == "P":
      return -1
    else:
      return 1

  elif p1 == "P":
    if p2 == "R":
      return -1
    else:
      return 1

def is_divisible(n,m):

  if n%m == 0:
    return True
  else:
    return False

def is_divisible23n8(x):

  if ((is_divisible(x,2)) or (is_divisible(x,3))) and (not is_divisible(x,8)):
    return "yes"
  else:
    return "no"
