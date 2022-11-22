import math

class Point:
    'class that represents a point in the plane'

## executing Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE THE OBJECT

## Variables INSIDE an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def distance(self, p):
        'returns distance to point p'
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def up(self):
        'move up 1 unit'
        self.move(0, 1)

    def down(self):
        'move down 1 unit'
        self.move(0, -1)

    def left(self):
        'move left 1 unit'
        self.move(-1, 0)

    def right(self):
        'move right 1 unit'
        self.move(1, 0)


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age='0'):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec, 'and I', self.lang)

    def getAge(self):
        'get animal age'
        return self.age

class Card():
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit


### Complete the following ###
    def __lt__(self, other):
        'self < other if rank of self < rank of other'
        return self.rank < other.rank

    def __gt__(self, other):
        'self > other if rank of self > rank of other'
        return self.rank > other.rank

    def __le__(self, other):
        'self <= other if rank of self <= rank of other'
        return self.rank <= other.rank

    def __ge__(self, other):
        'self >= other if rank of self >= rank of other'
        return self.rank >= other.rank

class BankAccount():
    'a bank account class'

    def __init__(self, initial=0):
        'constructor'
        self.bal = initial

    def withdraw(self, amount):
        'withdraws amount'
        self.bal = self.bal - amount

    def deposit(self,amount):
        'deposits amount'
        self.bal = self.bal + amount

    def balance(self):
        'returns balance'
        return self.bal

    def __repr__(self):
        return 'BankAccount('+str(self.bal)+')'

class PingPong():
    def __init__(self):
        self.state='PING'

    def next(self):
        print(self.state)
        if self.state=='PING':
            self.state='PONG'
        else:
            self.state='PING'



class Bird(Animal):  # class Bird inherits all attributes (data and method) from class Animal
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)

class Vector(Point):
    'a 2D vector class'

    def __mul__(self, v):
        'vector product'
        return self.x * v.x + self.y * v.y

    def __add__(self, v):
        'vector addition'
        return Vector(self.x + v.x, self.y + v.y)

    def __repr__(self):
        'returns the canonical string representation'
        return 'Vector{}'.format(self.get())


def m(i):
    '''(int)->number
    returns the sum 1/3+2/5+3/7+...+i/(2i+1)
    Precondition: i>=1
    '''
    if i == 1:
        return 1 / 3
    else:
        return i / (2 * i + 1) + m(i - 1)


def count_digits(n):
    '''(int)->int
    Returns the number of digits in n
    Precondition: n a non-negative integer
    '''

    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


def is_palindrome(s):
    '''(str)->bool
    Returns True if string s forms a palindrome and False otherwise
    '''
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

def gcd(a, b):
    '''(int,int)->int
    Returns the greatest common divisor of a and b
    Precondition: a and b are both positive integers
    '''  
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
