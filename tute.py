# stem argumente

# for i in range(0, 11, 2):  # for odd no.
#     print(i)


# for i in range(1, 11, 2):  # for even no.
#     print(i)

# for i in range(10, -1, -1):  # for odd no.
#     print(i)

# num = input("enter a number: ")
# total = 0
# for i in num:
#     total += int(i)
#     print(total)

# todo: function

# def add_num(a, b):
#     return a+b


# addition = add_num(56, 5)
# print(addition)

# home_num = int(input("enter your home number : "))
# age = int(input("enter you'r age : "))

# output = add_num(home_num, age)
# print(output)


# todo:odd_even

# def add_tow(a, b):
#     return a + b


# fristname = str(input("enter your frist name : "))
# lastname = str(input("enter your last name : "))
# output = add_tow(fristname, lastname)
# print(output)

#  for in range

# ........gratest.....


# def gretest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# # ans = gretest(10, 50, 9)
# # print(ans)


# def greater(a, b):
#     if a > b:
#         return a
#     return b

# # # ..........exc..self.


# def new_greatest(a, b, c):
#     bigger = greater(a, b)
#     return greater(bigger, c)


# print(new_greatest(100, 33, 50))


# # todo:fabnacci  series....self.
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a,b, end=" ")
#         for i in range(n - 2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end=" ")


# fibonacci(10)

#  todo...list in python....

# number = [1, 2, 3, 1, 2, 5, 6, ]
# print(number[0])

# words = ["suraj", "sony", "moni"]
# print(words[::-1])

# mixed = [1, 2, "suraj", 5.5, None]
# print(mixed[-1])

# todo............add in list .....

# name = ["apple", "graps"]
# name.append("banana")
# print(name)


# frouit = ["mango", "apple", "banana"]
# name = ["suraj", "sony", "mony"]
# # frouit.extend(name)
# frouit.append(name)
# print(frouit)
# print(name)


# todo....pop,push,remove...

# frouit = ["mango", "apple", "banana"]
# # frouit.pop()
# frouit.remove("apple")
# print(frouit)


# frouit = ["mango", "apple", "banana"]

# if "aple" in frouit:
#     print('apple is presetn in list')
# else:
#     print('apple is not here')

# todo..count,short method, shorted,reverse,clear,copy

# frouit = ["mango", "apple", "banana", "kiwi", "orenge", "pear", "apple"]
# counting = frouit.count("apple")
# frouit.sort()
# frouit.reverse()
# frouit.clear()
# frout_copy = frouit.copy()

# print(frouit)


# matrix = [[1, 2, 2], [2, 10, 500], [85, 985, 75555]]
# mat = matrix[2][0]
# print(mat)


# todo:  reverse to string inlist

# def reverse_element(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#         return elements

# words = ['suraj', 'sony', 'mona']
# print(reverse_element(words))


# todo filter odd even number in list in side list

# def filter_odd_even(l):
#     odd_nums = []
#     even_nums = []
#     for i in l:
#         if i % 2 == 0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output = [odd_nums, even_nums]
#     return output

# nums = [1, 2, 3, 4, 4, 5, 8]
# print(filter_odd_even(nums))


# todo....common_finder
# def common_finder(l1, l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#         return output


# print(common_finder([1, 2, 3], [1, 2, 5, 8]))

# todo...gretest minus min..self.
#  numbers=[50,52,556,100,200]
# def gretest_number(l):
#     return max(l) - min(l)

# output = gretest_number(numbers)
# print(output)


# todo...<list counters....>

# def counters_sublist(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count


# output = [[50, 52], [5, 56], [10, 0], [20, 0]]
# print(counters_sublist(output))

# todo min  and max number

# number = [2, 5, 56, 6, 8, 9]

# print(min(number))
# print(max(number))


# def gretest_diff(l):
#     return max(l) - min(l)


# print(gretest_diff(number)
import os

with open('my_words.txt') as infile:
    words = 0
    characters = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)

print(lineno)
print(words)
print(characters)














