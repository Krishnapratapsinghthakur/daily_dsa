# Problem: Maximum Subarray (Kadane's Algorithm)
# Topic: Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/

# Solution:


def maximum_subarray(nums):
    max_sum=nums[0]
    current=0
    if len(nums)==1:
        return nums[0]
    for i in nums:
        current=max(current+i,i)
        if current>max_sum:
            max_sum=current
    return max_sum

a=[5,4,-1,7,8]
res=maximum_subarray(a)
print(res)
