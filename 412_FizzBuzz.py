class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [str(i) if (i%3!=0 and i%5!=0) else ('FizzBuzz' if (i%15==0) else ("Fizz" if i%3 == 0 else 'Buzz')) for i in range(1,n+1,1)]

if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))