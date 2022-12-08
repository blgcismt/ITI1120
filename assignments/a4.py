from ast import Pass
from random import randint
from time import time

def secondary_minima_maxima(a):
  '''
  (list)-->int
  Take a list <a>  and return the difference between its second maxima and minima
  '''
  max = a[0]
  min = a[0]

  for i in range(len(a)-1) :
    if max < a[i] :
      max = a[i]

  for i in range(len(a)-1) :
    if min > a[i] :
      min = a[i]

  a.remove(max)
  a.remove(min)

  max2 = a[0]
  min2 = a[0]

  for i in range(len(a)-1) :
    if max2 < a[i] :
      max2 = a[i]

  for i in range(len(a)-1) :
    if min2 > a[i] :
      min2 = a[i]

  return max2 - min2

######################################################################################################

def distinctive(set1, list1):
    '''
    (set,list)--> set
    Take a set and a list <set1> and <list1> and return the values in one of them
    but not both in a set
    '''
    result = set()

    for i in set1:
        if i in list1:
            continue
        else:
            result.add(i)

    for i in list1:
        if i in set1:
            continue
        else:
            result.add(i)

    return result

######################################################################################################

def longest_repetition(a):
    '''
    (list)-->int
    Take <a> a list and return the longest run of repetition in the list if no such run
    exists return 1
    '''

    longest = 1
    current = 1

    for index in range(len(a) - 1):

        if a[index] == a[index + 1]:
            current += 1

        else:

            if current > longest:
                longest = current

            current = 1

    if current > longest:
        longest = current

    return longest

######################################################################################################

def multiplication_threshold(a,x):
  '''
  (list,int)--->set
  Take a list <a> and int <x> and return the multiplication of elements of <a> that are smaller than <x>
  ina set
  '''
  results = set()

  for i in a:
    for j in a:
      if i*j <= x :
        results.add(i*j)

  return results

######################################################################################################

def even_multiplication(n):
  '''
  (int)--> int
  Take an integer <n> and calculate the multiplication of the even numbers between
  0 and n recursively
  '''
  if n == 0 :
    return 1

  elif n % 2 != 0 :
    return (n-1)*even_multiplication(n-3)

  else :
    return n * even_multiplication(n-2)

######################################################################################################

def bubble_sort(a):
  '''
  (list)-->list
  Take <a> a list and sort it using the bubble sort method which compares adjacent elements
  and switches places accordingly to have an increasing list
  '''
  for i in range(len(a)):
      for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
  return a

def optimized_bubble_sort(a):
  '''
  (list)-->list
  Take a list <a> and sort it by using an optimized version of bubble sort method
  that decreases the amount of times ran over the list with a loop

  This decreases runtime because each iteration decreases the number of elements to loop over
  which reduces the runtime significantly. This does not cause a problem because those parts
  are sorted in the previous run anyway.
  '''
  for i in range(len(a)):
      for j in range(len(a)-1-i):
          if a[j] > a[j+1]:
              a[j], a[j+1] = a[j+1], a[j]
  return a

def generate_unsorted_list(n):
  '''
  (int)---> list
  Take an integer <n> and create a random list with <n> number of elements and return it
  '''
  unsorted_list = []
  for i in range(n):
      unsorted_list.append(randint(1, 1000000))
  return unsorted_list

start1 = time()

bubble_sort(generate_unsorted_list(10000))

end1 = time()

print("Bubble Sort Algorithm execution time : {}".format(end1-start1))

start2 = time()

optimized_bubble_sort(generate_unsorted_list(10000))

end2 = time()

print("Optimized Bubble Sort Algorithm execution time : {}".format(end2-start2))

print("Execution time saved using Optimized Bubble Sort Algorithm : {}".format((end1-start1)-(end2-start2)))

######################################################################################################

class employee():
    '''
    None --> str
    An employee class that has the methods retirement which returns the number of years until retirement and
    tax which returns the amount paid by the employee in taxes
    '''

    def __init__(self, age, salary):
        self.age = age
        self.salary = salary

    def retirement(self):
        return "the employee still have {} years to retire".format(60 - self.age)

    def tax(self):
        return "the employee pays {} dollars in taxes".format(self.salary * 13 / 100)
