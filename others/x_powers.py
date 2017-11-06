def get_combo(x,n):
	mapping = {}
	count = 0
	def get_powers():
		for i in range(0,x+1):
			val = pow(i,n)
			if val > x:
				return
			mapping[i] = val
		print mapping

	def core(num,count):
		r = None
		if num in mapping.values():
				count += 1
				print "#",count
				return mapping.values().index(num)
		if num <=0 :
			return None
		for i in range(1,len(mapping)+1):
			diff = num-mapping[i]
			if diff in mapping.values():
				count += 1
				print "#",count
				return mapping.values().index(diff) 
			else:
				r = core(diff,count)
				if r:
					print r
					return r
				else:
					return None
		return r

	get_powers()
	print mapping
	print core(x,count)
	print count

get_combo(100,2)