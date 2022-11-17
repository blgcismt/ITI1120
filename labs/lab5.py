def ah(l, x, y):
    '''(list, int,int)->(int,number/+inf)
    Returns two numbers such that ...
    Precondition: x <= y
                  and list l contains numbers
    '''
    count = 0
    min = None
    for i in l:
        if i >= x and i <= y:
            count += 1
            if min == None:
                min = i
            elif i < min:
                min = i
    return count, min


def divisors(n):
    '''(int)->None
    prints all the divisors of n
    Precondition: n is a positive integer'''
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(divisors)


def is_perfect(n):
    ''' (number)->bool
    Returns True if the given positive integer n is perfect
    Precondition: n>=1
    '''
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False


def arithmetic(l):
    '''(list)->bool
      Returns True if list l contains an arithmetic sequence,
      False otherwise
      Precondition: Elements of l are numbers
    '''
    if len(l) < 3:
        return False
    else:
        diff = l[1] - l[0]
        for i in range(2, len(l)):
            if l[i] - l[i - 1] != diff:
                return False
        return True


def is_sorted(l):
    '''(list)->bool
      Returns True if list l is sorted from smallest to largest number,
      False otherwise
      Precondition: Elements of l are numbers
    '''
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True
