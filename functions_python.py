# def for define function

def say_whatup(name, emoji):
    print(f'whattupppppp {name} {emoji}')

# say_whatup('cory', ':)')

# rule: params, *args, default parameters, *kwargs

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

# iterate over picture
# if it is a zero, print an empty space ' ',
# if it is a 1, print a star '*'

# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print('*', end='')
#         if pixel == 0:
#             print(' ', end='')
#     print('')

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list

# print(multiply_by2([2, 4, 6]))

# map -- transforms the items in a list, but returns the same exact number of items 


my_list = [5, 6, 7]

# def multiply_by_two(item):
#     return item * 2
# print(list(map(multiply_by_two, my_list)))

# print(my_list)

# filter -- search, receives a true or false boolean value

# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))


# Zip -- works like a zipper, takes two iteratable things (lists, tuples) and merges them together

your_list = [10, 20, 30]

# print(list(zip(my_list, your_list)))

# #reduce -- accumulate

from functools import reduce

# functools are a toolkit that we can use for functional tools that come with python installation

a_new_list = [1, 2, 3]

def accumulator(acc, item):
    print(acc, item)
    # 0 + 1 = 1
    # 1 + 2 = 3
    # 3 + 3 = 6
    return acc + item

# print(reduce(accumulator, a_new_list, 0))

# Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# my_sorted_numbers = my_numbers.reverse()

# print(list(zip(my_strings, sorted(my_numbers))))

# Filter the scores that pass over 50

scores = [73, 20, 65, 19, 76, 100, 88]

def over_fifty(x):
    if x > 50:
        return True

# print(list(filter(over_fifty, scores)))

# LAMBDA expression
# CS term for a one-time anonymous function that you don't use more than once

our_list = [7, 8, 9]

# print(list(map(lambda item: item *3, our_list)))

# print(list(map(lambda item: filter(item % 2 != 0, our_list), our_list)))

# List comprehension

wow_list = [char for char in 'hello']

print(wow_list)

# range of 0 - 100

wow_list2 = [num for num in range(0, 100)]

print(wow_list2)

wow_list3 = [num*3 for num in range(0, 33)]

print(wow_list3)

wow_list4 = [num*3 for num in range(0, 33) if num % 2 == 0]

print(wow_list4)