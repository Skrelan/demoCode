def largest_sum(nums, k):
    
    holder = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in nums:  #O(n)
        holder[i] = holder[i]+1 
    
    # by this point we should have the tallys in holder
    
    maximum_index = 9
    i = 0
    summed = 0
    
    while i < k: #o(k)
        while holder[maximum_index] == 0:
                maximum_index -= 1
        summed += maximum_index
        holder[maximum_index] -= 1
        i += 1
    return summed     