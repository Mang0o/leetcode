"""

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

"""
import collections



class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
        	return 0
        count = collections.Counter(s)
        before = 0
        result = 0
        for i in range(len(s) + 1):
        	if i == len(s) and before == 0:
        		return len(s)
        	if i == len(s) or count[s[i]] < k:
        		current = s[before: i]
        		if current:
        			result = max(result, self.longestSubstring(current, k))
        		before = i + 1
        return result


    def longestSubstring_v2(self, s, k):
	        """
	        :type s: str
	        :type k: int
	        :rtype: int
	        """
	        
	        if len(s) < k:
	        	return 0

	        del_char = set()
	        for i,v in collections.Counter(s).items():
	            if v < k:
	                del_char.add(i)
	        
	        if len(del_char) == 0:
	            return len(s)

	        new_s = ''.join([i if i not in del_char else ' ' for i in s])

	        max_length = 0
	        for i in new_s.split():
	            max_length = max(max_length,self.longestSubstring_v2(i,k))

	        return max_length

# print(collections.Counter([1,2, 1]))
# print(Solution().longestSubstring('weitong', 2))
print(Solution().longestSubstring('bbaaacbd', 3))


# def process_string(string, pos):
#  result = []
#  before = 0
#  pos = set(pos)
#  for i in range(len(string) + 1):
#   if (i in pos) or (i == len(string)):
#    current = string[before:i]
#    if current:
#     result.append(current)
#    before = i + 1
#  return result

# print(process_string('ababacb', [0,2,3,4]))
        

