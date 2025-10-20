"""days"""

from typing import Optional, Union

import pandas as pd

# Theory

# Create a DataFrame
data: dict[str, list[Union[str, int]]] = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 32, 18],
    "Score": [88, 92, 95]
}
df = pd.DataFrame(data)
print(df)

# Importing & Inspecting Data
titanic = pd.read_csv("data/titanic.csv")

df.head()  # first 5 rows
df.tail(3)  # last 3 rows
print(df.shape)  # (rows, columns)
print(df.columns)  # list of column names
df.info()  # data types, non-null counts
df.describe()  # summary stats for numeric cols

# Selecting Data
print(df["Name"])
print(df[["Name", "Age"]])

print(df.iloc[0])  # first row (by index position)
print(df.loc[1])  # row with label/index 1

print(df.iloc[:2, :2])  # first 2 rows, first 2 columns

# Filtering Rows
adults = df[df["Age"] >= 21]
print(adults)

young_highscore = df[(df["Age"] < 30) & (df["Score"] > 90)]
print(young_highscore)

# Adding / Modifying Columns
df["Passed"] = df["Score"] > 90
df["Score2x"] = df["Score"] * 2

# Sorting, Aggregating, and Grouping
df.sort_values(by="Score", ascending=False)
df["Score"].mean()
df["Age"].max()
df.groupby("Passed")["Age"].mean()

# Handling Missing Data
df.isnull().sum()  # count missing per column
df.fillna(0, inplace=True)  # replace NaN with 0
df.dropna(subset=["Age"], inplace=True)  # drop rows missing Age

# Mini Hands-on (Titanic Dataset)
df = pd.read_csv("data/titanic.csv")
print(df.shape)
print(df.columns)
print(df.describe())

adults = df[df["Age"] >= 18]
print("Adults count:", len(adults))

survival_rate = df.groupby("Sex")["Survived"].mean()
print(survival_rate)

# Practice
df["Child"] = df["Age"] < 18
survival_rate = df.groupby("Child")["Survived"].mean()
print(survival_rate)
print(df[df["Survived"] == 1].sort_values(by="Age").head())

# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made
# by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


class ListNode:
    """
    A linked list
    """
    def __init__(self, val: int = 0, next_val: Optional["ListNode"] = None):
        self.val = val
        self.next_val = next_val


def merge_two_lists(
    list1: Optional[ListNode],
    list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Merges the two sorted linked lists into one sorted linked list

    Args:
        list1: A linked list
        list2: A linked list

    Returns:
        A merged sorted linked list

    Complexity:
        Time: O(n+m)
        Space: O(1)
    """
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next_val = list1
            list1 = list1.next_val
        else:
            tail.next_val = list2
            list2 = list2.next_val
        tail = tail.next_val
    return dummy.next_val


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    """
    Builds a linked list out of list[int]

    Args:
        values: a list of integers

    Returns:
        A linked list

    Complexity:
        Time: O(n)
        Space: O(n)

    """
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next_val = ListNode(v)
        tail = tail.next_val
    return dummy.next_val
