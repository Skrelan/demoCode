class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        sum = 0
        carry = 0
        value = 0
        
        if  len(a)>=len(b):
            bigger = a
            smaller = b
        else:
            bigger = b
            smaller = a
        b_len = len(bigger)-1
        s_len = len(smaller)-1
        for i in xrange(0,len(bigger)):
            if i < len(smaller):
                sum = int(bigger[b_len-i]) + int(smaller[s_len-i]) + carry
            else:
                sum = int(bigger[b_len-i]) + carry
            if sum < 2:
                carry = 0
                value = sum
                
            elif sum == 2:
                carry = 1
                value = 0
            else:
                carry = 1
                value = 1
            result = result + str(value)

        if carry == 1:
            value = str(1)
            result = result + value
        return result[::-1]
        

if __name__ == "__main__":
    s = Solution()
    print s. addBinary('1','11')         