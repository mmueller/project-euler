#!/usr/bin/env python

# Project Euler: Problem 11
#
# What is the greatest product of four numbers in any direction (up, down,
# left, right, or diagonally) in the 20x20 grid?

import array

def product(grid, width, height):
    """Return the greatest product of four numbers in the grid."""

    # Look for horizontal products
    products = []
    for row in range(0, height):
        for colStart in range(0, width-3):
            p = 1
            for i in range(0, 4):
                p *= grid[row*width+colStart+i]
            products.append(p)

    # Look for vertical products
    for col in range(0, width):
        for rowStart in range(0, height-3):
            p = 1
            for i in range(0, 4):
                p *= grid[(rowStart+i)*width+col]
            products.append(p)

    # Look for diagonal products
    for row in range(0, height-3):
        for col in range(0, width-3):
            p = 1
            for i in range(0, 4):
                p *= grid[(row+i)*width+col+i]
            products.append(p)

    for row in range(0, height-3):
        for col in range(3, width):
            p = 1
            for i in range(0, 4):
                p *= grid[(row-i)*width+col+i]
            products.append(p)

    return max(products)

# Read in the input file, create a big fat array
input = file("p11_input.txt", "r")
grid = array.array('i')
for line in input:
    poop = line.split(" ")
    grid.extend(map(int, poop))

# Do it
print product(grid, 20, 20)
