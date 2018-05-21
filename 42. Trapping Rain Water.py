"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        
        my_height = []
        walls_volumne = 0
        
        for i in height:
            if not my_height:
                my_height.append(i)
            else:
                my_height.append(max(i,my_height[-1]))
            walls_volumne+=i
        print(my_height)
        print(height)
        for i in range(len(height)-1,-1,-1):
            if i < len(height)-1:
                my_height[i] = min(my_height[i],max(my_height[i+1],height[i]))
            else:
                my_height[i] = min(my_height[i],height[i])
        print(my_height)
        if my_height:
            ret = sum(my_height) - walls_volumne

        return ret


if __name__ == '__main__':
    s = Solution()
    s.trap([4,2,3])
