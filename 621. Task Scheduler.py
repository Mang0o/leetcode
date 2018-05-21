"""Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from queue import PriorityQueue
        from collections import Counter
        q = PriorityQueue()
        for k,v in Counter(tasks).items():
            q.put(tuple((-v,k)))

        count = 0
        while(not q.empty()):
            length = n + 1
            tmp_list = []
            while ((not q.empty()) and length>0):
                value = q.get()
                tmp_list.append(tuple((value[0]+1,value[1])))
                length-=1
                count+=1
            for i in tmp_list:
                if i[0] < 0:
                    q.put(i)

            if length and (not q.empty()) > 0:
                count+=length
        return count

if __name__ == '__main__':
    
    s = Solution()
    r = s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)
    print(r)
