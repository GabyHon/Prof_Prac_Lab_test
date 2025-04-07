#!/usr/bin/env python3

import sys

''' Identify the columns that contain the marks and student numbers '''
def getCols(f):
    headings = f.readline().strip().split(",")
    i = 1
    for head in headings:
        if head == "Student Number": num_col = i
        elif head == "Mark" : mark_col = i
    return num_col, mark_col

''' Finds the top student in the class '''
# Assuming all marks are distinct
def findTop(f,num_col, mark_col):
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
          best = mark
          best_idx += 1
    return best_idx, best

# Run the test
if __name__ == '__main__':
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f,num_col,mark_col)
    print("The top student was student %s with %d"%(best, best_idx))
