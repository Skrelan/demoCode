from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.dic = {}
        for i in xrange(0,len(nums)):
            #dic[num[i]] = dic.get(num[i],[]).append(i)
            if self.dic.get(nums[i],None) == None:
                self.dic[nums[i]] = [i]
            else:
                holder = self.dic[nums[i]]
                holder.append(i)
                self.dic[nums[i]] = holder 
        print self.dic
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        x = self.dic[target]
        x = x[randint(0,len(x)-1)]
        return x

if __name__ == "__main__":
    s = Solution([0,1,2,3,3,3])
    print s.pick(3)                   