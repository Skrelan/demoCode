class Solution(object):

    def better_solution(self,matrix):
        if len(matrix) == 0:
            return 0
        result = 0
        holder = [[0]*(len(matrix)+1)]*(len(matrix)+1) 
        for i in xrange(1,len(matrix)+1):
            for j in xrange(1,len(matrix)+1):
                if int(matrix[i-1][j-1]) == 1:
                    holder[i][j] = min(holder[i-1][j],holder[i][j-1],holder[i-1][j-1]) + 1
                    result = max(result,holder[i][j]) 
        return result*result      

if __name__ == "__main__":
    s = Solution()
    print s. better_solution(["10100","10111","11111","10111"])                   