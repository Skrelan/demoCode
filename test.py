"""
Questions shared by Nicole:

1.Algorithmic thinking - Find the maximum in an array of integers
 
2. Please describe one web project that you worked on. Can you describe what your contribution was. How much backend, how much front end, what technologies, etc.?
Can you provide a link to your web site that you worked on and point out the pages that you contributed to?
"""


"""
ANS 1.
The question seemed too simple so I tried writing it down as one would in a Production enviroment
and also to share a better understanding of my exposure to Python and quality of code.
"""
import random, time, logging

logging.basicConfig( 
	level=logging.DEBUG,
	format="[%(asctime)s] | [%(levelname)s] | %(message)s")

def timetaken(func):
    def helper(*args,**kwargs):
        start = time.time()
        results = func(*args,**kwargs)
        end = time.time()
        diff = end - start
        logging.info("function {0} took {1} seconds".format(func.__name__,diff))
        return results
    return helper

@timetaken
def maximum_using_built_in_functions(arr):
	return None if len(arr) == 0 else max(arr)

@timetaken
def maximum_using_linear_algo(arr):
	'''
	O(n) time
	O(1) space
	'''
	if len(arr) == 0:
		return None
	max_v = arr[0]
	for i in range(1,len(arr)):
		max_v = max(max_v,arr[i])
	return max_v


if __name__ == '__main__':
	lis = random.sample(range(1, 10000), 1000)
	logging.info("result: {0}".format(maximum_using_built_in_functions(lis)))
	logging.info("result: {0}".format(maximum_using_linear_algo(lis)))

"""
ANS 2.
I have worked on several web applications in the past base on various frameworks and sdks.
The frameworks that I have worked with in the past are the follows. web.py, django and flask.
The web app SDK that I have worked with in the past is the FB SDK

An example of one such application is the web service we use internally at Facebook, which is used to
connect Internal traffic to a 3D party application server which is used for Data visuilizaton. 

My contribution to this python based web service (running on Flask) is re-factoring and optimizing code to improve efficency, 
to create new endpoints based on the needs of our internal customers,
to ensure the webservice is running and Database connections are live,
to modify the Javascript front end on the Application server for customization and interaction with the backend web service.

80-percent Backend (Python), 15-percent Frontend (javaScript) and 5-percent Database(mySQL, HIVE and POSTGRES)

This is internal to Facebook and one can not access it without Autherization.
"""	