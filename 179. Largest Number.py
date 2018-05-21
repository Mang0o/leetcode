class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        def cmp(a,b):
            tmp_a = a+b
            tmp_b = b+a
            for i in range(len(tmp_a)):
                if tmp_a[i]==tmp_b[i]:
                    continue
                else:
                    return 1 if tmp_a[i]>tmp_b[i] else -1
            return 1

        l = [str(i) for i in nums]
        l.sort(key = cmp_to_key(cmp),reverse=True)
        return ''.join(l)

if __name__ == '__main__':
    s = Solution()
    nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
    print(s.largestNumber(nums))