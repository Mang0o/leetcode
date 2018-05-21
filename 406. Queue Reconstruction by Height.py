"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

import itertools
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
        for k, g in itertools.groupby(sorted(people, reverse=True), key=lambda x: x[0]):
            
            for person in sorted(g):
                res.insert(person[1], person)
                print(res)
        return res

if __name__ == '__main__':
    s = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(sorted(people, reverse=True))

    for k,g in itertools.groupby(sorted(people, reverse=True), key=lambda x: x[0]):
        print(k,sorted(list(g)))

    print(s.reconstructQueue(people))

    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
