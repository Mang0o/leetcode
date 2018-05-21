"""
301. Remove Invalid Parentheses
DescriptionHintsSubmissionsDiscussSolution
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        def isValid(string):
            stack = 0
            for i in string:
                if i=="(":stack+=1
                if i==")":stack-=1
                if stack<0:
                    return False
            return stack==0
        
        ret = []
        process_set = set([])
        from queue import Queue
        q = Queue()
        q.put(s)
        process_set.add(s)
        
        found_flag = False
        while(not q.empty()):
            tmp_str = q.get()
            if (isValid(tmp_str)):
                ret.append(tmp_str)
                found_flag = True
            if found_flag:
                continue
            for i in range(0,len(tmp_str)):
                if (tmp_str[i] != ")") and (tmp_str[i] != "("):
                    continue
                new_str = tmp_str[:i]+tmp_str[i+1:]
                if new_str not in process_set:
                    q.put(new_str)
                    process_set.add(new_str)
        
        
        return ret

if __name__ == '__main__':
    s = Solution()
    st = "()())()"
    print(s.removeInvalidParentheses(st))
