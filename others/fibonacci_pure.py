def nthfibo_pure(n):
	return n if n<2 else nthfibo(n-1) + nthfibo(n-2)


def nthfibo_noob(n):
	fibbo = [0,1]
	i = 0
	def helper(i):
		if i>n:
			return
		if i>=2:
			result = fibbo[i-1]+fibbo[i-2]
			fibbo.append(result)
			helper(i+1)
	helper(2)
	return fibbo[n]