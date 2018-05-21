class Solution:
    #进一步优化思路，控制4个边界变量，以及在1还是在2中的flag
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        Xth = len(nums1) + len(nums2)
        if Xth/2 == Xth//2:
            return (self.findXthSortedArrarys(nums1,nums2,Xth//2) + self.findXthSortedArrarys(nums1,nums2,Xth//2+1))/2
        else:
            return self.findXthSortedArrarys(nums1,nums2,Xth//2+1)
        
    def findXthSortedArrarys(self,nums1,nums2,Xth = None):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if Xth > len(nums1)+len(nums2):
            return -1
        to_drop_num = min(Xth//2,len(nums1),len(nums2))
        to_drop_index = to_drop_num -1
        if Xth == 1:
            if min(len(nums1),len(nums2)) == 0:
                return (nums1 + nums2)[0]
            else:
                return nums1[0] if nums1[0] < nums2[0] else nums2[0]
        if to_drop_num == 0:
            return (nums1 + nums2)[Xth-1]
        a = nums1[to_drop_index]
        b = nums2[to_drop_index]
        if a == b and Xth <= 2:
            return a
        if a < b:
            return self.findXthSortedArrarys(nums1[to_drop_index+1:],nums2,Xth - to_drop_num)
        else:
            return self.findXthSortedArrarys(nums1,nums2[to_drop_index+1:],Xth - to_drop_num)


def main():
    s = Solution()

    # nums1 = [1,3,4,5,6]
    # nums1 = [1,2,3]
    nums1 = [1,2]
    nums2 = [1,2]
    # print(s.findMedianSortedArrays(nums1,nums2))
    # print('*****************************')

    print(s.findXthSortedArrarys(nums1,nums2,2))
    print(s.findXthSortedArrarys(nums1,nums2,4))

if __name__ == '__main__':
    main()