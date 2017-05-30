
from copy import copy
def elections(inputs, T):
	if len(inputs)== 0:
		return ""
	inputs.sort() #4 , 8 , 12...
	votes_untill = {} #this will store the votes until day present in keys 
	tals = {inputs[0][1]:1} #this will store the tals from each day
	votes_untill = {inputs[0][0]:tals}
	for i in xrange(1,len(inputs)):
		# votes_untill = votes_untill.get(inputs[i][0], tals) 
		# we need to now check for past values of the candidate
		tal = copy(tals)
		tal[inputs[i][1]] = tal.get(inputs[i][1],0)+1
		votes_untill[inputs[i][0]] = tal
	t = T
	results = None
	print votes_untill
	while t >= 0: # T can be 0
		if t in votes_untill:
			results = votes_untill[t]
			return max(results)
		t -= 1

	print("no votes happened before time {}".format(T))
	return ""