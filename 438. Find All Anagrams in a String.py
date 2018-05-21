"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(s)<len(p):
            return ret
        from collections import Counter
        counter = Counter(p)
        print(counter)
        for index,value in enumerate(s):
            if index > len(s)-len(p):
                break
            print(value,s[index:index+len(p)])
            if value in counter:
                if counter == Counter(s[index:index+len(p)]):
                    ret.append(index)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams('abceabdcba','abc'))