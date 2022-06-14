#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


# long solution

def diagonalDifference(arr):
    

    left_to_right = 0
    right_to_left = 0
    result_sum = 0;
    
    for i in range (n):
        
        print("arr[i][i] = ", arr[i][i])
        left_to_right+=arr[i][i]
    
    for j in range (n):
        
        for k in range(n-1-j, -1, -1):
            
            right_to_left+=arr[j][k]
        
            #print("right_to_left = ",  right_to_left)
            print("arr[j][k] = ",  arr[j][k])
            
            break
        
    result_sum = abs(left_to_right-right_to_left) 
    
    return result_sum

# short solution
    '''
def diagonalDifference(arr):

    diagonal1 = sum(arr[x][x] for x in range(n))
    diagonal2= sum(arr[x][n-1-x] for x in range(n))
    return abs(diagonal1-diagonal2)
    '''
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
