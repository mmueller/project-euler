#!/usr/bin/env python

# Find the maximum total from top to bottom of the triangle below:

def traverse(triangle, row, col):
    if row == len(triangle) - 1:
        return triangle[row][col]
    else:
        return triangle[row][col] + \
                max(traverse(triangle, row+1, col),
                    traverse(triangle, row+1, col+1))

input = []
for line in file("inputs/p18.txt", "r"):
    input.append(map(int, line.split(" ")))
print traverse(input, 0, 0)
