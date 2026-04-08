# Problem: Pascal's Triangle
# Topic: Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/pascals-triangle/

# Solution:

mainli=[]

for i in range(1,6):
    li=[]
    for j in range(i):
        li.append(0)
    mainli.append(li)
print(mainli)
    
for i in range(len(mainli)):

    for j in range(len(mainli[i])):
        if(j==0 or j==len(mainli[i])-1):
            mainli[i][j]=1
        else :
            mainli[i][j]=mainli[i-1][j-1]+mainli[i-1][j]

print(mainli)

def pascal_tringle(n):
    mainlist=[]
    for i in range(1,n+1):
        if(len(mainlist)!=0):
            prevrow=mainlist[len(mainlist)-1]
        row=[]
        for j in range(i):
            row.append(0)
            if(j==0 or j==i-1):
                row[j]=1
            else:
                row[j]=prevrow[j-1]+prevrow[j]
        mainlist.append(row)
    return mainlist
mainlist=pascal_tringle(5)
print(mainlist)

        
