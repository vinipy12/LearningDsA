"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def isAnagram(s: str, t: str) -> bool:
    hashmap_s = {}
    hashmap_t = {}

    for ch in s:
        if hashmap_s.get(ch):
            hashmap_s[ch] += 1
        else:
            hashmap_s[ch] = 1
    
    for ch in t:
        if hashmap_s.get(ch):
            hashmap_t[ch] += 1
        else:
            hashmap_t[ch] = 1

    return hashmap_t == hashmap_s
