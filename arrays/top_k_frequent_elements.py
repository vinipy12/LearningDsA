"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    hashmap = {}
    answer = []
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    for number, count in hashmap.items():
        if count >= k:
            answer.append(number)
    return answer

nums = [1,1,1,2,2,3] 
k = 2
topKFrequent(nums, k)