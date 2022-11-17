import random

def make_matrix_random(a, b, x, y):
    '''(int,int,int,int)->2D list
     Returns a 2D list representing a matrix with a rows and b columns
     filled with random integers >=x and <=y
     Precondition: a,b positive and x <=y
    '''
    matrix = []
    for i in range(a):
        matrix.append([])
        for j in range(b):
            matrix[i].append(random.randint(x,y))
    return matrix


def sum_above_diagonal(m):
    '''(2D list)->number
    Returns the sum of the elements of the matarix m that are on or about the diagonal of m
    (for clarification see the slide entitled: Details about Prog Ex 2)
    Precondition: m is a square matrix filled with numbers

    >>> sum_above_diagonal([[1,2],[10,20]] )
    23
    '''
    sum = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if j >= i:
                sum += m[i][j]
    return sum


def max_over_all_even_cols(m):
    '''(2D list)->number
    Returns the maximum element among all the numbers that are in even columns of m
    i.e. the maximum element amoung all elements in 0th, 2nd, 4th etc. column
    Precondition: m is a matrix filled with numbers with at least 1 row and 1 column

    >>> max_over_all_even_cols([[1,1,1,1,1,1,1],[1,10,3,20,12,6,0]])
    12
    '''

    max = 0
    for i in range(len(m)):
        for j in range(len(m[i])):

            if j % 2 == 0:

                if m[i][j] > max:
                    max = m[i][j]
    return max


def max_each_row(m):
    '''(2D list)->list
    Returns a list where in position p of the list is the max number among all the numebrs of p-th row of m
    Precondition: m is a matrix filled with numbers

    >>> max_each_row([[1,2],[200,0],[3,3],[-10,-20]])
    [2, 200, 3, -10]
    '''
    max_row = []

    for row in m:
        max_row.append(max(row))

    return max_row


def index_of_max_sum_row(m):
    '''(2D list)->int
    Returns the index of a row that has the largest sum of all the rows
    Precondition: m is a matrix filled with numbers
    >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [1,2]])
    2
    >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [10000,2]])
    3
    '''

    largest_sum = sum(m[0])

    largest_sum_index = 0

    for i in range(1, len(m)):

        if sum(m[i]) > largest_sum:
            largest_sum = sum(m[i])

            largest_sum_index = i

    return largest_sum_index


def magic(m):
    '''2D list->bool
    Returns True if m forms a magic square
    Precondition: m is a matrix with at least 2 rows and 2 columns '''

    if len(m) != len(m[0]):
        return False

    for row in m:
        for element in row:
            if type(element) != int:
                return False

    for row in m:
        for element in row:
            if element < 0:
                return False

    sum_of_first_row = sum(m[0])
    for row in m:
        if sum(row) != sum_of_first_row:
            return False

    for i in range(len(m)):
        sum_of_column = 0
        for row in m:
            sum_of_column += row[i]
        if sum_of_column != sum_of_first_row:
            return False

    sum_of_diagonal_1 = 0
    sum_of_diagonal_2 = 0
    for i in range(len(m)):
        sum_of_diagonal_1 += m[i][i]
        sum_of_diagonal_2 += m[i][len(m) - 1 - i]
    if sum_of_diagonal_1 != sum_of_first_row or sum_of_diagonal_2 != sum_of_first_row:
        return False

    biggest_element = 0
    for row in m:
        for element in row:
            if element > biggest_element:
                biggest_element = element
    if biggest_element != len(m) ** 2:
        return False

    return True


def move_zeros_with_return(lst):
    '''lst -> lst
       Returns a new list where the zeros of the given list lst
       are placed to the end (without change the relative order of other numbers)
       Precondition: lst is a list of numbers
    '''
    tmp = []
    for i in lst:
        if i != 0:
            tmp.append(i)
    for i in range(len(lst)):
        if lst[i] == 0:
            tmp.append(0)
    return tmp


def move_zeros_extra_list_no_return(lst):
    '''lst -> None
       moves zeros of the given list lst to the end (without change the relative order of other numbers)
       Precondition: lst is a list of numbers
    '''
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(0)
            lst.remove(0)
    print(x, end=" ")
    print(None)


def move_zeros_in_place(lst):
    '''lst -> None
       moves zeros of the given list lst to the end (but it may change the relative order of other numbers)
       Precondition: lst is a list of numbers
    '''
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(lst[i])
            lst.remove(lst[i])
    print(lst)
