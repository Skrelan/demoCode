# /********************************************************************** 
#  *                          			                                *
#  *                                                                    *
#  *  Prompt: Given a set S, return the power set P(S), which is        *
#  *          a set of all subsets of S.                                *
#  *                                                                    *
#  *  Input:  A String                                                  *
#  *  Output: An Array with the power set of the input string           *
#  *                                                                    *
#  *  Example: S = "abc", P(S) = ['', 'a', 'b','c','ab','ac','bc','abc']*                                                               *
#  *                                                                    *
#  *  Note: There should not be any duplicates in the power set         *
#  *        ('ab' and 'ba' are considered the same), and it will always *
#  *        begin with an empty string ('')                             *
#  *                                                                    *
#  **********************************************************************/

def powerSet(input):  #i/p - abcd o/p - "" a b c d ab ac ad bc bd cd 
  # your work here
  super_set = [""]
  length = len(input)
  counter = 0
  for val in input:
	super_set.append(val)
  def helper(inp,counter):
	a =[]
	for val1 in range(0,len(inp)):
		for val2 in range(val1,len(inp)):
			if inp[val1] == inp[val2]: continue
			if inp[val1] in inp[val2] : continue
			holder = inp[val1]+inp[val2]
			print holder
			a.append(holder)
		counter = counter + 1
		super_set.append(a)
		if counter<length:
			helper(super_set,counter)
		
  helper(super_set,counter)
  #return super_set
powerSet('abcd')  
x = raw_input('enter')