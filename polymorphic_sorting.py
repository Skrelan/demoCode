A = -1 
B = 1
C = -1
X = [-1,0,3,3,4]

y1 = []
y2 = []
y = []

def equation(x):
	return (A*x*x)+(B*x)+C

previous = equation(X[0])
y1.append(X[0])

for i in xrange(1,len(X)):
	current = equation(X[i])
	if current > previous:
		y1.append(current)
	else:
		y2.append(current)
	previous = current

print y2
print y1

for i in xrange(len(y2)-1,-1,-1):
	y.append(y2[i])

y.extend(y1)
print y

#https://discuss.leetcode.com/topic/41388/given-a-sorted-integer-array-x-and-3-integers-a-b-and-c-return-the-corresponding-sorted-polynomial-array/2