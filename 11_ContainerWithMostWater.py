 
class Solution(object):
    #啊啊啊啊，理解错题意版，以为是木桶理论
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        for i in height:
            # print('============================',i,stack,max_area)
            if len(stack) == 0 or stack[-1] <= i:
                stack.append(i)
            else:
                max_right = stack.pop()
                max_area = max(max_area,1*i)
                num = 1
                while(len(stack) > 0 and stack[-1] >= i):
                    # print('&&&&&&====',i,stack,max_area)

                    new_area = stack.pop()*num
                    # print('hahaha====',new_area,i*(num+1))
                    max_area = max(max_area,new_area,i*(num+1))
                    num+=1
                for j in range(num+1):
                    stack.append(i)
        
        # print('***********************************',stack,num)
        if len(stack) > 0:
            stack.pop()
            num = 1
            while(len(stack) > 0):
                max_area = max(max_area,stack.pop()*num)
                num+=1

        return max_area

    def maxArea(self,nums):
        if (not nums) or len(nums) < 2:return 0
        ret = 0
        l,r = 0,len(nums)-1

        while (l<r):
            ret = max(ret,min(nums[l],nums[r])*(r-l))
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return ret



if __name__ == '__main__':
    s = Solution()
    # print(s.maxArea([3,2,1,3]))


    print(s.maxArea([10,14,10,4,10,2,6,1,6,12]))

