"""days"""

import numpy as np

# Theory

# Creating arrays

# From Python lists
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# Special arrays
zeros = np.zeros((2, 3))  # 2 rows, 3 columns
print(zeros)
ones = np.ones((3, 3))
print(ones)
rand = np.random.rand(2, 2)
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8] uses step size
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1] uses number of steps

# Array indexing and slicing

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0, 1])   # 20
print(arr[:, 1])   # all rows, 2nd column → [20, 50, 80]
print(arr[1:, :2]) # from 2nd row, first 2 columns

# Vectorized Operations (increased performance)

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)      # [11, 22, 33]
print(x * y)      # [10, 40, 90]
print(x ** 2)     # [1, 4, 9]
print(np.exp(x))  # [2.718, 7.389, 20.085]

# Broadcasting (auto match shapes for compatible operations)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])

print(a + b)
# [[11, 22, 33],
#  [14, 25, 36]]

# Dot Product (The Core of ML Math).
# Sum of elementwise multiplication of two vectors.
# In linear algebra → used for matrix multiplication, projections,
# neural network (NN) activations, etc.
# Dot products: linear regression, cosine similarity, NN forward pass.

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

dot = np.dot(u, v)    # 1*4 + 2*5 + 3*6 = 32
print(dot)

# For matrices
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

C = np.dot(A, B)
print(C)
# [[19, 22],
#  [43, 50]]

# Practice

def manual_dot (vector_a: list[int], vector_b: list[int]) -> int:
    '''
    Return the dot product of 2 vectors of same length

    Args:
        vector_a (list[int]): A list of integers
        vector_a (list[int]): A list of integers

    Returns:
        int: A dot product of 2 vectors

    Complexity:
        Time: O(n)
        Space: O(1)
        '''
    assert len(vector_a) == len(vector_b), "Vectors of different lengths!"

    sum_manual = 0
    for i, number in enumerate(vector_a):
        sum_manual += number * vector_b[i]
    return sum_manual


def matrix_multiplication(
        matrix_a: list[list[int]], matrix_b: list[list[int]]
) -> list[list[int]]:
    '''
    Return the product of 2 matrices multiplication

    Args:
        matrix_a (list[list[int]]): A matrix of integers
        vector_a (list[list[int]]): A matrix of integers

    Returns:
        int: A dot product of 2 vectors

    Complexity:
        Time: O(n)
        Space: O(1)
        '''
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    assert cols_a == rows_b, "Inconpatible matrix sizes"

    matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_c


x = [1, 2, 3]
y = [4, 5, 6]
print("Manual:", manual_dot(x, y))
print("NumPy:", np.dot(x, y))

matrix_A = [
    [1, 2],
    [3, 4]
]
matrix_B = [
    [1, 2, 3],
    [4, 5, 6],
]
print("Manual:", matrix_multiplication(matrix_A, matrix_B))
print("NumPy:", np.dot(matrix_A, matrix_B))

# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def is_valid(s: str) -> bool:
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '['
    and ']', determines if the input string is valid.
    '''
    if len(s) % 2:
        return False
    brackets: dict[str, int] = {
        "(": 0,
        "{": 0,
        "[": 0,
    }
    complement_brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    pointer = -1
    bracket_list: list[str] = []
    for bracket in s:
        if bracket in ["(", "{", "["]:
            brackets[bracket] += 1
            pointer += 1
            bracket_list.append(bracket)
        else:
            complement_bracket = complement_brackets[bracket]
            brackets[complement_bracket] -= 1
            if brackets[complement_bracket] < 0:
                return False
            if complement_bracket != bracket_list[pointer]:
                return False
            pointer -=1
            bracket_list.pop()
    if sum(v ** 2 for v in brackets.values()) != 0:
        return False
    return True


def is_valid_v2(s: str) -> bool:
    '''
    Given a string s containing just the characters '(', ')', '{', '}', '['
    and ']', determines if the input string is valid.
    '''
    if len(s) % 2:
        return False
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    opens = pairs.values()
    stack: list[str] = []
    for bracket in s:
        if bracket in opens:
            stack.append(bracket)
        else:
            if not stack or stack.pop() != pairs[bracket]:
                return False
    return not stack
print(is_valid("[([]])"))
