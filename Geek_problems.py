"""Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given
number S.
Input: The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and
S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
Output: For each testcase, in a new line, print the starting and ending positions(1 indexing) of first
such occuring subarray from the left if sum equals to subarray, else print -1. Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010
Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5"""


def get_subarray(array):
    array.remove(array[0])

    subarrays = []

    while len(array) != 0:
        nums, sum = array[0]
        current_array = array[1]

        array.remove(array[0])
        array.remove(array[0])

        subarrays.append(helper(current_array, sum))

    return subarrays


def helper(array, sum):
    possible_subarrys = []

    for i, n in enumerate(array):
        if len(possible_subarrys) != 0:
            for subarray in possible_subarrys:
                subarray[1] += n
        possible_subarrys.append([i, n])

        for subarray in possible_subarrys:
            if subarray[1] == sum:

                return [subarray[0]+1, i+1]

    return [-1]


print(get_subarray([[2], [5, 12], [1, 2, 3, 7, 5], [10, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))


"""Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of
A[i] <= A[j]. Input: The first line contains an integer T, depicting total number of test cases. Then T test case
follows. First line of each test case contains an integer N denoting the size of the array. Next line contains N space
separated integeres denoting the elements of the array. Output: Print the maximum difference of the indexes i and j in
a separtate line. Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 1018
Example:
Input:
1
9
34 8 10 3 2 80 30 33 1
Output:
6"""


def max_difference(array):
    array.remove(array[0])

    max_diff = []

    while len(array) != 0:
        current_size = array[0][0]
        current_array = array[1]

        array.remove(array[0])
        array.remove(array[0])

        max_diff.append(helper(current_array, current_size))

    return max_diff


def helper(array, size):
    max_diff = None

    length = size - 1
    times = 1

    while max_diff is None and length != 0:

        for i in range(times):

            if array[i] <= array[length+i]:
                max_diff = array.index(array[length+i]) - array.index(array[i])
                return max_diff

        length -= 1
        times += 1

    return max_diff


"""You are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas
the other two number occur exactly once and are distinct. You need to find the other two numbers and print them
in ascending order. Input: The first line contains a value T, which denotes the number of test cases. Then T
test cases follow. The first line of each test case contains a value N. The next line contains 2*N+2 space
separated integers. Output: Print in a new line the two numbers in ascending order. Constraints:
1<=T<=100
1<=N<=10^6
1<=A[i]<=5*10^8
Example: Input:
2
2
1 2 3 2 1 4
1
2 1 3 2
Output:
3 4
1 3"""


def find_numbers(array):
    array.remove(array[0])

    subarrays = []

    while len(array) != 0:
        current_array = array[1]

        array.remove(array[0])
        array.remove(array[0])

        subarrays.append(helper(current_array))

    return subarrays


def helper(array):
    num_to_return = []
    holder = []

    for num in array:
        if num not in holder:
            if num not in num_to_return:
                num_to_return.append(num)
            else:
                holder.append(num)
                num_to_return.remove(num)

    return num_to_return


"""Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid
parenthesis substring. Input: First line contains number of test cases T.  Each test case have one line string S
of character '(' and ')' of length N. Constraints:
1 <= T <= 500
1 <= N <= 105
Example:
Input:
2
((()
)()())
Output:
2
4"""


def parenthesis(string):
    open_paren = 0
    max_open = 0
    counter = 0
    can_continue = True

    for char in string:

        if char == ")" and open_paren == 0:
            can_continue = False

        if char == "(":
            open_paren += 1
            counter += 1
            can_continue = True

        if char == ")" and open_paren != 0:
            open_paren -= 1
            counter += 1

        if counter > max_open:
            max_open = counter

        if not can_continue:
            counter = 0

    return max_open - open_paren