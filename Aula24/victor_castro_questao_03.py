#!/usr/bin/python
# -*- coding: utf-8 -*-

array = 1
array_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
array_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
new_array = []

for i in range(len(array_1) + len(array_2)):
    if array:
        new_array.append(array_1[int(i / 2)])
        array = 0
    else:
        new_array.append(array_2[int(i / 2)])
        array = 1

print(new_array)
