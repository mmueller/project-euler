#!/usr/bin/env python

"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in p67_input.txt, a 15K text file
containing a triangle with one-hundred rows.
"""

# Memoized version of the p18 algorithm. Boom.
results = {}
def traverse(triangle, row, col):
    global results
    if (row, col) in results:
        return results[(row, col)]
    if row == len(triangle) - 1:
        results[(row, col)] = triangle[row][col]
        return triangle[row][col]
    else:
        result = triangle[row][col] + \
                max(traverse(triangle, row+1, col),
                    traverse(triangle, row+1, col+1))
        results[(row, col)] = result
        return result

if __name__ == '__main__':
    input = []
    for line in file("inputs/p67.txt", "r"):
        input.append(map(int, line.split(" ")))
    print traverse(input, 0, 0)
