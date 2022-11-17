import math

def Area(r):
  '''
  (int|float)---->int|float
  Takes the <r> radius from the user and calculates the area of a circle by using <r>
  '''
  return math.pi*r**2


def MyNameIs(greeting, name, n):
  '''
  (str,str,int)---> None
  Takes a <greeting> a <name> and the number of times the catchphrase will be multiplied <n> and
  returns a string combining them.
  '''
  print(greeting + ",")
  for i in range(n):
    print("My Name is,")
  print(name)

def Sum_Digits(n):
  '''
  (int)-->int
  Preconditions: <n> is a three-digit number and an integer
  Returns the sum of each digit of the number <n>
  '''
  if 100<=n and n<=999:
    a = n//100
    b = n%100
    c = b//10
    d = b%10
    return a+c+d
  else:
    print("Error! Please enter a three digit number")


def MidPoint(x1, y1, x2, y2):
  '''
  (int|float,int|float,int|float,int|float) ----> None
  Find the midpoint of two points (<x1>,<y1>) and (<x2,<y2>) in the xy axis and
  also the distance between them and return the midpoint and the distance
  '''
  midpoint = ((x1+x2)/2,(y1+y2)/2)
  distance = math.sqrt((y2-y1)**2+(x2-x1)**2)
  str(midpoint)
  str(distance)
  print("Midpoint : {} \nDistance : {}".format(midpoint,round(distance,2)))

def ascending(x, y, z) :
  '''
  (int|float|str,int|float|str,int|float|str)----> bool
  Figure out if the arguments entered <x>,<y>,<z> by the user are in ascending order return
  True if there is an ascending order, False if there is not an ascending order.
  '''
  if z >= y and y >= x :
    return True
  else:
    return False

def descending(x, y, z) :
  '''
  (int|float|str,int|float|str,int|float|str)----> bool
  Figure out if the arguments <x>,<y>,<z> are in a descending order return True if there is a descending order,
  False if there is not a descending order
  '''
  if x >= y and y >= z:
    return True
  else:
    return False


def duplicates(x, y, z):
  '''
  (int|float|str,int|float|str,int|float|str)----> bool
  Figure out if the arguments <x>,<y>,<z> are duplicates return True if the arguments are duplicates,
  False if they are not.
  '''
  if x == y and y == z and z == x:
    return True
  else:
    return False

def maythe4th(x, y):
  '''
  (int,int)--->bool
  Check if the given integers <x>,<y> are equal or their sum or difference are equal to 4 and
  return True if <x> and <y> are equal or their sum or difference is 4, False if not
  '''
  if x == y or x + y == 4 or abs(x-y) == 4:
    return True
  else:
    return False


def daysOfMonth():
  '''
  (str)--> str
  Shows the months in a year and asks the user to choose a month, then returns the number of days in that month.
  '''
  months = ["January, February, March, April, May, June, July, August, September, October, November, December"]
  thirty = ["april", "june", "september", "november"]
  thirty_one = ["january", "march", "may", "july", "august", "october", "december"]
  print("List of months:", months)

  x = input("Input the name of Month:")
  y = x.lower()
  z = y.replace(" ", "")
  for i in thirty:
    if z == i:
      return "No. of days: {} days".format(30)

  for i in thirty_one:
    if z == i:
      return "No. of days: {} days".format(31)

  if z == "february":
    year = int(input("Please enter the year:"))
    if year % 4 == 0:
      return "29"
    else:
      return "28"
  else:
    print("Please check your spelling")


def coordinates(s):
  '''
  (str)--->bool
  Check whether if a given string <s> denotes a coordinate of a point and
  return True if <s> denotes the coordinates of a point, False if <s> does not denote the coordinates of a point
  '''

  s.strip(" ")

  count_comma = 0
  count_decimal = 0
  count_dash = 0

  for i in s:
    if i == ",":
      count_comma += 1

  for i in s:
    if i == ".":
      count_decimal += 1

  for i in s:
    if i == "-":
      count_dash += 1

  if count_comma > 1 or count_comma == 0:
    return False

  if count_decimal > 2:
    return False

  if count_dash > 2:
    return False

  y = s.strip("-")
  z = y.replace(".", "")
  x = z.split(",")

  for i in x:
    if i.isnumeric():
      return True
    else:
      return False

def NumberOfBits(n):
  '''
  (int)--->int
  Preconditions : <n> is bigger or equal to 1
  Find the number of digits required to represent the entered number <n>
  in binary system and return the result.
  '''
  if n<1:
    print("Please enter a number equal or bigger than one")
  count = 0
  while n >= 2:
    n = n/2
    count += 1
  return count + 1

def vulnerability(play1, play2):
    '''
    (str,str)--->str
    Take elemental types <play1>,<play2> and determine vulnerability correlation.
    '''

    x = play1.lower()
    y = play2.lower()

    if x == y:
      return "no weakness found"
    elif x == "fire":
      if y == "water":
        return "Player 1 is vulnerable to Player 2"
      else:
        return "Player 2 is vulnerable to Player 1"
    elif x == "water":
      if y == "grass":
        return "Player 1 is vulnerable to Player 2"
      else:
        return "Player 2 is vulnerable to Player 1"
    elif x == "grass":
      if y == "fire":
        return "Player 1 is vulnerable to Player 2"
      else:
        return "Player 2 is vulnerable to Player 1"
    else:
      print("Please enter a valid move!")

