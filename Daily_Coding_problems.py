"""Given an array of integers, return a new array such that each element at index i of the new array
is a product of all the numbers in the original array except the one at i"""


def product_not_i(arr):
    arr_product = 1
    for i in arr:                                   # runtime: O(n)
        arr_product *= i
    new_arr = []
    for i in arr:                                   # runtime: O(n)
        new_arr.append(int(arr_product/i))
    return new_arr

# runtime would be O(n): linear


"""Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest possible integer that does not exist in the array.
The array can contain duplicates and negative numbers as well."""


def lowest_int_not_in_arr(arr):
    lst = [0 for i in range(len(arr))]
    print(lst)
    for num in arr:                                 # runtime: O(n)
        if 0 < num < len(lst):
            lst[num - 1] = 1
            print(lst)
    return lst.index(0) + 1                         # runtime at worst: O(n)

# runtime would be at worst O(n): linear


"""cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4. Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr."""


def car(pair):
    def cons(a, b):
        return a
    return pair(cons)


def cdr(pair):
    def cons(a, b):
        return b
    return pair(cons)


"""Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'."""


def possible_decodes(message):
    if len(message) == 0:
        return 0
    else:
        count = 1
        for i, j in enumerate(message):                                     # runtime: O(n)
            try:
                if int(j) == 1 and int(message[i+1]):
                    count += 1
                elif int(j) == 2 and int(message[i+1]) not in [7, 8, 9]:
                    count += 1
            except:
                continue
        return count

# runtime would be at worst O(n): linear


"""Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix. For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal]."""


def auto_system(set_of_strings, query_string):
    new_list = []
    length = len(query_string)
    for string in set_of_strings:                               # runtime: O(n)
        if length <= len(string):
            if query_string == string[:length]:
                new_list.append(string)
    return new_list

# runtime would be at worst O(n): linear


"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2"""


def staircase(stairs_num):
    if stairs_num <= 1:
        return 1
    return staircase(stairs_num - 1) + staircase(stairs_num - 2)

# runtime would be O(n^2): quadratic


"""Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced.
For example, given the string "([])[]({})", return true. Given the string "([)]" or "((()", return false."""


def balanced_string(str):
    rb = 0
    cb = 0
    sb = 0

    if str[0] == ")" or str[0] == "}" or str[0] == "]":
        return False

    if str[-1] == "(" or str[-1] == "{" or str[-1] == "[":
        return False

    for i in range(len(str)):           # runtime: O(n)
        if str[i] == "(":
            if str[i+1] == "}" or str[i+1] == "]":
                return False
            rb += 1
        elif str[i] == "{":
            cb += 1
            if str[i+1] == "]" or str[i+1] == ")":
                return False
        elif str[i] == "[":
            if str[i+1] == "}" or str[i+1] == ")":
                return False
            sb += 1
        elif str[i] == ")":
            rb -= 1
            if rb == -1:
                return False
        elif str[i] == "}":
            cb -= 1
            if cb == -1:
                return False
        elif str[i] == "]":
            sb -= 1
            if sb == -1:
                return False

    return rb == 0 and cb == 0 and sb == 0


# runtime would be at worst O(n): linear


"""Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated 
successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded 
as "4A3B2C1D2A". Implement run-length encoding and decoding. You can assume the string to be encoded have no digits 
and consists solely of alphabetic characters. You can assume the string to be decoded is valid."""


class EncoderDecoder:
    def __init__(self, val):
        self.val = val

    def encoding(self):
        encoded_val = ""
        counter = 0
        for i, j in enumerate(self.val):
            counter += 1
            try:
                if self.val[i] != self.val[i+1]:
                    encoded_val += str(counter) + j
                    counter -= counter
            except:
                encoded_val += str(counter) + j
        self.val = encoded_val

    def decoding(self):
        decode_val = ""
        for i, j in enumerate(self.val):
            try:
                if type(int(j)) == int:
                    decode_val += str(self.val[i+1] * int(j))
            except:
                continue
        self.val = decode_val


"""Given a list of numbers and a number k, return whether any 2 numbers from the list add up to k."""


def sums_to_k(lst, k):
    for n in lst:
        return k - n in lst


# Bonus:
def sums_to_k_2(lst, k):
    return [(n, i) for n in lst for i in lst if i + n == k]      # list of the values that add to k and empty if none


"""Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
"""


def running_median(lst):
    running_lst = []
    for num in lst:
        running_lst.append(num)
        running_lst.sort()
        if len(running_lst) % 2 == 0:
            print((running_lst[(len(running_lst) // 2 - 1)] + running_lst[len(running_lst) // 2]) / 2)
        else:
            print(running_lst[len(running_lst) // 2])


"""Given the root to a binary search tree, find the second largest node in the tree."""


class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.l_child = None
        self.r_child = None

    def get_val(self):
        return self.val

    def get_l_child(self):
        return self.l_child

    def get_r_child(self):
        return self.r_child

    def set_l_child(self, child):
        self.l_child = child

    def set_r_child(self, child):
        self.r_child = child


class BinaryTree:
    def __init__(self, val):
        self.root = BinaryNode(val)

    def add_element(self, val, current_node=None):
        new_node = BinaryNode(val)
        if current_node is None:
            current_node = self.root
        if current_node.get_val() > val:
            if current_node.get_l_child() is None:
                current_node.set_l_child(new_node)
            else:
                current_node = current_node.get_l_child()
                self.add_element(val, current_node)
        elif current_node.get_val() < val:
            if current_node.get_r_child() is None:
                current_node.set_r_child(new_node)
            else:
                current_node = current_node.get_r_child()
                self.add_element(val, current_node)
        else:
            print("Node value already in tree! Value not added.")

    def second_max_element(self):
        if self.root.get_r_child() is None:
            if self.root.get_l_child() is None:
                return print("Only one value in tree")
            else:
                current_node = self.root.get_l_child()
                while current_node.get_r_child() is not None:
                    current_node = current_node.get_r_child()
                return current_node.get_val()
        else:
            current_node = self.root
            right_child = current_node.get_r_child()
            while right_child.get_r_child() is not None:
                current_node = current_node.get_r_child()
                right_child = current_node.get_r_child()
            return current_node.get_val()


"""Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
lexicographically earliest one (the first one alphabetically). For example, given the string "race", you should
return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes
first alphabetically. As another example, given the string "google", you should return "elgoogle"."""


def shortest_palindrome(str):
    if len(str) <= 1:
        return str

    if is_palindrome(str):
        return str

    current_palindrome = ""
    left_side_palindrome = ""
    right_side_palindrome = ""
    for i, j in enumerate(str):

        if i != 0 and j == str[0]:
            if is_palindrome(str[0: i+1]):
                left_side_palindrome = str[0: i+1]

        elif i != len(str)-1 and j == str[-1]:
            if is_palindrome(str[i:]):
                if len(str[i:]) > len(right_side_palindrome):
                    right_side_palindrome = str[i:]

    if len(left_side_palindrome) > len(right_side_palindrome):
        for i in range(len(str) - len(left_side_palindrome)):
            current_palindrome += str[-1 - i]
        current_palindrome += str

    elif len(left_side_palindrome) < len(right_side_palindrome):
        current_palindrome += str
        for i in range(len(str) - len(right_side_palindrome)):
            string = str[0: len(str) - len(right_side_palindrome)]
            current_palindrome += string[-1 - i]

    else:
        earliest_letter = check_letter(str)

        if earliest_letter == str[0]:
            current_palindrome += str
            for i in range(len(str)-1):
                current_palindrome += str[-2 - i]

        elif earliest_letter == str[-1]:
            for i in range(len(str) - 1):
                current_palindrome += str[-1 - i]
            current_palindrome += str

    return current_palindrome


def is_palindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-1 - i]:
            return False
    return True


def check_letter(str):
    lower_str = str.lower()
    earliest_letter = ""
    conversions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                   'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                   'x': 24, 'y': 25, 'z': 26}

    if conversions[lower_str[0]] < conversions[lower_str[-1]]:
        earliest_letter += str[0]

    elif conversions[lower_str[0]] > conversions[lower_str[-1]]:
        earliest_letter += str[-1]

    else:
        next_letter = check_letter(str[1:-1])
        if next_letter == str[1]:
            earliest_letter += str[0]
        elif next_letter == str[-2]:
            earliest_letter += str[-1]

    return earliest_letter


"""Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array
so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array. Do this in linear time and in-place. For example,
given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']."""


def segregated_array(array):
    while True:
        left_index, right_index = 0, 1

        while right_index is not len(array)-1:
            if array[left_index] is 'B' or array[right_index] is 'R':
                array[left_index], array[right_index] = array[right_index], array[left_index]
            right_index += 1
            left_index += 1

        while left_index is not 0:
            if array[left_index] is 'B' or array[right_index] is 'R':
                array[left_index], array[right_index] = array[right_index], array[left_index]
            right_index -= 1
            left_index -= 1

        counter = 0
        for i in range(len(array) - 1):
            if array[i] != array[i+1]:
                counter += 1

        print(counter)

        if counter <= 2:
            break

    return array


"""Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:
Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
and the number of steps it should run for. Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to
bottom-rightmost live cell."""


def conway_game(starting_list, n):
    live_cells = starting_list
    for i in range(n):
        cells_to_remove = []
        cells_to_add = []
        adjacent_dict = {}

        for cell in live_cells:
            neighbours = adjacent_cells(cell[0], cell[1])
            live_neighbours = 0

            for neighbour in neighbours:
                adjacent_dict.setdefault(str(neighbour), [neighbour, 0])
                adjacent_dict[str(neighbour)][1] += 1

                if neighbour in live_cells:
                    live_neighbours += 1

            if live_neighbours < 2 or live_neighbours > 3:
                cells_to_remove.append(cell)

        for cell in adjacent_dict:
            if adjacent_dict[cell][1] == 3 and adjacent_dict[cell][0] not in live_cells:
                cells_to_add.append(adjacent_dict[cell][0])

        for cell in cells_to_remove:
            live_cells.remove(cell)
        live_cells += cells_to_add

        print(live_cells)

    return


def adjacent_cells(x, y):
    neighbours = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for i in neighbours:
        i[0] += x
        i[1] += y

    return neighbours


"""The edit distance between two strings refers to the minimum number of character insertions, deletions,
and substitutions required to change one string to the other. For example, the edit distance between
“kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them."""


def edit_distance(str_1, str_2):
    distance = 0
    if len(str_1) == len(str_2):
        short = len(str_1)
        diff = 0
    else:
        short = min(len(str_1), len(str_2))
        diff = abs(len(str_1) - len(str_2))
    for i in range(short):
        if str_1[i] != str_2[i]:
            distance += 1
    distance += diff

    return distance


"""Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting
airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible
itineraries, return the lexicographically smallest one. All flights must be used in the itinerary. For example, given
the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting  airport 'YUL', you
should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']. Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM', you should return null. Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'),
('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though
['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller."""


def shortest_route(stops, start):
    current_pos = start
    short_route = [start]

    while len(stops) != 0:
        possible_stop = []

        for stop in stops:
            if stop[0] is current_pos:
                possible_stop.append(stop)

        if len(possible_stop) is 0:
            return None

        elif len(possible_stop) is 1:
            current_pos = possible_stop[0][1]
            short_route.append(current_pos)
            stops.remove(possible_stop[0])

        else:
            lex_small = '   '
            for pos in possible_stop:
                lex_small = get_first_letter(lex_small, pos[1])
            stops.remove((current_pos, lex_small))
            current_pos = lex_small
            short_route.append(current_pos)

    return short_route


def get_first_letter(str_1, str_2):
    low_1, low_2 = str_1.lower(), str_2.lower()
    conversions = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                   'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                   'x': 24, 'y': 25, 'z': 26, ' ': 27}

    for i in range(len(low_1)):
        if conversions[low_1[i]] < conversions[low_2[i]]:
            return str_1
        elif conversions[low_1[i]] > conversions[low_2[i]]:
            return str_2


"""Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null. Integers can appear more than once in the list.
You may assume all numbers in the list are positive. For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
return [12, 9, 2, 1] since it sums up to 24."""


def adds_to_k(subset, k):
    work_list = sorted(subset)
    subset_list = []

    while len(work_list) is not 0:
        subset_list = check_subset(work_list, subset_list, k)

        if len(subset_list) is not 0:
            return subset_list
        work_list.pop()
    return None


def check_subset(subset, subset_list, k):
    work_list = []

    for i in subset:
        if i <= k:
            work_list.append(i)

    if len(subset) is 0:
        return []

    if k is work_list[-1]:
        return [k]

    big_vs_k = k - work_list[-1]
    subset_list = check_subset(work_list[:-1], subset_list, big_vs_k)

    if len(subset_list) is not 0:
        subset_list.append(work_list[-1])

    return subset_list


"""Implement a stack that has the following methods: push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
then it should throw an error or return null. max(), which returns the maximum value in the stack currently. If there
are no elements in the stack, then it should throw an error or return null. Each method should run in constant time."""


class Node:
    def __init__(self, val, nn=None):
        self.val = val
        self.nn = nn

    def get_val(self):
        return self.val

    def get_nn(self):
        return self.nn

    def set_nn(self, nn):
        self.nn = nn


class Stack:
    def __init__(self, val, size=1):
        self.hn = Node(val)
        self.size = size

    def push(self, val):
        new_node = Node(val)
        new_node.set_nn(self.hn)
        self.hn = new_node
        self.size += 1

    def pop(self):
        if self.size is 0:
            return None

        current_node = self.hn
        self.hn = current_node.get_nn()

        self.size -= 1

        return current_node.get_val()

    def max(self):
        if self.size is 0:
            return None
        return self.size


"""Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required. For example, given [(30, 75), (0, 50), (60, 150)], you should return 2."""


def min_classrooms(times):
    classrooms = len(times)
    start = []
    end = []
    for i in times:
        start.append(i[0])
        end.append(i[1])
    start.sort()
    end.sort()

    while start[-1] >= end[0]:

        for i in start:
            for j in end:
                if i >= j:
                    classrooms -= 1
                    start.remove(i)
                    end.remove(j)

    return classrooms


"""You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on. Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path,
then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the
edges of the board. For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is
7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row."""


def quick_route(board, start, end):
    steps = 0

    start_l = [start]
    end_l = [end]

    while True:
        length = len(start_l)
        for i in range(len(start_l)):

            adjacent_tiles = get_adjacent_tiles(start_l[i][0], start_l[i][1])

            for tile in adjacent_tiles:
                if inside_board(board, tile[0], tile[1]):
                    if not board[tile[0]][tile[1]]:
                        if [tile[0], tile[1]] not in start_l:
                            start_l.append(tile)

        steps += 1

        for cor in start_l:
            if cor in end_l:
                return steps

        if length is len(start_l):
            return None


def get_adjacent_tiles(x, y):
    neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    adjacent_tiles = []
    for n in neighbours:
        adjacent_tiles.append([n[0] + x, n[1] + y])

    return adjacent_tiles


def inside_board(board, x, y):
    return 0 <= x <= len(board[0]) - 1 and 0 <= y <= len(board) - 1


print(quick_route([[False, False, False, False],
                   [True, True, False, True],
                   [False, False, False, False],
                   [False, False, False, False]],
                  [3, 0], [0, 0]))


"""Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive)."""
import random


def rand7():
    rand67 = random.randint(6, 7)
    return random.choice((rand5(), rand67))


def rand5():
    return random.randint(1, 5)


"""We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and
A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element. Given an
array, count the number of inversions it has. Do this faster than O(N^2) time. You may assume each element in the array
is distinct. For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions:
(2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion."""


def num_inversions(array):
    count = 0
    while len(array) != 0:
        num = array[0]
        for i in array[1:]:
            if num > i:
                count += 1
        array.remove(array[0])

    return count


"""Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one. For example,
the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana"."""


def palindromic_substring(string):
    length = len(string)
    while length != 0:
        for i in range(len(string) + 1 - length):
            if is_palindrome(string[i:length+i]):
                return string[i:length+i]
        length -= 1


def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1] and is_palindrome(string[1:-1]):
        return True

    return False


"""Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null. For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
 you should return ['the', 'quick', 'brown', 'fox']. Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
 and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']."""


def str_dict_sentence(dictionary, string):
    ori_list = []
    for i in dictionary:
        length = len(dictionary[i])
        for j in range(len(string)):
            if string[j: j + length] == dictionary[i]:
                ori_list.append(dictionary[i])
                string = string[0:j] + string[j + length:]

    if len(string) != 0:
        return None

    return ori_list


"""Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it. For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars."""


def stock_trader(prices):
    best_trade = 0
    low_point = 0, prices[0]
    high_point = 0, prices[0]

    for i, j in enumerate(prices):
        if j < low_point[1]:
            low_point = i, j

        if j > high_point[1] or low_point[0] > high_point[0]:
            high_point = i, j

        if low_point[0] < high_point[0] and high_point[1] - low_point[1] > best_trade:
            best_trade = high_point[1] - low_point[1]

    return best_trade


"""Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following inorder traversal:
[d, b, e, a, f, c, g]
You should return the following tree:
    a
   / \
  b   c
 / \ / \
d  e f  g
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def reconstructing(pre_order, in_order):
    root = Node(pre_order[0])
    root_index = in_order.index(pre_order[0])
    pre_order.remove(pre_order[0])

    current_node = root
    current_index = root_index

    while len(pre_order) is not 0:

        if in_order.index(pre_order[0]) < current_index:
            if current_node.left_child is None:
                current_node.left_child = Node(pre_order[0])
                pre_order.remove(pre_order[0])
            else:
                current_node = current_node.left_child

        elif in_order.index(pre_order[0]) > current_index:
            if current_node.right_child is None:
                current_node.right_child = Node(pre_order[0])
                pre_order.remove(pre_order[0])

            else:
                current_node = current_node.right_child

    return root


"""Given an array of numbers, find the maximum sum of any contiguous subarray of the array. For example, given the array
[34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86. Given the
array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements. Do this in O(N) time."""


def max_sum_array(array):
    max_sum = 0
    count_hold = 0
    count = 0

    for num in array:
        if count + num < 0:
            if count_hold is 0:
                if max_sum < count:
                    max_sum = count
                count = 0
            elif count_hold > count * -1:
                if count > 0:
                    count_hold += count
                    count = 0
                count += num
            else:
                if max_sum < count_hold:
                    max_sum = count_hold
                count_hold = 0
                count = 0

        elif count + num < count:
            if count_hold is 0:
                count_hold = count
                count = num
            elif count_hold > 0:
                count_hold += count
                count = num

        else:
            count += num

    if count > 0:
        count_hold += count

    if max_sum < count_hold:
        max_sum = count_hold

    return max_sum


"""Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is
one of '+', '−', '∗', or '/'. Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5)."""


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


root = BinaryTreeNode('*')
a = BinaryTreeNode('+')
b = BinaryTreeNode('+')

a1 = BinaryTreeNode(3)
a2 = BinaryTreeNode(2)
b1 = BinaryTreeNode(4)
b2 = BinaryTreeNode(5)

root.left_child = a
root.right_child = b
a.left_child = a1
a.right_child = a2
b.left_child = b1
b.right_child = b2


def arithmetic_expression(node):
    if type(node.data) == int:
        return node.data

    elif type(node.data) == str:
        if node.data is '+':
            node.data = arithmetic_expression(node.left_child) + arithmetic_expression(node.right_child)

        elif node.data is '-':
            node.data = arithmetic_expression(node.left_child) - arithmetic_expression(node.right_child)

        elif node.data is '*':
            node.data = arithmetic_expression(node.left_child) * arithmetic_expression(node.right_child)

        elif node.data is '/':
            node.data = arithmetic_expression(node.left_child) / arithmetic_expression(node.right_child)

        return node.data


"""Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space."""


class Node:
    def __init__(self, data, nn=None):
        self.data = data
        self.nn = nn

class LinkedList:
    def __init__(self, hn_data):
        self.hn = Node(hn_data)
        self.size = 1

    def add(self, data):
        new_node = Node(data)
        new_node.nn = self.hn
        self.hn = new_node
        self.size += 1

A = LinkedList(10)
A.add(8)
A.add(7)
A.add(3)

B = LinkedList(10)
B.add(8)
B.add(1)
B.add(99)
B.add(100)


def intersection(ll_1, ll_2):
    difference = abs(ll_1.size - ll_2.size)

    if difference != 0:
        if ll_1.size > ll_2.size:
            for i in range(difference):
                ll_1.hn = ll_1.hn.nn
        elif ll_1.size < ll_2.size:
            for i in range(difference):
                ll_2.hn = ll_2.hn.nn

    while ll_1.hn.nn is not None:
        if ll_1.hn.data == ll_2.hn.data:
            return ll_1.hn
        ll_1.hn = ll_1.hn.nn
        ll_2.hn = ll_2.hn.nn

    return print("Does not intersect!")


"""Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input,
write a function that shuffles a deck of cards represented as an array using only swaps. It should run in O(N) time."""
import random

def shuffle(k):
    deck = [i for i in range(52)]

    for i, j in enumerate(deck):
        swap_index = random.randint(1, k)

        if swap_index >= 52:
            swap_index = swap_index % 51

        deck[i], deck[swap_index] = deck[swap_index], j

    return deck


"""Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
subarray of length k. For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them."""

array = [10, 5, 2, 7, 8, 7]
k = 3

for i in range(len(array) - k + 1):
    print(max(array[i:i+k]))


"""Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability."""
import random


def pick(stream):
    random_element = None

    for i, j in enumerate(stream):
        if i == 0:
            random_element = j
        elif random.randint(1, i + 1) == 1:
            random_element = j

    return random_element


"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
characters. For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""


def longest_distinct_substring(string, k):
    substring = ""
    working_list = []

    for i in string:
        working_list.append(i)

        dict_test = {}

        for j in working_list:
            dict_test.setdefault(j, 0)

        while len(dict_test) > k:
            working_list.remove(working_list[0])
            dict_test = {}
            for j in working_list:
                dict_test.setdefault(j, 0)

        if len(working_list) > len(substring):
            substring = ""
            for j in working_list:
                substring += j

    return substring


"""Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n,
and contain the following methods: set(key, value): sets key to value. If there are already n items in the cache
and we are adding a new item, then it should also remove the least recently used item. get(key):
gets the value at key. If no such key exists, return null. Each operation should run in O(1) time."""


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class Cache:
    def __init__(self, n):
        self.max_size = n
        self.size = 0
        self.head_node = None

    def set(self, key, value):

        if self.max_size == 0:
            return print("The defined cache space is 0.")

        if self.max_size == 1:
            if self.head_node is not None:
                print("Had to remove least used key and value.")
            self.head_node = Node(key, value)
            self.size = 1
            return

        if self.head_node is None:
            self.head_node = Node(key, value)
            self.size += 1
            return

        if self.size == self.max_size:
            current_node = self.head_node
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
            self.size -= 1
            print("Had to remove least used key and value.")

        new_node = Node(key, value)
        new_node.next = self.head_node
        self.head_node = new_node
        self.size += 1

    def get(self, key):

        if self.max_size == 0:
            return print("The defined cache space is 0.")

        current_node = self.head_node

        while current_node.key != key:
            if current_node.next is None:
                return None
            current_node = current_node.next

        return current_node.value


"""Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with
the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it."""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.head_node = None
        self.size = 0

    def push(self, val):
        if self.head_node is None:
            self.head_node = Node(val)
            self.size += 1

        else:
            new_node = Node(val, self.head_node)
            self.head_node = new_node
            self.size += 1


class Queue:
    def __init__(self):
        self.head_node = None
        self.size = 0

    def enqueue(self, sta1, sta2):
        if sta1.size == 0:
            print("No elements in stack")
        else:
            self.head_node = sta1.head_node
            self.size = sta1.size

        if sta2.size == 0:
            print("No elements in stack")

        else:
            new_element = sta2.head_node
            while new_element.next_node is not None:
                new_element = new_element.next_node
            new_element.next_node = self.head_node
            self.head_node = sta2.head_node
            self.size += sta2.size

    def dequeue(self):
        if self.size == 0:
            print("No elements in queue")

        elif self.size == 1:
            print("Removing {} from the queue.".format(self.head_node.data))
            self.head_node = None

        else:
            element_to_dequeue = self.head_node
            while element_to_dequeue.next_node.next_node is not None:
                element_to_dequeue = element_to_dequeue.next_node
            print("Removing {} from the queue.".format(element_to_dequeue.next_node.data))
            element_to_dequeue.next_node = None
            self.size -= 1


"""Implement a URL shortener with the following methods: shorten(url), which shortens the url into a six-character
alphanumeric string, such as zLg6wl. restore(short), which expands the shortened string into the original url.
If no such shortened string exists, return null."""
import random
import string


class URLshortener:

    def __init__(self):
        self.holder = {}
        self.size = 0

    def shorten(self, url):

        key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        if key in self.holder:
            return print("Key occupied. Try again")

        self.holder[key] = url
        print("Added the URL: {} - it's access key is: {}".format(url, key))
        self.size += 1
        return key

    def restore(self, key):

        if self.size == 0:
            return print("No URLs in the holder.")

        if key not in self.holder:
            return None

        print("The key: {} returns the URL: {}".format(key, self.holder[key]))
        url = self.holder[key]
        self.holder.pop(key)
        self.size -= 1
        return url


"""Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or
less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of
words. If there's no way to break the text up, then return null. You can assume that there are no spaces at the ends of
the string and that there is exactly one space between each word. For example, given the string "the quick brown fox
jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10."""


def str_break_up(s, k):
    current_list = []
    current_sentence = ""
    current_word = ""
    for i, j in enumerate(s):
        current_word += j

        if j == " ":
            current_sentence += current_word
            current_word = ""

        if i % k == 0 and i != 0:
            if len(current_sentence) == 0:
                return None
            if current_sentence[-1] == " ":
                current_list.append(current_sentence[:-1])
            else:
                current_list.append(current_sentence)
            current_sentence = ""

    if (len(current_sentence) + len(current_word) != 0) < k:
        current_sentence += current_word
        current_word = ""

    if len(current_sentence) != 0:
        current_list.append(current_sentence)

    if len(current_word) != 0:
        current_list.append(current_word)

    return current_list


"""A sorted array of integers was rotated an unknown number of times. Given such an array, find the index of the
element in the array in faster than linear time. If the element doesn't exist in the array, return null. For example,
given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
You can assume all the integers in the array are unique."""


def rotated_array(array, e):
    if array[0] == e:
        return 0
    if array[len(array)//2] == e:
        return len(array)//2
    if array[0] < e < array[len(array)//2]:
        return rotated_array(array[1:len(array)//2], e)
    else:
        return rotated_array(array[len(array)//2:], e) + len(array[:len(array)//2])


"""Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55. Given the multiset {15, 5, 20, 10, 35},
it would return false, since we can't split it up into two subsets that add up to the same sum."""


def equal_subsets(multiset):
    sum_list = 0

    for num in multiset:
        sum_list += num

    if sum_list % 2 != 0:
        return False

    half_sum = sum_list / 2
    smallest_subset = len(multiset) // 2

    return has_sum(multiset, half_sum, smallest_subset)


def has_sum(subset, k, size):
    if k in subset:
        return True
    else:
        if size == 1:
            return False
        for num in subset:
            subset.remove(num)
            if has_sum(subset, k-num, size-1):
                return True
        return False


"""Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns
x^y. Do this faster than the naive method of repeated multiplication. For example, pow(2, 10) should return 1024."""


def pow(x, y):
    if y == 0:
        return 1

    half = pow(x, int(y / 2))

    if y % 2 == 0:
        return half * half

    else:
        return half * half * x


"""There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the 
top-left corner and getting to the bottom-right corner. You can only move right or down. For example, given a 2 by 2 
matrix, you should return 2, since there are two ways to get to the bottom-right: Right, then down. Down, then right.
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right."""


def ways_in_matrix(n, m):
    if n == 1 or m == 1:
        return 1

    return ways_in_matrix(n - 1, m) + ways_in_matrix(n, m - 1)


"""Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in 
the matrix by going left-to-right, or up-to-down. For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, 
given the target word 'MASS', you should return true, since it's the last row."""


def matrix_words(matrix, word):
    vedical_word = ""
    latteral_word = ""

    for i, j in enumerate(matrix):
        for k in range(len(j)):
            vedical_word += matrix[k][i]
            latteral_word += matrix[i][k]

            if vedical_word == word or latteral_word == word:
                return True

            if len(vedical_word) == len(matrix[0]):
                vedical_word = ""

            if len(latteral_word) == len(matrix[0]):
                latteral_word = ""

    return False


"""Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12"""


def clockwise_print(n, m):
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            matrix[i][j] = i * n + j + 1

    low_x = 0
    high_x = n
    low_y = 0
    high_y = m



    while low_x < high_x and low_y < high_y:
        for i in range(low_x, high_x):
            print(matrix[low_y][i])

        low_y += 1

        for i in range(low_y, high_y):
            print(matrix[i][high_x - 1])

        high_x -= 1

        if low_y < high_y:

            for i in range(high_x - low_x):
                print(matrix[high_y - 1][high_x - 1 - i])

            high_y -= 1

        if low_x < high_x:

            for i in range(low_y, high_y):
                print(matrix[high_y - i][low_x])

            low_x += 1


"""Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but
also not 0-100 or 100-0). You do not know the bias of the coin. Write a function to simulate an unbiased coin toss."""
import random

def unbiased_toss(eq):
    val = 0
    for _ in range(100000):
        val += eq
    val * 13
    val//10
    val % 100
    if val < 50:
        return 0
    return 1


def toss_biased():
    num = random.randint(1, 10)
    if num < 5:
        return 0
    return 1


"""Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n,
and contain the following methods: set(key, value): sets key to value. If there are already n items in the cache
and we are adding a new item, then it should also remove the least frequently used item. If there is a tie,
then the least recently used key should be removed. get(key): gets the value at key. If no such key exists,
return null. Each operation should run in O(1) time."""


class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node


class Cache:
    def __init__(self, n):
        self.max_size = n
        self.size = 0
        self.head = None
        self.tail = None

    def set(self, key, value):
        if self.size == self.max_size:
            print("Removing {} due to space".format(self.head.key))
            self.head = self.head.next_node
            self.size -= 1

        if self.head is None:
            self.head = Node(key, value)
            self.tail = self.head
            self.size += 1

        else:
            self.tail.next_node = Node(key, value)
            self.tail = self.tail.next_node
            self.size += 1

    def get(self, key):
        value_to_return = None

        current_node = self.head

        while current_node is not None:

            if current_node.key == key:
                value_to_return = current_node.value

            current_node = current_node.next_node

        return value_to_return


"""On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that
have another bishop located between them, i.e. bishops can attack through pieces. You are given N bishops, represented
as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack
each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
For example, given M = 5 and the list of bishops:
(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4."""


def special_chessboard(n, m):
    attacking_bishops = []

    bishop_list = []

    for bishop in n:
        bishop_list.append(list(bishop))

    for i, piece in enumerate(bishop_list):
        valid_targets = targets(piece, m)

        for target in valid_targets:
            for bishop in bishop_list:
                if target == bishop:
                    if [i, bishop_list.index(target)] not in attacking_bishops and \
                            [bishop_list.index(target), i] not in attacking_bishops:
                        attacking_bishops.append([i, bishop_list.index(target)])

    return len(attacking_bishops)


def inside_board(poss, m):
    x, y = poss
    return 0 <= x < m and 0 <= y < m


def targets(piece, m):
    target_list = []

    directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

    for direction in directions:
        for i in range(m):
            x, y = piece

            if direction[0] == -1:
                x += -1 - i
            else:
                x += 1 + i
            if direction[1] == -1:
                y += -1 - i
            else:
                y += 1 + i

            target = [x, y]

            if inside_board(target, m):

                target_list.append(target)

    return target_list


"""Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5."""


def largest_product(ints):
    high_1 = 0
    high_2 = 0
    high_3 = 0

    low_1 = 0
    low_2 = 0

    for n in ints:
        if n >= high_1:
            high_3 = high_2
            high_2 = high_1
            high_1 = n

        elif n >= high_2:
            high_3 = high_2
            high_2 = n

        elif n >= high_3:
            high_3 = n

        if n <= low_1:
            low_2 = low_1
            low_1 = n

        elif n <= low_2:
            low_2 = n

    if high_1 * high_2 * high_3 < low_1 * low_2 * high_1:
        return low_1 * low_2 * high_1

    return high_1 * high_2 * high_3


"""A number is considered perfect if its digits sum up to exactly 10. Given a positive integer n,
return the n-th perfect number. For example, given 1, you should return 19. Given 2, you should return 28."""


def perfect_digit(n):
    return int(str(n) + str(10-n))


"""Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive)."""
import random


def rand7():
    return random.randint(1, 7)


def rand5():
    num = rand7()
    if num > 5:
        num = rand5()

    return num


"""Given the head of a singly linked list, reverse it in-place."""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, data):
        self.head_node = Node(data)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def printer(self):
        current_node = self.head_node

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def reverse(self):
        current_node = self.head_node
        previous_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
            self.head_node = previous_node


"""Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th
column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed). Given integers N and X, write a function that
returns the number of times X appears as a value in an N by N multiplication table. For example,
given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
| 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 4 | 6 | 8 | 10 | 12 |
| 3 | 6 | 9 | 12 | 15 | 18 |
| 4 | 8 | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |
And there are 4 12's in the table."""


def mul_table(n, x):
    count = 0

    table = [[0 for _ in range(n)] for _ in range(n)]

    for i, row in enumerate(table):
        for j, column in enumerate(row):
            table[i][j] = (j + 1) * (i + 1)

            if table[i][j] == x:
                count += 1

    return count


"""Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping
intervals have been merged. The input list is not necessarily ordered in any way. For example, given
[(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]."""


def overlapping(array):
    no_overlap = []

    while len(array) != 0:
        current_low = None
        current_high = None

        for interval in array:
            if current_low is None or interval[0] < current_low:
                current_low = interval[0]
                current_high = interval[1]

        check = True

        while check:

            check = False

            for interval in reversed(array):
                if interval[0] >= current_low and interval[1] <= current_high:
                    array.remove(interval)

                elif interval[1] >= current_high >= interval[0] >= current_low:
                    current_high = interval[1]
                    array.remove(interval)
                    check = True

        no_overlap.append((current_low, current_high))

    return no_overlap


"""You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed
to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically
For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.
As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered (there's only one row).
As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it."""


def low_matrix(matrix):
    if len(matrix) <= 1:
        return 0

    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            matrix[i][j] = converter(letter)

    col_to_remove = 0

    print(matrix)

    for i, row in enumerate(matrix):
        current_val = matrix[0][i]
        for j, letter in enumerate(row):
            if current_val > matrix[j][i]:
                col_to_remove += 1

            elif current_val < matrix[j][i]:
                current_val = matrix[j][i]

    return col_to_remove


def converter(letter):
    return ord(letter)


"""Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list."""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, data):
        self.head_node = Node(data)
        self.tail_node = self.head_node

    def push(self, data):
        new_node = Node(data)
        self.tail_node.next_node = new_node
        self.tail_node = new_node

    def add_ll(self, ll):
        self.tail_node.next_node = ll.head_node
        self.tail_node = ll.tail_node

    def printer(self):
        current_node = self.head_node

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


"""Given an array of integers, write a function to determine whether the array could become non-decreasing by
modifying at most 1 element. For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing. Given the array [10, 5, 1], you should return false,
since we can't modify any one element to get a non-decreasing array."""


def mod_1_element(array):
    count = 0

    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            count += 1

    return count <= 1


"""Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
    a
   / \
  b   c
 /
d"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = []

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            self.elements.append(self.root)

        else:

            for node in self.elements:
                if node.left is None:
                    node.left = TreeNode(data)
                    self.elements.append(node.left)
                    return

                if node.right is None:
                    node.right = TreeNode(data)
                    self.elements.append(node.right)
                    return

    def deepest_node(self):
        print(self.elements[-1].data)


"""Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”."""


def read7(string):
    return string[0:7]


def readN(string, n):

    list_to_return = []

    for i in range(n):
        list_to_return.append(read7(string))
        string = string[7:]

    return list_to_return


"""Invert a binary tree."""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = []

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            self.elements.append(self.root)

        else:
            for node in self.elements:
                if node.left is None:
                    node.left = TreeNode(data)
                    self.elements.append(node.left)
                    return

                if node.right is None:
                    node.right = TreeNode(data)
                    self.elements.append(node.right)
                    return

    def invert(self):
        for node in self.elements:
            node.left, node.right = node.right, node.left

"""Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents
water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water."""


def islands(matrix):

    all_island_tiles = []

    num_of_islands = 0

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == 1:
                if [i, j] not in all_island_tiles:
                    num_of_islands += 1
                    all_island_tiles.append([i, j])
                    adjacent_island = adjacent_islands(matrix, i, j, all_island_tiles)
                    for island in adjacent_island:
                        if island not in all_island_tiles:
                            all_island_tiles.append(island)

    return num_of_islands


def adjacent_islands(matrix, i, j, all_island_tiles):
    islands = all_island_tiles

    adjacent_tiles = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    for tile in adjacent_tiles:
        if 0 <= tile[0] + i < len(matrix) and 0 <= tile[1] + j < len(matrix[0]):
            if matrix[tile[0] + i][tile[1] + j] == 1:
                if [tile[0] + i, tile[1] + j] not in islands:
                    islands.append([tile[0] + i, tile[1] + j])
                    adjacent_island = adjacent_islands(matrix, tile[0] + i, tile[1] + j, islands)
                    for island in adjacent_island:
                        if island not in islands:
                            islands.append(island)

    return islands


"""Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make
the string valid (i.e. each open parenthesis is eventually closed). For example, given the string "()())()",
you should return 1. Given the string ")(", you should return 2, since we must remove all of them."""


def valid_string(string):
    delete = 0

    count = 0

    start = True

    for char in string:
        if char == ")" and start:
            delete += 1

        elif char == "(" and start:
            count += 1
            start = False

        elif char == "(":
            count += 1

        elif char == ")":
            count -= 1
            if count == 0:
                start = True

    delete += count

    return delete


def valid_string(s, p):
    if p == '.*':
        return True
    if p == '.':
        return len(s) == 1
    if '*' not in p:
        return s == p

    current_p = ""
    while len(p) != 0:
        current_p += p[0]
        p = p[1:]
        if current_p[-1] == '*':
            break

    while len(s) != 0:
        if current_p[-1] != '*':
            if s[:len(current_p)-1] != current_p[:-1] and current_p[0] != '.':
                return False
            else:
                if current_p[0] == '.':
                    return len(s) == 1
                return s == current_p
        else:

            if s[:len(current_p)-1] == current_p[:-1]:
                s = s[len(current_p)-1:]
            else:
                if len(p) == 0:
                    return False
                else:
                    current_p = ""
                    while len(p) != 0:
                        current_p += p[0]
                        p = p[1:]
                        if current_p[-1] == '*':
                            break

    return True


"""Determine whether a tree is a valid binary search tree. A binary search tree is a tree with two children,
left and right, and satisfies the constraint that the key in the left child must be less than or equal to
the root and the key in the right child must be greater than or equal to the root."""


def valid_binary_tree(node):
    if node.left is None and node.right is None:
        return True

    elif node.left is None:
        if node.right.val >= node.val:
            return valid_binary_tree(node.right)

    elif node.right is None:
        if node.left.val <= node.val:
            return valid_binary_tree(node.left)

    elif node.left.val <= node.val <= node.right.val:
        return valid_binary_tree(node.left) and valid_binary_tree(node.right)

    return False


"""Given an integer n and a list of integers l, write a function that randomly
generates a number from 0 to n-1 that isn't in l (uniform)."""
import random


def uniform(n, l):
    num = random.uniform(0, n-1)

    while num in l:
        num = random.uniform(0, n-1)

    return num


"""We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the
prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering. For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'],
'CSC100': []}, should return ['CSC100', 'CSC200', 'CSC300']."""


def course_map(hashmap):
    needed_courses = []
    for course in hashmap:
        for c in hashmap[course]:
            if c not in hashmap:
                return None
            if c not in needed_courses:
                needed_courses.append(c)
        if course not in needed_courses:
            needed_courses.append(course)

    needed_courses.sort()

    return needed_courses


"""Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
It should contain the following methods: set(key, value, time): sets key to value for t = time. get(key, time):
gets the key at t = time. The map should work like this. If we set a key at a particular time, it will maintain
that value forever or until it gets set at a later time. In other words, when we get a key at a time,
it should return the value that was set for that key set at the most recent time."""


class HashMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value, time):
        if self.map.setdefault(key, [value, time]) != [value, time]:
            self.map[key] = [value, time]

    def get(self, key, time):
        if key in self.map:
            if time == self.map[key][1]:
                return self.map[key][0]

            return "Incorrect timestamp"

        return "Key not in map"


"""The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once. For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false."""


def exists(board, word):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == word[0]:
                if check(board, word[1:], x, y, [x, y]):
                    return True

    return False

def check(board, word, x, y, holder):
    if len(word) == 0:
        return True

    neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    current_neighbours = [[i+x, j+y] for i, j in neighbours]

    for neighbour in current_neighbours:
        if 0 <= neighbour[0] < len(board) and 0 <= neighbour[1] < len(board[0]):
            if board[neighbour[0]][neighbour[1]] == word[0] and [neighbour[0], neighbour[1]] not in holder:
                if check(board, word[1:], neighbour[0], neighbour[1], holder + [[neighbour[0], neighbour[1]]]):
                    return True

    return False


"""You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.
Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2)."""


def min_steps(array):
    steps = 0
    for i in range(len(array)-1):
        x_diff = abs(array[i][0] - array[i+1][0])
        y_diff = abs(array[i][1] - array[i+1][1])
        steps += max(x_diff, y_diff)

    return steps

print(min_steps([(0, 0), (1, 1), (1, 2)]))


"""Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.
Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d."""


def goldbach_conjecture(n):
    if n <= 3 or n % 2 == 1:
        return False

    for i in range(2, n):
        if is_prime(i):
            if is_prime(n-i):
                return [i, n-i]

def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0 and i != n:
            prime = False

    return prime


"""Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9."""


def sum_to_k(lst, k):

    check_lst = []
    sum = 0

    for num in lst:
        check_lst.append(num)
        sum += num

        while sum > k:
            sum -= check_lst[0]
            check_lst.remove(check_lst[0])

        if sum == k:
            return check_lst

    return print("No contiguous elements of the list sum to K.")


"""Given an integer list where each number represents the number of jumps you can make, determine whether you can reach
to the last index starting at index 0. For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False."""


def can_jump_to_last(array):
    print(array)

    if len(array) == 0:
        return True

    if array[0] >= len(array) - 1:
        return True

    for i in range(array[0]-1, 0, -1):
        if can_jump_to_last(array[i+1:]):
            return True

    return False


"""Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def add(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node

        else:
            for node in self.nodes:
                if node.left is None:
                    node.left = new_node
                    break
                elif node.right is None:
                    node.right = new_node
                    break

        self.nodes.append(new_node)

    def print_tree(self):
        for node in self.nodes:
            print(node.data)


"""Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false."""


def a_shifted_b(a, b):
    if len(a) == len(b):
        for i, letter in enumerate(a):
            if letter == b[0]:
                if a[i:] + a[:i] == b:
                    return True
    return False


"""Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped,
the 3rd and 4th bit should be swapped, and so on. For example, 10101010 should be 01010101.
11100010 should be 11010001. Bonus: Can you do this in one line?"""


def bit_swap(bit_num):
    return int(''.join([str(1) if i == '0' else str(0) for i in str(bit_num)]))


"""Given a word W and a string S, find all starting indices in S which are anagrams of W.
For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4."""


def all_anagrams(w, s):
    if len(w) > len(s):
        return None

    check = False

    for i in range(len(s) - (len(w) - 1)):
        if check:
            if s[i-1] == s[i+len(w)-1]:
                print(i)
            else:
                check = False

        else:
            if is_anagram(w, s[i:i+len(w)]):
                print(i)
                check = True


def is_anagram(s1, s2):
    return set(s1) - set(s2) == set()


"""Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
return "here world hello" Follow-up: given a mutable string representation, can you perform this operation in-place?"""


def swap_words(s):
    return ' '.join(reversed([i for i in s.split()]))


"""Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node
values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself."""


def check_s_and_t(s, t):
    trees_to_check = []

    nodes_to_check = [t]

    while len(nodes_to_check) != 0:
        for node in nodes_to_check:
            if node.left:
                nodes_to_check.append(node.left)
            if node.right:
                nodes_to_check.append(node.right)

            if node.value == s.value:
                trees_to_check.append(node)

            nodes_to_check.remove(node)

    if len(trees_to_check) == 0:
        return False

    for tree in trees_to_check:
        if same_tree(s, tree):
            return True

    return False


def same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if (tree1 and not tree2) or (not tree1 and tree2):
        return False

    return tree1.value == tree2.value and same_tree(tree1.left, tree2.left) and same_tree(tree1.right, tree2.right)


"""Given a binary tree, return the level of the tree with minimum sum."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def low_sum_of_level(root):
    queue = [root]

    level = 0

    low_sum = 0, root.val

    while len(queue) > 0:

        current_sum = 0

        temp = []

        for i, node in enumerate(queue):
            current_sum += node.val
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            queue.remove(node)

        if current_sum < low_sum[1]:
            low_sum = level, current_sum

        level += 1

        queue = temp

    return low_sum[0]


"""Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]."""


def sorted_squares(lst):
    squares = [i*i for i in lst]
    squares.sort()
    return squares


"""Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them. For example, given the intervals
[0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}."""


def small_covers(s):

    high = None
    low = None

    for interval in s:
        if not high or interval[0] > high:
            high = interval[0]

        if not low  or interval[1] < low:
            low = interval[1]

    if low >= high:
        return {high}
    return {low, high}


"""Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'."""


def can_make_palindrome(s, k):
    length = len(s)
    reverse_s = s[::-1]

    return is_palindrome(s, reverse_s, length, length) <= k * 2


def is_palindrome(str_1, str_2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str_1[m-1] == str_2[n-1]:
        return is_palindrome(str_1, str_2, m-1, n-1)

    return 1 + min(is_palindrome(str_1, str_2, m-1, n), is_palindrome(str_1, str_2, m, n-1))


"""You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at
matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom
right corner. For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins."""


def most_coins(matrix, m=0, n=0):
    if m == len(matrix) - 1 and n == len(matrix[0]) - 1:
        return matrix[m][n]

    elif m == len(matrix) - 1:
        return matrix[m][n] + most_coins(matrix, m, n+1)

    elif n == len(matrix[0]) - 1:
        return matrix[m][n] + most_coins(matrix, m+1, n)

    return matrix[m][n] + max(most_coins(matrix, m, n+1), most_coins(matrix, m+1, n))


"""
Given a string, return whether it represents a number. Here are the different kinds of numbers:
"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:
"a"
"x 1"
"a -2"
"-"
"""


def repr_num(s):
    try:
        float(s)
        return True
    except:
        pass

    for i, c in enumerate(s):
        if c == 'e':
            return repr_num(s[0:i]) and repr_num(s[i+1:])

    return False


"""You have n fair coins and you flip them all at the same time. Any that come up tails you set aside.
The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?
Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains."""
import random


def one_left(n, uneven=random.choice([True, False])):
    if n == 1:
        return 0

    if n % 2 == 1:
        if uneven:
            uneven = False
        else:
            uneven = True

        if uneven:
            return 1 + one_left(n//2+1, uneven)

    return 1 + one_left(n//2, uneven)


"""Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_target(root, k):
    holder = {}
    nodes_to_check = [root]

    while len(nodes_to_check) != 0:
        current = nodes_to_check[0]
        nodes_to_check.remove(current)

        if k - current.val in holder:
            return current, holder[k - current.val]

        holder.setdefault(current.val, current)

        if current.left:
            nodes_to_check.append(current.left)

        if current.right:
            nodes_to_check.append(current.right)

    return None


"""Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] 
rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. 
How many swap or move operations do you need?"""


def swap(lst, k):
    return lst[k:] + lst[:k]


"""Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.
Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_ll(ll_1, ll_2):
    current_1 = ll_1
    current_2 = ll_2
    sum_root = TreeNode(0)
    current_sum = sum_root

    ten = False

    while current_1 or current_2:

        if current_1:
            current_sum.val += current_1.val

        if current_2:
            current_sum.val += current_2.val

        if ten:
            current_sum.val += 1
            ten = False

        if current_sum.val >= 10:
            current_sum.val -= 10
            ten = True

        current_1 = current_1.next
        current_2 = current_2.next

        if current_1 or current_2:
            new_node = TreeNode(0)
            current_sum.next = new_node
            current_sum = new_node

    if ten:
        new_node = TreeNode(1)
        current_sum.next = new_node

    return sum_root


"""Given a real number n, find the square root of n. For example, given n = 9, return 3."""


def squr(n):
    return n ** (1/2)


"""Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again. For example,
given k = 2 and the array [5, 2, 4, 0, 1], you should return 3."""


def largest_profit(prices, k):
    map = []
    index = []

    low = [0, prices[0]]
    current = [0, prices[0]]

    for i, price in enumerate(prices):

        if price < current[1]:

            if i != low[0] + 1:
                index.append([low[0], current[0]])
                map.append([low[1], current[1]])
            low = [i, price]

        current = [i, price]

    if current[0] != low[0] and current[1] > low[1]:
        index.append([low[0], current[0]])
        map.append([low[1], current[1]])

    if low == [0, prices[0]]:
        return 0

    profit = 0

    if len(map) <= k:
        for pair in map:
            profit += pair[1] - pair[0]

    return profit


"""Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere
in the linked list, deep clone the list."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pointer = None


def deep_clone(head):
    list1 = []
    list2 = []

    current = head

    while current:
        new_node = TreeNode(current.val)

        list1.append(current)
        list2.append(new_node)

        current = current.next

    for i, element in enumerate(list2):
        if i != len(list2) - 1:
            element.next = list2[i+1]

        element.pointer = list2[list1.index(list1[i].pointer)]

    return list2[0]


"""Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations: record(timestamp): records a hit that happened at timestamp.
total(): returns the total number of hits recorded. range(lower, upper): returns the number of hits that
occurred between timestamps lower and upper (inclusive). Follow-up: What if our system has limited memory?"""


class HitCounter:
    def __init__(self):
        self.timestamps = []

    def record(self, timestamp):
        self.timestamps.append(timestamp)

    def total(self):
        return len(self.timestamps)

    def range(self, lower, upper):
        hits = 0
        for stamp in self.timestamps:
            if lower <= stamp <= upper:
                hits += 1
        return hits

# Answer to follow-up: Implement self.maxsize


"""Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.
For example, the inorder successor of 22 is 30.
   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        

def inorder_successor(node):
    current = node.parent
    while current:
        if current.val > node.val:
            return current.val
        current = current.parent    
    return None

"""You have a large array with most of the elements as zero. Use a more space-efficient data structure, SparseArray,
that implements the same interface: init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val. get(i): gets the value at index i."""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.head = None
        if self.size > 1:
            self.head = Node(arr[0])
            current = self.head
            for i in range(1, self.size):
                new = Node(arr[i])
                current.next = new
                current = current.next

    def set(self, i, val):
        current = self.head
        index = 0
        while current:
            if index == i - 1:
                end = current.next
                new = Node(val)
                current.next = new
                new.next = end
                self.size += 1
                return
            index += 1
            current = current.next
        print("List doesn't have that index!")

    def get(self, i):
        current = self.head
        index = 0
        while current:
            if index == i:
                return current.val
            index += 1
            current = current.next
        print("List doesn't have that index!")

        
     
   """Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def min_path(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return node.val
    if not node.left:
        return node.val + min_path(node.right)
    if not node.right:
        return node.val + min_path(node.left)
    else:
        return node.val + min(min_path(node.left), min_path(node.right))

    
"""Implement a bit array. A bit array is a space efficient array that holds a value of 1 or 0 at each index.
init(size): initialize the array with size. set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i."""


class BitArray:
    def __init__(self, size):
        self.array = [0 for _ in range(size)]

    def set(self, i, val):
        assert type(i) == int and i < len(self.array)
        assert val == 0 or val == 1
        self.array[i] = val

    def get(self, i):
        return self.array[i]

    
"""Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢."""


def min_coins(n):
    coins = 0

    coins += n // 25
    n = n % 25

    coins += n // 10
    n = n % 10

    coins += n // 5
    n = n % 5

    coins += n

    return coins


"""Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
find the two elements that appear only once. For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
The order does not matter. Follow-up: Can you do this in linear time and constant space?"""


def two_elements(array):
    array.sort()
    index = 0
    output = None
    while True:
        if index == len(array) - 1 or array[index] != array[index+1]:
            if output:
                return output, array[index]
            output = array[index]
            index += 1
        else:
            index += 2

   
"""Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass"""


class Stack:
    def __init__(self):
        self.list = [[], [], []]

    def pop(self, stack_number):
        return self.list[stack_number].pop()

    def push(self, item, stack_number):
        self.list[stack_number].append(item)

        
"""Given a pivot x, and a list lst, partition the list into three parts.
The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.
For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]"""


def pivot(lst, x):
    partition = []
    small_end_index = 0
    holder = 0
    for element in lst:
        if element < x:
            partition.insert(0, element)
            small_end_index += 1
        elif element > x:
            partition.append(element)
        else:
            holder += 1
    for i in range(holder):
        partition.insert(small_end_index, x)

    return partition


"""Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i,
where distance is measured in array indices. For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest
larger integer, then return null. Follow-up: If you can preprocess the array, can you do this in constant time?"""


def nearest_large_num(array, index):
    right_index = index + 1
    left_index = index - 1

    while right_index <= len(array) - 1 or left_index >= 0:
        if right_index <= len(array) - 1:
            if array[right_index] > array[index]:
                return right_index
        if left_index >= 0:
            if array[left_index] > array[index]:
                return left_index

        right_index += 1
        left_index -= 1

    return None


class PreProcess:
    def __init__(self, array):
        self.array = array
        self.map = {}

        for i in range(len(self.array)):
            self.map[i] = nearest_large_num(self.array, i)

    def get_near_large_num(self, index):
        return self.map[index]

    
    """Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3."""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def swap_two(self):
        prev = self.head
        current = self.head
        next = self.head.next

        while current and next:
            current.next = next.next
            next.next = current

            if prev == self.head:
                self.head = next
            else:
                prev.next = next

            prev = current
            current = current.next
            if current:
                next = current.next

                
                """Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.
For example, given the following tree:
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:
   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant."""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def cut_tree(root):
    queue = [root]
    while len(queue) != 0:
        current = queue[0]
        if current.left:
            if remove(current.left):
                current.left = None
            else:
                queue.append(current.left)
        if current.right:
            if remove(current.right):
                current.right = None
            else:
                queue.append(current.right)
        queue.remove(current)
    return root


def remove(node):
    if not node.left and not node.right:
        return node.val == 0
    if node.left and node.right:
        return remove(node.left) and remove(node.right) and node.val == 0
    if node.left:
        remove(node.left) and node.val == 0
    if node.right:
        return remove(node.right) and node.val == 0

    
"""Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j."""


def reverse(lst, i, j):
    left = lst[:i]
    right = lst[j+1:]

    return left + swap(lst[i:j+1]) + right


def swap(lst):
    swapped_lst = []
    for c in reversed(lst):
        swapped_lst.append(c)

    return swapped_lst


"""Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j]
(including i, excluding j). For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.
You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step."""


class L:
    def __init__(self, lst):
        self.map = {}

        index = 1

        while index < len(lst) - 1:
            for i in range(0, len(lst) - (index-1)):
                self.map[str(i) + " " + str(i + index)] = sum(lst[i: i + index])
            index += 1

    def sum(self, low_i, high_i):
        return self.map[str(low_i) + " " + str(high_i)]
    

"""Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
return [(0, 0), (3, 1)]."""


def k_nearest_points(lst, center, k):
    points = []
    distances = []

    for point in lst:
        distance = abs(point[0] - center[0]) + abs(point[1] - center[1])
        if not distances:
            distances.append(distance)
            points.append(point)
        else:
            index = 0
            while index < len(distances) and distances[index] < distance:
                index += 1

            if index == len(distances):
                distances.append(distance)
                points.append(point)
            else:
                distances.insert(index, distance)
                points.insert(index, point)

    return points[:k]


"""Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.
For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B
"""


def fill_change(matrix, pixel, color):
    old_color = matrix[pixel[1]][pixel[0]]
    queue = [list(pixel)]

    while len(queue) > 0:
        current = queue[0]
        matrix[current[1]][current[0]] = color
        adjacent = get_adjacent(current[0], current[1])
        for pixel in adjacent:
            if 0 <= pixel[0] < len(matrix[0]) and 0 <= pixel[1] < len(matrix):
                if matrix[pixel[1]][pixel[0]] == old_color and pixel not in queue:
                    queue.append(pixel)
        queue.remove(queue[0])

    return matrix


def get_adjacent(x, y):
    adjacent = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    return [[x + i[0], y + i[1]] for i in adjacent]


"""You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers
with its corresponding probability. For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
You can generate random numbers between 0 and 1 uniformly."""
import random


def corresponding_probability(nums, probs):
    choice = random.uniform(0, 1)

    total = 0

    options = []

    for val in probs:
        total += val
        options.append(total)

    assert total == 1

    for i, val in enumerate(options):
        if choice <= val:
            return nums[i]

        
"""Find an efficient algorithm to find the smallest distance (measured in number of words) between any two
given words in a string. For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words."""


def smallest_distance(text, w1, w2):
    sample = text.split()

    start = False
    index = 0
    smallest = None

    for word in sample:
        if word == w1:
            start = True
            index = 0
        if word == w2 and start:
            if not smallest or index - 1 < smallest:
                smallest = index - 1
        index += 1

    return smallest


"""Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).
You can assume that such element exists. For example, given [1, 2, 1, 1, 3, 4, 1], return 1."""


def majority_element(array):
    map = {}

    for element in array:
        map.setdefault(element, 0)
        map[element] += 1

    for element in map:
        if map[element] > len(array) // 2:
            return element

        
"""Given a positive integer n, find the smallest number of squared integers which sum to n. For example,
given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4. Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9."""


def small_square(num):
    high_base = 1

    while True:
        if high_base ** 2 > num:
            break
        high_base += 1

    small_num = None
    current_num = 0
    sum = 0

    for i in range(high_base, 0, -1):

        current_base = i

        while sum != num:
            if current_base**2 + sum > num:
                current_base -= 1
            else:
                sum += current_base**2
                current_num += 1
                if small_num and current_num > small_num:
                    break

        if not small_num or current_num < small_num:
            small_num = current_num

    return small_num


"""Given a string, determine whether any permutation of it is a palindrome. For example,
carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome."""


def is_palindrome_permutation(string):
    map = {}

    for c in string:
        map.setdefault(c, 0)
        map[c] += 1

    odd = False

    for c in map:
        if map[c] % 2 == 1:
            if odd:
                return False
            odd = True

    return True


"""Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null."""


def first_recurring_chr(string):
    map = {}

    for c in string:
        if c in map:
            return c
        map[c] = 0

    return None


"""Given a 32-bit integer, return the number with its bits reversed. For example, given the binary number
1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111."""


# assume they're given as a list of strings
def binary_reversed(bitcode):
    reversed_bitcode = []
    for four_bit in bitcode:
        four_reversed = ""
        for c in four_bit:
            if c == "0":
                four_reversed += '1'
            else:
                four_reversed += '0'
        reversed_bitcode.append(four_reversed)

    return reversed_bitcode


"""You are given a list of data entries that represent entries and exits of groups of people into a building.
An entry looks like this: {"timestamp": 1526579928, count: 3, "type": "enter"} This means 3 people entered the building.
An exit looks like this: {"timestamp": 1526580382, count: 2, "type": "exit"} This means that 2 people exited the
building. timestamp is in Unix time. Find the busiest period in the building, that is, the time with the most people
in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and
ends up empty, i.e. with 0 people inside."""


def most_in_building(entries):
    current = entries[0]['count']
    start = entries[0]['timestamp']

    high = entries[0]['count']
    time = start, start

    for i in range(1, len(entries)):
        if current == 0:
            start = entries[i]['timestamp']
        if entries[i]['type'] == 'enter':
            current += entries[i]['count']
        else:
            current -= entries[i]['count']
        if current > high:
            high = current
            time = start, entries[i]['timestamp']

    return time


"""Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following
methods: next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left. For example, given the input
[[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty."""


class Iterator2D:
    def __init__(self, array2d):
        self.array2d = array2d
        self.current_index = None

    def next(self):
        if not self.has_next():
            raise Exception
        else:
            if not self.current_index:
                for i, array in enumerate(self.array2d):
                    if len(array) > 0:
                        self.current_index = i, 0
                        break
            else:
                if len(self.array2d[self.current_index[0]]) - 1 <= self.current_index[1]:
                    for i in range(self.current_index[0] + 1, len(self.array2d)):
                        if len(self.array2d[i]) > 0:
                            self.current_index = i, 0
                            break
                else:
                    self.current_index = self.current_index[0], self.current_index[1] + 1
            return self.array2d[self.current_index[0]][self.current_index[1]]

    def has_next(self):
        if not self.current_index:
            for i, array in enumerate(self.array2d):
                if len(array) > 0:
                    return True
            return False
        else:
            if len(self.array2d[self.current_index[0]]) - 1 <= self.current_index[1]:
                for i in range(self.current_index[0]+1, len(self.array2d)):
                    if len(self.array2d[i]) == 0:
                        return True
                return False
            else:
                return True


"""Given an N by N matrix, rotate it by 90 degrees clockwise. For example, given the following matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?"""


def rotation90clockwise(array2d):
    rotation = [[0 for _ in range(len(array2d))] for _ in range(len(array2d))]

    length = len(array2d) - 1
    low = 0

    for x, array in enumerate(array2d):
        for y in range(len(array2d)-1, -1, -1):
            print(x, y)
            rotation[low+y][length-x] = array2d[x][y]

    return rotation


"""Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)]."""


class Solution:
    def unique_indices(self, lst):
        unique = []

        for x in range(len(lst) - 1):
            for y in range(x+1, len(lst)):
                word1 = lst[x] + lst[y]
                word2 = lst[y] + lst[x]
                if self.is_palindrome(word1):
                    unique.append((x, y))
                if self.is_palindrome(word2):
                    unique.append((y, x))

        return unique


    def is_palindrome(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-1-i]:
                return False
        return True
    
  
"""Given a string s and a list of words words, where each word is the same length, find all starting indices of
substrings in s that is a concatenation of every word in words exactly once. For example, given
s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog"
starts at index 13. Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings
composed of "dog" and "cat" in s. The order of the indices does not matter."""


class Solution:
    def __init__(self, s, words):
        self.s = s
        self.words = words
        self.w_length = len(words[0])
        self.indices = []

    def find_starting_indices(self):
        for i in range(len(self.s) - self.w_length):
            if self.s[i:i+self.w_length] in self.words:
                if self.is_concatenation(i, self.words):
                    self.indices.append(i)
        return self.indices

    def is_concatenation(self, index, words):
        current_list = [i for i in words]
        while current_list:
            current_list.remove(self.s[index:index + self.w_length])
            index += self.w_length
            if not current_list:
                return True
            if index > len(self.s) and current_list:
                break
            if self.s[index:index + self.w_length] not in current_list:
                break
        return False


"""Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur."""


def flatten_dict(nested):
    keys = []
    vals = []
    flattened = []
    for key in nested:
        if type(nested[key]) == dict:
            new_keys, new_vals = unnest(key, nested[key])
            keys += new_keys
            vals += new_vals
        else:
            keys.append(key)
            vals.append(nested[key])
    for i in range(len(keys)):
        flattened.append({keys[i]: vals[i]})
    return dict(pair for d in flattened for pair in d.items())

def unnest(key, value):
    keys = []
    vals = []
    for e in value:
        if type(value[e]) == dict:
            new_keys, new_vals = unnest(e, value[e])
            keys += [key + '.' + i for i in new_keys]
            vals += new_vals
        else:
            keys.append(key + '.' + e)
            vals.append(value[e])
    return keys, vals


"""You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.
For example, given the starting state a, number of steps 5000, and the following transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }."""
import random


class Solution:
    def markov_chain(self, state, array, steps):
        self.output = {}
        self.current_pos = state

        for i in range(steps):
            ran = random.uniform(0, 1)
            self.prev_val = 0
            self.helper(ran, array)
        return self.output

    def helper(self, ran, array):
        for element in array:
            if element[0] == self.current_pos:
                if element[2] + self.prev_val > ran:
                    self.current_pos = element[1]
                    self.output.setdefault(element[1], 0)
                    self.output[element[1]] += 1
                    break
                self.prev_val += element[2]
        return

    
"""Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters."""


class Solution:
    def one_to_one_mapping(self, s1, s2):
        short = min(len(s1), len(s2))
        for i in range(short - 1):
            print(s1[-i-1:])
            print(s2[:i+1])
            if s1[-i-1:] == s2[:i+1]:
                return True
        return False

    
"""Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2."""


class Note:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        if not self.head:
            self.head = Note(val)
            self.tail = self.head
        else:
            new = Note(val)
            self.tail.next = new
            self.tail = new

    def rotate(self, k):
        queue = [self.head]
        while queue[-1].next:
            queue.append(queue[-1].next)
            if len(queue) > k:
                queue.remove(queue[0])
        queue[-1].next = self.head
        self.tail = queue[-1]
        self.head = queue[0]
        return self.head

 
"""Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple
probabilistic games. The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six.
Your number of rolls is the amount you pay, in dollars. The second game: same, except that the stopping condition
is a five followed by a five. Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value."""
import random


class Solution:
    def dice_game(self, first, second):
        first_roll_cleared = False
        dollars = 0
        while True:
            ran_num = random.randint(1, 6)
            dollars += 1
            if first_roll_cleared:
                if ran_num == second:
                    return dollars
                if ran_num != first:
                    first_roll_cleared = False

            else:
                if ran_num == first:
                    first_roll_cleared = True

    def simulation(self, first, second):
        sum = 0
        for i in range(10000):
            sum += self.dice_game(first, second)
        return sum / 10000

# She should pick first game (conditional probability)


"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


class Solution:
    def twoSum(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                return [start, end]
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return None
    
    

"""Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows."""


class Solution:
    def reverse(self, x: int) -> int:
        lst = [i for i in reversed(str(x))]
        minus = False

        if lst[-1] == '-':
            lst.pop()
            minus = True

        lst = int(''.join(lst))

        if lst > 2 ** 31 - 1:
            return 0

        if minus:
            return -lst
        return lst
    
    
"""Given an array of elements, return the length of the longest subarray where all its elements are distinct. For example,
given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1]."""


def longest_subarray(array):
    long = 0
    start = 0
    subarray = {}

    for i, e in enumerate(array):
        if e in subarray:
            if i - subarray[e] > long:
                long = i - (subarray[e] + 1)
            if start < subarray[e] + 1:
                start = subarray[e] + 1
        if i - start > long:
            long = i - start
        subarray[e] = i

    long += 1

    return long


"""Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1"""


class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - (len(needle) - 1)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

    
"""You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying
to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether
you can get to the end of the array. For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
0 -> 1 -> 3 -> 5, so return true. Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false."""


def can_reach_end(array):
    if not array:
        return []

    if array[0] >= len(array) - 1:
        return True

    else:
        for i in range(array[0]):
            if can_reach_end(array[i+1:]):
                return True

    return False


"""Given a array of numbers representing the stock prices of a company in chronological order, write a function that
calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee
that represents a transaction fee for each buy and sell transaction. You must buy before you can sell the stock, but
you can make as many transactions as you like. For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9,
since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10
dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees."""


def max_profit(array, fee):
    if not array:
        return 0

    profit = 0
    buy = array[0]

    for i, num in enumerate(array):
        if num < buy:
            buy = num
        if num - fee > buy:
            try:
                if array[i+1] < num - fee:
                    profit += num - fee - buy
                    buy = array[i+1]
            except:
                pass

    if array[-1] - fee > buy:
        profit += array[-1] - fee - buy

    return profit


"""Let A be an N by M matrix in which every row and every column is sorted.
Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
For example, given the following matrix:
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23."""


def smaller_larger_than(matrix, low, high):
    num_of_elements = 0

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num < matrix[low[0]][low[1]] or num > matrix[high[0]][high[1]]:
                num_of_elements += 1

    return num_of_elements


"""Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place."""


def rotate(array, k):
    assert k < len(array)

    for i in range(k):
        for j in range(len(array) - 1):
            array[-1-j], array[-2-j] = array[-2-j], array[-1-j]

    return array


"""Given a set of distinct positive integers, find the largest subset such that every pair of elements
in the subset (i, j) satisfies either i % j = 0 or j % i = 0. For example, given the set [3, 5, 10, 20, 21],
you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24]."""


def largest_modular_subpair(array):
    hm = {}
    ls = []

    for num in array:
        hm.setdefault(num, [])
        for element in hm:
            if num % element == 0:
                hm[element].append(num)
                if len(hm[element]) > len(ls):
                    ls = hm[element]

    return ls


"""Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval
in X contains at least one point in P. Compute the smallest set of points that stabs X.
For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9]."""


def real_line(array):
    start = array[0][1]
    end = array[-1][0]

    for point in array:
        if point[1] < start:
            start = point[1]

        if point[0] > end:
            end = point[0]

    return [start, end]


"""You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the
sum of the entries. Write a program that returns the weight of the maximum weight path."""


def max_weight_path(array):
    if not array:
        return 0

    current_weight = array[-1]
    for i in range(len(array) - 1):
        next_level = []
        for j in range(len(current_weight) - 1):
            if array[-2-i][j] + current_weight[j] > array[-2-i][j] + current_weight[j+1]:
                next_level.append(array[-2-i][j] + current_weight[j])
            else:
                next_level.append(array[-2-i][j] + current_weight[j+1])
        current_weight = next_level

    return current_weight[0]


"""Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
678 is not a palindrome. Do not convert the integer into a string."""


def is_int_palindrome(num):
    while num >= 10:
        right = num % 10
        temp = 10
        while num // temp != 0:
            temp *= 10
        temp //= 10
        left = num // temp

        if left == right:
            num -= temp
            num //= 10

        else:
            return False

        
 """Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary
tree has every level filled except the last, and the nodes in the last level are filled starting from the left."""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.notes = []
        self.root = None

    def add(self, val):
        new_note = TreeNode(val)

        self.notes.append(new_note)

        if not self.root:
            self.root = new_note
        else:
            for note in self.notes:
                if not note.left:
                    note.left = new_note
                    break
                if not note.right:
                    note.right = new_note
                    break

    def count(self):
        print(len(self.notes))

        
"""A permutation can be specified by an array P, where P[i] represents the location of the element at i
in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"]
and the permutation [2, 1, 0], return ["c", "b", "a"]."""


def permutation_swap(array, perm):
    new_array = [i for i in range(len(array))]

    for i, num in enumerate(perm):
        new_array[i] = array[num]

    return new_array


"""Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio"."""


def long_common_sub(w1, w2, w3):
    w1 = make_vowels(w1)
    w2 = make_vowels(w2)
    w3 = make_vowels(w3)
    length = len(w1)
    times = 1
    while length > 0:
        for i in range(times):
            print(w1[i:i+length])
            if in_word(w1[i:i+length], w2) and in_word(w1[i:i+length], w3):
                return len(w1[i:i+length])
        length -= 1
        times += 1
    return None


def make_vowels(word):
    new_word = ''
    for letter in word:
        if letter in ['e', 'i', 'o']:
            if not new_word:
                new_word += letter
            else:
                new_word += letter if letter != new_word[-1] else ''
    return new_word


def in_word(w1, w2):
    return w1 in w2


"""A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?"""


def collatz_sequence(n):
    sequence = 0
    for i in range(n*10):
        if n == 1:
            return sequence
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = 3 * n + 1
        sequence += 1
    return False


def bonus():
    large = 0, 0
    for i in range(1000000):
        current = collatz_sequence(i+1)
        if current > large[0]:
            large = current, i
    return large[1]


"""Spreadsheets often use this alphabetical encoding for its columns:
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....Given a column number,
return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA"."""


def num_to_letter(num):
    assert type(num) == int
    assert num > 0

    string = ''
    temp = []

    while num != 0:
        if num % 26 == 0:
            temp.append(26)
            num = num // 26 - 1
        else:
            temp.append(num % 26)
            num = num // 26

    for val in reversed(temp):
        string += chr(val + 64)

    return string


"""Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
For example, given 156, you should return 3."""


def logest_1_binary(n):
    if n == 0:
        return 0

    start = 1

    while start < n:
        start *= 2

    start //= 2

    bit_code = []

    while n != 0:
        if n // start == 1:
            bit_code.append(1)
            n -= start
        else:
            bit_code.append(0)
        start //= 2

    ones = 0
    counter = 0

    print(bit_code)

    for bit in bit_code:
        if bit == 1:
            counter += 1
        else:
            if ones < counter:
                ones = counter
            counter = 0

    if ones < counter:
        ones = counter
    
    return ones


"""Given a number in Roman numeral format, convert it to decimal. The values of Roman numerals are as follows:
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
For the input XIV, for instance, you should return 14."""


def roman_to_num(string):
    lib = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    num = 0

    for i, letter in enumerate(string):
        if i <= len(string) - 2 and lib[letter] < lib[string[i+1]]:
            continue
        else:
            if i != 0 and lib[letter] > lib[string[i - 1]]:
                num += lib[letter] - lib[string[i - 1]]
            else:
                num += lib[letter]

    return num


"""Write an algorithm that computes the reversal of a directed graph. For example,
if a graph consists of A -> B -> C, it should become A <- B <- C."""


class GraphNote:
    def __init__(self, val):
        self.val = val
        self.from_notes = []
        self.to_notes = []


class Graph:
    def __init__(self):
        self.graph = []

    def add_note(self, val):
        self.graph.append(GraphNote(val))

    def create_link(self, note1, note2):
        for note in self.graph:
            if note.val == note1:
                note1 = note
            elif note.val == note2:
                note2 = note
        note1.to_notes.append(note2)
        note2.from_notes.append(note1)

    def reverse_graph(self):
        for note in self.graph:
            note.from_notes, note.to_notes = note.to_notes, note.from_notes

    def view(self):
        for note in self.graph:
            print(f"VAL: {note.val} - LINKS FROM {note.from_notes} - LINKS TO {note.to_notes}")

            
 """Implement a PrefixMapSum class with the following methods:
insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3
mapsum.insert("column", 2)
assert mapsum.sum("col") == 5"""


class PrefixMapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        assert type(key) == str
        assert type(val) == int
        self.map[key] = val

    def sum(self, prefix):
        assert type(prefix) == str

        sum = 0

        for key, val in self.map.items():
            if key[:len(prefix)] == prefix:
                sum += val

        return sum

    
"""Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2."""


def pythogorean_triplet(a, b, c):
    if a >= b and a >= c:
        return c**2 + b**2 == a**2
    elif b >= a and b >= c:
        return a** 2 + c ** 2 == b ** 2
    else:
        return a ** 2 + b ** 2 == c ** 2

     
"""A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's
friendship relations. In other words, this is the smallest set such that no student in the group has any friends
outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.
Given a friendship list such as the one above, determine the number of friend groups in the class."""


def num_of_groups(friendships):
    groups = 0
    holder = set()

    def helper(value):
        for val in value:
            if val not in holder:
                holder.add(val)
                helper(friendships[val])

    for key, value in friendships.items():
        if value == []:
            groups += 1
        else:
            if key not in holder:
                holder.add(key)
                groups += 1
                helper(value)

    return groups


"""UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes. For example, the Euro sign,
€, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:
For a single-byte character, the first bit must be zero. For an n-byte character, the first byte starts with n ones
and a zero. The other n - 1 bytes all start with 10. Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values,
and returns whether it is a valid UTF-8 encoding."""


def valid_UTF(vals):
    if len(vals) > 7:
        return False

    if len(vals) == 1:
        assert type(vals) == list and len(vals[0]) == 8
        return vals[0][0] == '0'

    for i, val in enumerate(vals):
        assert type(vals) == list and len(vals[0]) == 8

        if i == 0:
            for j, bit in enumerate(val):
                if j < len(vals) and bit == '0':
                    return False
                if j == len(vals) + 1 and bit == '1':
                    return False

        else:
            if val[0:2] != '10':
                return False

    return True


"""On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud."""


def top_3_candidates():
    with open("text.txt", "r") as f:
        data = f.read()

        voters = set()

        candidates = {}

        for voter, can in data:
            if voter in voters:
                print(f"Voter: {voter} is a fraud!")

            else:
                voters.add(voter)
                candidates.setdefault(can, 0)
                candidates[can] += 1

        assert len(candidates) >= 3
        sorted_candidates = sorted(candidates.items(), key=lambda x: x[1])

        return sorted_candidates[:3]

    
"""Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the
values of the corresponding nodes of the input trees. If only one input tree has a node in a given position,
the corresponding node in the new tree should match that input node."""


class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.tree_list = []

    def add(self, val):
        new_node = BinaryNode(val)

        if not self.root:
            self.root = new_node

        else:
            for node in self.tree_list:
                if not node.left:
                    node.left = new_node
                    break
                if not node.right:
                    node.right = new_node
                    break

        self.tree_list.append(new_node)


def add_2_binary_nodes(node1, node2):

    new_val = 0

    if node1:
        new_val += node1.val

    if node2:
        new_val += node2.val

    new_node = BinaryNode(new_val)

    if (node1 and node1.left) or (node2 and node2.left):
        new_node.left = add_2_binary_nodes(node1.left, node2.left)

    if (node1 and node1.right) or (node2 and node2.right):
        new_node.right = add_2_binary_nodes(node1.right, node2.right)

    return new_node


def add_2_binary_trees(root1, root2):
    if not root1 and not root2:
        return None

    tree_root = (add_2_binary_nodes(root1, root2))

    return tree_root


"""Consider the following scenario: there are N mice and N holes placed at integer points along a line.
Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.
Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.
For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this
case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6."""


def minimize_mice_to_holes(mize, holes):
    mize.sort()
    holes.sort()

    max_diff = 0

    for i in range(len(mize)):
        if abs(mize[i] - holes[i]) > max_diff:
            max_diff = abs(mize[i] - holes[i])

    return max_diff


"""In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom
right are identical. Here is an example:
[[1, 2, 3, 4, 8],
[5, 1, 2, 3, 4],
[4, 5, 1, 2, 3],
[7, 4, 5, 1, 2]]
Write a program to determine whether a given input is a Toeplitz matrix."""


def check_right_and_down(matrix, num, x, y):
    try:
        if matrix[y+1][x+1] == num:
            return check_right_and_down(matrix, num, x+1, y+1)
        return False
    except:
        return True


def is_toeplitz_matrix(matrix):
    for y, array in enumerate(matrix):
        if y == 0:
            for x, num in enumerate(array):
                if not check_right_and_down(matrix, num, x, y):
                    return False

        else:
            if not check_right_and_down(matrix, array[0], 0, y):
                return False

    return True


"""Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example,
given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)]."""


def pythagoras(a, b):
    return (a**2 + b**2)**(1/2)


def closest_points(array):
    points = [], 0

    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            euclidean_dist = pythagoras(abs(array[i][0] - array[j][0]), abs(array[i][1] - array[j][1]))

            if not points[0] or euclidean_dist < points[1]:
                points = [array[i], array[j]], euclidean_dist

    return points[0]


"""Given an array of numbers and a number k, determine if there are three entries in the array which add up to the
specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49."""


def is_sum_of_3_elements(array, num):
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == num:
                    return True

    return False


"""A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
For example, 16891 is strobogrammatic. Create a program that finds all strobogrammatic numbers with N digits."""


def is_strobogrammatic(string):
    length = len(string)

    if length % 2 == 1:
        if string[length // 2] not in ["0", "1", "8"]:
            return False

    for i in range(length // 2):
        if string[i] in ["0", "1", "8"]:
            if string[i] != string[-i-1]:
                return False
        elif string[i] == "6":
            if string[-i-1] != "9":
                return False
        elif string[i] == "9":
            if string[-i-1] != "6":
                return False
        else:
            return False

    return True


def strobogrammatic_numbers(n):
    if n == 0:
        return []

    numbers = []

    for i in range(10**(n-1), 10**(n), 1):
        if is_strobogrammatic(str(i)):
            numbers.append(i)

    return numbers



