from copy import copy
def find_sum(ls,T):
	result = []
	dict_org = {}
	dict_curr = {}
	
	for i in ls:
		dict_org[i] = dict_org.get(i,0) + 1

	# print dict_org

	for i in dict_org:
		dict_curr = copy(dict_org)
		dict_curr[i] =  dict_curr[i] - 1
		# print T, i, T - i
		if T - i in dict_curr:
			# print 'yes'
			if dict_curr[T-i] != 0:
				result.append((i,T-i))
	print result

find_sum([1,2,3,4,5,6,7,8,9,5],10)