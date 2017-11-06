# Complete the function below.

#can be achieved via function recursion
def  chooseFleets(wheels):
    results = []
    count = 0
    
    def helper(n,c):
        if n <= 0:
            return c
        if n%2 == 0:
            c+=1
            return helper(n-4,c)
            
    for w in wheels:
        count=0
        if w%2 != 0:
            results.append(0)
            continue
        count+= 1
        if w%4 == 0:
            count+=1   
        count = helper(w-4,count)
        results.append(count)
    
    return results
