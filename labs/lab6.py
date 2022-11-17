def sum_odd_while_v2(n):
    '''(int)->int
       Returns the sum of all odd integers between 5 and n
    '''

    sum = 0
    i = 5
    while i <= n:
        sum = sum + i
        i = i + 2
    return sum

def sum_odd_for_v2(n):
  '''(int)->int
     Returns the sum of all odd integers between 5 and n
  '''

  sum = 0
  for i in range(5, n+1, 2):
        sum += i
  return sum

def sum2():
    while True:
        print("Enter two numbers to add them together")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The sum of the two numbers is: ", num1 + num2)
        print("Do you want to continue? ")
        answer = input("Enter yes or no: ")
        if answer != "yes":
            break

def first_neg(a):
    i = 0

    while i < len(a):

        if a[i] < 0:
            return i
        i += 1
        
    return None

