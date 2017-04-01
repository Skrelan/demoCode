class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I' : 1,
                'V' : 5,
                'X' : 10,
                'L': 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000}
        nums = []
        for digit in s:
            nums.append(dict[digit])
        print nums
        current = nums[0]
        sums = nums[0]
        for i in range(1,len(nums)):
            if current < nums[i]:
                
                sums = sums + nums[i]
                sums = sums - current - current 
            else:
                print "there", nums[i]
                sums = sums + nums[i]
            
            current = nums[i]
        return sums

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MCMXII')