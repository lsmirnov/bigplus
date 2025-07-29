"""Chapter 1 Combinatorial Analysis"""

from math import comb as c, factorial as f

# Problem 5

# A safe can be opened by inserting a code consisting of three digits
# between 0 and 9.
# a) How many codes are possible?
# b) How many codes are possible with no digit repeated?
# c) How many codes starting with a 1 are possible?

print(f"Problem 5a: {10**3}, 5b: {10 * 9 * 8}, 5c: {10**2}")
# 5a: 1000, 5b: 720, 5c: 100

# Problem 12

# a) How many 3 digit numbers xyz, with x, y, z all ranging from 0 to 9
# have at least 2 of their digits equal?
# b) How many have exactly 2 equal digits?

print(f"Problem 12a: {10**3 - 10 * 9 * 8}, 12b: {10**3 - 10 * 9 * 8 - 10}")
# 12a: 280, 12b: 270

# Problem 20

# A team of 9, consisting of 2 mathematicians, 3 statisticians,
# and 4 physicists, is to be selected from a faculty of 10 mathematicians,
# 8 statisticians, and 7 physicists.
# How many teams are possible?

print(f"Problem 20: {c(10, 2) * c(8, 3) * c(7, 4)}")
# 88200

# Problem 22

# A person has 8 friends, of whom 5 will be invited to aparty.
# a) How many choices are there if 2 of the friends are feuding
# and will not attend together?
# b) How many choices if 2 of the friends will only attend together?
# DON'T FORGET ABOUT A CASE WITH NONE OF THE TWO ATTENDING

print(f"Problem 22a: {2 * c(6, 4) + 6}, 22b: {c(6, 3) + 6}")
# 22a: 36, 22b: 26

# Problem 23

# Consider the grid of points shown at the top of the next column.
# Suppose that, starting at the point labeled A, you can go one step up
# or one step to the right at each move.
# This procedure is continued until the point labeled B is reached.
# How many different paths from A to B are possible?

print(f"Problem 23: {c(4 + 3, 3)}")
# 35

# Problem 24

# In Problem 23, how many different paths are there from A to B
# that go through the point circled in the following lattice?

print(f"Problem 24: {c(2 + 2, 2) + c(2 + 1, 1)}")
# 9

# Problem 31

# a) If 10 gifts are to be distributed among 3 friends,
# how many distributions are possible?
# b) What if each friend should receive at least 3 gifts?

print(f"Problem 31a: {c(10 + 3 - 1, 3 - 1)}, 31b: {c(10 - 9 + 3 - 1, 2)}")
# 31a: 66, 31b: 3

# Problem 32

# Ten weight lifters are competing in a team weight-lifting contest.
# Of the lifters, 3 are from the United States, 4 are from Russia,
# 2 are from China, and 1 is from Canada.
# a) If the scoring takes account of the countries that the lifters represent,
# but not their individual identities, how many different outcomes are possible
# from the point of view of scores?
# b) How many different outcomes correspond to results in which
# the United States has 1 competitor in the top three and 2 in the bottom three?

print(
    f"Problem 32a: {f(10) // (f(3) * f(4) * f(2) * f(1))}, "
    f"32b: {c(3, 1) * c(3, 2) * f(7) // (f(4) * f(2) * f(1))}"
)
# 32a: 12600, 32b: 945

# Problem 34

# a) If 8 identical blackboards are to be divided among 4 schools,
# how many divisions are possible?
# b) How many if each school must receive at least 1 blackboard?

print(f"Problem 34a: {c(8 + 4 - 1, 4 - 1)}, 34b: {c(8 - 1, 4 - 1)}")
# 34a: 165, 34b: 35

# Problem 36

# We have $20,000 that must be invested among 4 possible opportunities.
# Each investment must be integral in units of $1000, and there are minimal
# investments that need to be made if one is to invest in these opportunities.
# The minimal investments are $2000, $2000, $3000, and $4000.

# How many different investment strategies areavailable if
# (a) an investment must be made in each opportunity?
# (b) investments must be made in at least 3 of the 4 opportunities?
# DON'T FORGET ABOUT A CASE WITH ALL FOUR

a = c(20 - 11 + 4 - 1, 4 - 1)
b = (
    c(20 - 11 + 4 - 1, 4 - 1)
    + c(20 - 9 + 3 - 1, 3 - 1) * 2
    + c(20 - 8 + 3 - 1, 3 - 1)
    + c(20 - 7 + 3 - 1, 2)
)
print(f"Problem 36a: {a}, 36b: {b}")
# 36a: 220, 36b: 572
