# Problem: Sort Colors (Sort 0, 1, 2)
# Topic: Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-colors/

# Solution:

def shor012(nums):
    high=len(nums)-1
    low=0
    mid=0

    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        
        elif nums[mid]==1:
            # nums[mid],nums[low]=nums[low],nums[mid]
            # low+=1
            mid+=1
        elif nums[mid]==0:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1


        


