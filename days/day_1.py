"""days"""

import re
from collections import Counter
from typing import Optional

# Theory

# Lists

numbers = [1, 2, 3, 4, 5]
words = ["ML", "AI", "Data"]

# Access
print(numbers[0])      # 1
print(words[-1])       # "Data"

# Modify
numbers[2] = 99        # [1, 2, 99, 4, 5]

# Add / Remove
numbers.append(6)      # [1, 2, 99, 4, 5, 6]
numbers.pop()          # removes last → [1, 2, 99, 4, 5]

# List comprehension
squared_numbers = [x**2 for x in numbers]   # [1, 4, 9801, 16, 25]

# Dictionaries

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Access
print(scores["Alice"])     # 95

# Add / Modify
scores["Diana"] = 88
scores["Alice"] = 99

# Remove
scores.pop("Bob")

# Iterate
for name, score in scores.items():
    print(name, score)

# Sets

unique_nums = {1, 2, 2, 3, 4}  # pylint: disable=duplicate-value
print(unique_nums)        # {1, 2, 3, 4}

# Add / Remove
unique_nums.add(5)
unique_nums.remove(2)

# Operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # Union → {1, 2, 3, 4, 5}
print(A & B)   # Intersection → {3}
print(A - B)   # Difference → {1, 2}

# Practice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = {num: num**2 for num in numbers}
print(squares)

even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)

for n, square in squares.items():
    if n > 5:
        print(n, square)

TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
cleaned_text = re.sub(r"[^a-zA-ZÀ-ÿ0-9'\s-]", "", TEXT.lower()).split()
frequencies = Counter(cleaned_text)
print(frequencies)

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9. Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6. Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6. Output: [0,1]

def two_sum(nums: list[int], target: int) -> Optional[list[int]]:
    '''
    Return the indices of the two numbers that add up to the target.

    This function finds two distinct indices i and j in the input list `nums`
    such that nums[i] + nums[j] == target. It uses a hash map to achieve
    O(n) time complexity by storing numbers and their indices as they are
    iterated over.

    Args:
        nums (list[int]): A list of integers to search through.
        target (int): The target sum to find.

    Returns:
        list[int]: A list containing the two indices [i, j] where
            nums[i] + nums[j] == target. The order of indices is [first, second]
            where the first index corresponds to the earlier element in `nums`.

    Complexity:
        Time: O(n)
        Space: O(n)
    '''
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
print(two_sum(nums=[2, 7, 11, 15], target=9))
