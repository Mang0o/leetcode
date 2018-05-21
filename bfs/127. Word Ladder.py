"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def distance(str1,str2):
            ret = 0
            if len(str1) != len(str2):
                print(str1,str2)
                assert False
            for i in range(len(str1)):
                if str1[i]!=str2[i]:
                    ret+=1
            return ret
        from queue import Queue
        q = Queue()
        q.put((beginWord,1))

        used_str = set([])
        can_use_set = set(wordList)
        if endWord in can_use_set:
            while (not q.empty()):
                s,level = q.get()
                if s == endWord:
                    return level
                for i in can_use_set:
                    if distance(i,s) == 1:
                        q.put((i,level+1))
                        used_str.add(i)
                can_use_set = can_use_set - used_str

        return 0

if __name__ == '__main__':
    s = Solution()
    

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(s.ladderLength(beginWord,endWord,wordList))
