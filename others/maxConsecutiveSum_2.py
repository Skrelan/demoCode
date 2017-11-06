def max_sum(list_of_numbers):
	if len(list_of_numbers) == 0:
		return 0
	local_max = list_of_numbers[0]
	sums = []
	for i in range (1,len(list_of_numbers)):
		#local_max = max(local_max+,list_of_numbers[i])
		if local_max + list_of_numbers[i] < list_of_numbers[i]:
			sums.append(local_max)
			local_max = list_of_numbers[i]
		else:
			local_max+= list_of_numbers[i]
		sums.append(local_max)
	print sums
	print max(sums)
