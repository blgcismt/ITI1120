import random

def coprime(x,y):
  '''
  (int,int)--> bool

  Precondition: <x> and <y> are positive integers
  Takes integers <x> and <y> and returns True if they are coprime numbers returns False otherwise
  '''
  for i in range(2,y+1):

    if x % i == 0 and y % i == 0 :
      return False

  return True


def all_coprime_pairs(L):
    '''
    (list)--> list

    Precondition: All elements of list <L> are positive and unique integers

    Take a list <L> and find coprime pairs within the list pair them in a tuple and
    append the tuple to a list which is finally returned if there are no coprime pairs
    an empty list is returned
    '''
    tuples = []

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if coprime(L[i], L[j]):
                tuples.append((L[i], L[j]))

    return tuples


def zero_out(a1, a2):
    '''
    (list,list)-->list
    Take 2 lists and replace the occurrences of the 2nd list with 0 in the first list and return the result
    '''

    if len(a1) < len(a2):
        return a1

    length = len(a2)

    for i in range(len(a1)):
        if a1[i:i + length] == a2:
            a1[i:i + length] = [0] * length

    return a1


def coin_flip(flip_results):
    '''
    (file)--> None
    Take each line of file as coin tosses and count the number of coin tosses and print the number of heads and the percentage of heads,
    if it's bigger than 50 percent print you win!
    '''

    path = "/content/drive/MyDrive/ITI1120/Assignments/Assignment3/"  # you can enter your path here, this is my path I used to test

    f = open(path + flip_results).read().splitlines()

    result_list = []

    for line in f:
        result_list.append(line)

    for i in result_list:
        counth = 0
        total_count = 0
        i = i.lower()

        for j in i:
            if j == "h":
                counth += 1
            total_count += 1

        percentage = (counth * 100) / total_count
        percentage = round(percentage, 1)
        print(str(counth) + " heads " + "(" + str(percentage) + "%" + ")")

        if percentage > 50:
            print("You win !")


def run():
    '''
    None --> str
    Does 20 dice tosses and prints a string combining the results if consecutive results exist prints them between parenthesis
    ex :
    1 2 5 5 3 1 2 4 3 2 2 2 2 3 6 5 5 6 3 1  ---> 1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1
    '''
    first_index = 0
    same = False
    results = []

    for i in range(20):
        results.append(random.randint(1, 6))

    length = len(results)
    i = 0

    while i < length:
        if i == length - 1 and results[first_index] == results[i]:
            results.insert(first_index, "(")
            results.append(")")
            break

        if results[first_index] == results[i] and i != 0:
            same = True
            i += 1
            continue

        if results[first_index] != results[i] and same == True:
            results.insert(first_index, "(")
            results.insert(i + 1, ")")
            same = False
            length += 2

        first_index = i
        i += 1

    result = ''.join(str(d) for d in results)

    return result


def is_all_odd(lis):
    '''
    (list)-->bool
    Precondition : elements of list <lis> are integers
    Take a list of lists <lis> and return True if lis is an empty list or all the elements within the lists
    list <lis> are odd integers, return False otherwise.
    '''

    if len(lis) == 0:
        return True

    for i in lis:
        for j in i:
            if j % 2 == 0:
                return False

    return True


def range_diff(lis):
    '''
    (list)--> int
    Take a list of lists <lis> and return the range of values in <lis> which is the biggest number - the smallest number + 1
    '''

    if len(lis) == 0:
        return 0

    biggest = 0
    smallest = lis[0][0]
    for i in lis:
        for j in i:

            if j > biggest:
                biggest = j

            if j < smallest:
                smallest = j

    return (biggest - smallest) + 1


def coupon_collector():
    '''
    None --> None
    Print the number of cards picked before a card is picked from each suite and the cards picked
    '''

    deck = []
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for i in range(len(suits)):
        for j in range(len(values)):
            deck.append([suits[i], values[j]])

    random.shuffle(deck)

    count = 0
    spades = ""
    hearts = ""
    diamonds = ""
    clubs = ""

    while (len(spades) == 0 or len(diamonds) == 0 or len(hearts) == 0 or len(clubs) == 0):

        card_index = random.randint(0, len(deck) - 1)
        card = deck[card_index]

        if (deck[card_index][0].lower() == "hearts"):
            hearts = deck[card_index][1] + " of " + deck[card_index][0]
            deck.append(card)
            deck.remove(card)

        elif (deck[card_index][0].lower() == "spades"):
            spades = deck[card_index][1] + " of " + deck[card_index][0]
            deck.append(card)
            deck.remove(card)

        elif (deck[card_index][0].lower() == "diamonds"):
            diamonds = deck[card_index][1] + " of " + deck[card_index][0]
            deck.append(card)
            deck.remove(card)

        elif (deck[card_index][0].lower() == "clubs"):
            clubs = deck[card_index][1] + " of " + deck[card_index][0]
            deck.append(card)
            deck.remove(card)

        else:
            deck.append(card)
            deck.remove(card)

        count += 1

    print("Cards picked : {}, {}, {}, {}".format(spades, hearts, diamonds, clubs))
    print("Number of cards picked : ", count)


def hangman_game():
    '''
    None --> None
    A hangman game that keeps going until user wants to exit the program
    '''

    word = random.choice(["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"])
    word2 = list(word)
    count = 0
    word_length = len(word)
    word_crypted = "*" * word_length
    word_crypted2 = list(word_crypted)
    guessed = []

    while True:
        letter = input("(Guess) Enter a letter in word {} ".format("".join(word_crypted2)))
        if letter in guessed and letter in "".join(word_crypted2):
            print("{} is already in the word".format(letter))

        elif letter in guessed:
            print("{} is already guessed".format(letter))

        elif letter in word2:
            for i in range(word_length):
                if word2[i] == letter:
                    word_crypted2[i] = letter
                    guessed.append(letter)
            print("".join(word_crypted2))

            if "".join(word_crypted2) == word:
                print("The word is {}, you missed {} time".format(word, count))
                break

        else:
            print("{} is not in the word".format(letter))
            count += 1
        guessed.append(letter)

    if input("Do you want to guess another word? Enter y or n>") == "y":
        hangman_game()
    else:
        exit()
