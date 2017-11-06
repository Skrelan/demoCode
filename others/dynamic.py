#Memoization

''' concept1 - function decoraters '''

def mydecorator(f):
	'''
	this is your decorator function
		Args: Function f
		Return type: Function
	'''
	def helper(*args,**kwargs):
		''' 
		* pulls in all positional arguments. ex:lists
		** pulls in all keyword arguments. ex: ?
		'''
		print("before")
		f(*args, **kwargs)
		print("after")

	return helper

# myfunction is your real function @decorator is myfunction's function decorator
@mydecorator
def myfunction(name):
	print name

''' concept2 - Dynamic Programming '''	

def memoize(f):
	memo = {0:1}
	def helper(x):
		if x not in memo:
			print memo
			memo[x] = f(x)
		return memo[x]
	return helper

@memoize
def fib(n):
	return n if n <=2 else fib(n-1) + fib(n-2)

#alternative way of implementing decorator
#fib = memoize(fib)