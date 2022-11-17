def get_year():
    '''None->int'''
    year = ""
    while len(year) < 4 :
      year_user = input("Please give a four digit integer for the year : ")
      if year_user.isnumeric() and len(year_user) == 4 :
        year = year_user
        return int(year_user)


def linear_search_v1(lst, value):
    """ (list, object) -> int
    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    """
    index = -1
    i = 0

    if len(lst) == 0:
        return -1

    while i < len(lst):
        if lst[i] == value:
            index = i
        i += 1

    return index


def linear_search_v2(lst, value):
    """ (list, object) -> int
    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1


def linear_search_v3(lst, value):
    """ (list, object) -> int
    Return the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    """
    if len(lst) == 0:
        return -1

    size = len(lst)
    lst.insert(0, value)

    i = -1

    while lst[i] != value:
        i -= 1

    lst.remove(value)

    if i == size:
        return -1

    else:
        return len(lst) + i

def min_or_max_index(L, flag):
    """ (list, bool) -> tuple of (object, int)
    Return the minimum or maximum item and its index from L, depending on
    whether flag is True or False.
    """
    if flag == True:
        min = L[0]
        for i in range(1, len(L)):
            if L[i] < min:
                min = L[i]
        return min, L.index(min)
    else:
        max = L[0]
        for i in range(1, len(L)):
            if L[i] > max:
                max = L[i]
        return max, L.index(max)


def first_one(L):
    ''' (list) -> int
    Return the index of the first occurrence of 1 in L, or return
    -1 if 1 is not in L.
    Precondition: L only has 0s and 1s and all 0s appear before all 1s
    '''
    for i in L:
        if i == 1:
            return L.index(i)

    return -1


def last_zero(L):
    ''' (list) -> int
    Return the index of the last occurrence of 0 in L, or return
    -1 if 0 is not in L.
    Precondition: L only has 0s and 1s and all 0s appear before all 1s'''

    for i in range(len(L) - 1, -1, -1):
        if L[i] == 0:
            return i
    return -1
