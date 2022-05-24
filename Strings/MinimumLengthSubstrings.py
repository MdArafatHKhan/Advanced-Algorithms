import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def min_length_substring(s, t):
    # Write your code here
    min_length = 0
    t_ascii = [ord(x) for x in t]
    s_ascii = [ord(x) for x in s]
    indices = []
    for x in t_ascii:
        if x not in s_ascii:
            return -1
        indices.append(s_ascii.index(x))
        s_ascii[s_ascii.index(x)]=  -1

    return max(indices) - min(indices) + 1











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    # Add your own test cases here
  