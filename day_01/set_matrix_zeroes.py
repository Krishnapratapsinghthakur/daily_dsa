# Problem: Set Matrix Zeroes
# Topic: Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/

# Solution:

import copy

matrix = [[1,1,1],[1,0,1],[1,1,1]]
newmatrix=copy.deepcopy(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j]==0):
            if(i!=0):
                newmatrix[i-1][j]=0
            if(i!=len(matrix)-1):
                newmatrix[i+1][j]=0
            if(j!=0):
                newmatrix[i][j-1]=0
            if(j!=len(matrix[i])-1):
                newmatrix[i][j+1]=0
            
print(newmatrix)
