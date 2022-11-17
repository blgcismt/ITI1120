def is_eligible(age, citizenship, prison):
    '''(int, str, str)->bool
    Returns true if a person is eligible to vote, and false otherwise
    '''
    a = citizenship.replace(" ", "")
    b = prison.replace(" ", "")
    x = a.lower()
    y = b.lower()
    if (age >= 18) and (x == "canada" or "canadian") and (y == "no"):
        return True
    else:
        return False


def mess(phrase):
    '''(str)->str
    Returns a copy of the given phrase where
    each character that is one of the last  8 consonants
    of English alphabet is capitalized
    and where each space is replaced by a dash.
    '''

    last8 = ['r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    newPhrase = ""

    for char in phrase:
        if char == " ":
            newPhrase += "-"

        elif char in last8:
            newPhrase += char.upper()

        else:
            newPhrase += char

    return newPhrase


def is_divisible(n, m):
    '''(int, int)->bool
    returns True if n is divisible by n, and False otherwise.'''
    return n % m == 0


def is_divisible23n8(n):
    '''(int)->bool
    returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
    if ((is_divisible(n, 2) or is_divisible(n, 3)) and not (is_divisible(n, 8))):
        return True
    else:
        return False

def print_all_23n8(num):
  divisible = []
  for i in range(1,num):
    if is_divisible23n8(i):
      divisible.append(i)
  print(divisible)

def draw():
    rows = int(input("Enter a positive integer: "))
    char = input("Enter a character: ")
    for i in range(1, rows + 1):
        print(char * i)


def draw2():
    rows = int(input("Enter number of rows: "))

    k = 0

    for i in range(1, rows + 1):
        for space in range(1, (rows - i) + 1):
            print(end="  ")

        while k != (2 * i - 1):
            print("# ", end="")
            k += 1

        k = 0
        print()


def prime(n):
    '''(int)->bool
    returns True if n is a prime, and False otherwise
    Precondition: n is a positive integer'''
    if n == 1:
        return False

    elif n == 2:
        return True

    else:
        for i in range(2, n):
            if n % i == 0:
                return False

    return True


def prime_v2(n):
    '''(int)->bool
    returns True if n is a prime, and False otherwise
    Precondition: n is a positive integer'''

    primes = []
    for i in range(1, n):
        if prime(i):
            primes.append(i)

    print(primes)


def divisors(n):
    '''(int)->None
    prints all the divisors of n
    Precondition: n is a positive integer'''

    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(divisors)
