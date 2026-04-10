# Problem: Rotate Image (Matrix 90 Degrees)
# Topic: Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/

# Solution:


matrix=[[1,2,3],[4,5,6],[7,8,9]]

def rotate( matrix):
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        for i in range(len(matrix)-1):
            

            for j in range(i,len(matrix[i])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(len(matrix)-1):
            start=0
            end=len(matrix[i])-1

            for j in range(i,len(matrix[i])):
                 while start<end:
                      matrix[i][start],matrix[i][end]=matrix[i][end],matrix[i][start]
                      start+=1
                      end-=1
                  
        print(matrix)    

rotate(matrix=matrix)
                  
                  
                
        
        
