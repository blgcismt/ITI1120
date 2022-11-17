def repeater(s1, s2, n):
    return "_" + (s1 + s2) * n + "_"

def roots(a, b, c):
    a = int(input("A:"))
    b = int(input("B:"))
    c = int(input("C:"))

    delta = b ** 2 - 4 * a * c
    equation = combine(a, "x²") + "+" + "(" + combine(b, "x") + ")" + "+""(" + combine(c, "") + ")"
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)

    print("Equation: {}\nRoot 1: {}\nRoot 2: {}".format(equation, x1, x2))


def combine(word, integer):
    new = str(word) + integer
    return new

def real_roots(a, b, c):
  delta = b ** 2 - 4 * a * c
  return delta>=0

def reverse(x):
  a = x//10
  b = x%10
  return combine2(b, a)


def combine2(int1, int2):
  combination = str(int1)+str(int2)
  return combination

