class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height = 0
        width = 0
        area =[]
        
        for row_index in range(0,len(matrix)):
            width = 0
            height = 0
            for element_index in range(0,len(matrix[row_index])):
                current_width = 0
                current_height = 0
                element = int(matrix[row_index][element_index])
                down_pointer = row_index
                
                print 'row', row_index, 'column', element_index
                
                if element == 1 and element_index < len(matrix[row_index])-1:
                    while down_pointer < len(matrix) and int(matrix[down_pointer][element_index]) == 1:
                        height = height+1
                        current_width = 0
                        right_pointer = element_index

                        is_first_down_done = False
                        while right_pointer < len(matrix[row_index]) and int(matrix[row_index][right_pointer]) == 1:
                            if int(matrix[down_pointer][element_index+1] == 1) or is_first_down_done: 
                                current_width += 1
                                right_pointer += 1
                                is_first_down_done = True
                        if current_width == 0:
                            continue
                        elif width == 0:
                            width = current_width
                        else:
                            width = min(width,current_width)
                        down_pointer = down_pointer + 1
                    print 'element',element,'height', height,'width',width    
                    edge = min(height,width)
                    area.append(edge*edge)
        print area
        return max(area) 

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