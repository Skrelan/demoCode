# Implement the 3 functions belows so the code executes and produces the expected output.
# Do not include any other imports.
# Do not use any Python built-in functions like.
# Is guarenteed to execute to completion.

import time
import random

## YOUR CODE ONLY BELOW HERE
# 1. Implement this function

def enum(iterator):
    i = -1
    while True:
        i = i+1
        yield i, next(iterator)

# 2. Implement this function (a generator)
def stream_objects():
    while True:
        obj = Object()
        yield obj

# 3. Implement this function
def timetaken(func):
    def helper(*args,**kwargs):
        start = time.time()
        results = func(*args,**kwargs)
        end = time.time()
        diff = end - start
        #print results
        print "Run function took {} seconds".format(diff)
        return results
    return helper
## YOUR CODE ONLY ABOVE HERE


## DO NOT MODIFY ANYTHING BELOW HERE
class Object():
    def __init__(self):
        self.complete = random.random() < 0.2

    def is_complete(self):
        return self.complete

@timetaken
def run():
    for index, current in enum(stream_objects()):
        #print "%%%",index, current.is_complete()
        if current.is_complete():
            return index

print 'Expected output:'
print "Run function took # seconds."
print 'Final object was at index #.'

print 'Actual output:'
final_index = run()
print 'Final object was at index {}'.format(final_index)