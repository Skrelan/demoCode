#Find the number of occurances of a substring with a wild character with in a string.
#Constrains
#1. Each Substring, P may have any of the 5 Characters A,B,C,D or *. Where * is a wild character
#2. Each String, S will have only Characters A,B,C or D.

############################################# 

#Inputs
ints = raw_input()
S = raw_input()
P = raw_input()

#Assumption:
# when going through the list S searching for matches, * in P can be any element A,B,C or D.
#i.e if S = ABABADAC & P = A*
#result would be = 4    ->(AB)(AB)(AD)(AC)

#Example:
#S=ABCAABC P=ABC
#desired output 2 -> (ABC)A(ABC), we must keep track of the past element

#it is possible to solve this problem using 2 for loops but it will be an O(n^2) solution even at best case, as below pesudo code
#
#for i in xrange(0,len(S)):
#   for j in xrange(i,len(S)):
#      #compare element by element S and P till either a full match is found or a missmatch and alter result accordingly
#      #also keep track of weather match has occured so that we do not re-visit a subset
#
#This solution is can be improved upon and the best case can be brought down to O(n) 
#
#I am going to attempt a best case of O(n), worst case of O(n^2) solution as shown below


def hodor(S,P):
    result = 0
    tracker = 0
    i = 0
    flag = False
    while i < len(S):
        if ((S[i] == P[tracker])|(P[tracker] == '*')):
            if tracker == 0:
                if i+1 < len(S)-1: #for tracking the index where a match started
                    holder = i
                    flag = True   #to indicate if miss-match happened mid-way through
            if tracker == (len(P)-1):
                result = result + 1
                tracker = 0
            else:
                #if tracker < len(P): #making sure tracker is less than the length of P, inorder to avoid outOfRange error
                tracker = tracker + 1    
        else:
            tracker = 0
            if flag:
                i = holder
                flag = False
        #print i,holder,"S",S[i],"P",P[tracker],flag   for testing/debugging purpose
        i = i + 1
       
    return result 

print hodor(S,P)