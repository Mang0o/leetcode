"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
# class Solution:
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         ret = 0
#         num_of_1 = 0
        
#         tmp = num
#         while (tmp):
#             if tmp&1:
#                 num_of_1+=1
#             tmp = tmp>>1
        
#         tmp = num
#         bit_of_high_1 = 0
#         new_num_of_1 = 0
#         while (tmp):
#             bit_of_high_1+=1
#             if tmp&1:
#                 new_num_of_1+=1
#                 tmp2 = (bit_of_high_1-1)*(2**(bit_of_high_1-1-1))+(num_of_1-new_num_of_1)*2**(bit_of_high_1-1)
#                 ret+= tmp2
#             tmp = tmp>>1

#         return int(ret+num_of_1)

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret,length = [0,1],2
        while(length<num+1):
            length*=2
            ret = ret+[i+1 for i in ret]
        return ret[:num+1]

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(9))
