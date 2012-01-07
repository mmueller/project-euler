#!/usr/bin/env python

import array

cache = { }
def explore(row, col):
    global width, height, cache

    # see if this is the goal
    if row == height-1 and col == width-1:
        return 1

    # see if we've been here before
    rowDistance = height - row
    colDistance = width - col
    if (rowDistance,colDistance) in cache:
        return cache[(rowDistance,colDistance)]

    # try right
    result = 0
    if col < width-1:
        result += explore(row,col+1)

    # try down
    if row < height-1:
        result += explore(row+1,col)

    cache[(rowDistance,colDistance)] = result
    return result

width = 1
height = 1
for i in range(1,22):
    width = i
    height = i
    found = explore(0,0)
    print "size", i, "found", found, "paths"
