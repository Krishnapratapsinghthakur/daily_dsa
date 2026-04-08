# Problem: Next Permutation
# Topic: Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/next-permutation/

# Solution:


def nextPermutation( nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                pivot=i
                break
        if pivot != -1:
            for i in range(n-1,pivot,-1):
                if(nums[i]>nums[pivot]):
                    nums[pivot],nums[i]=nums[i],nums[pivot]
                    break

        left,right=pivot+1,n-1
        while(left<right):
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

        return nums

arr=[1,2,3]
arr=nextPermutation(arr)
print(arr)




