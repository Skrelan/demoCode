"""
SFO => LAX => NYC => LHR
(A , B)

[NYC, LHR, LAX, SFO]
NYC LHR, LAX, NYC, SFO, LAX

#1
GOAL: To find the origin

INPUT: array of tuples
OUTPUT: Starting city

"""

"""
Key Values
SFO  LAX
LAX  NYC
NYC  LHR

while key!=0
    results.append(key)
    key = d.get('SFO',0) 
    

"""
import random

def main():
    '''
    Trip:
        SFO => LAX
        LAX => NYC
        NYC => LHR
        
    '''
    tickets = [
        ('SFO', 'LAX'),
        ('LAX', 'NYC'),
        ('NYC', 'LHR')
    ]
    
    # Randomly shuffle the tickets
    random.shuffle(tickets)
    
    
    # Get the origin city
    origin = get_origin(tickets)
    print origin # SFO
    print get_path(tickets)
    

    
def get_origin(tickets): #O(n)
    cities = set()
    for ticket in tickets:
        cities.add(ticket[0])
        cities.add(ticket[1])
    for ticket in tickets:
        cities.remove(ticket[1])
    return cities.pop()
    
    
        

    
def get_path(tickets):
    start = get_origin(tickets)#O(N)
    key = start
    results = []
    d = {}
    for ticket in tickets: #O(N)
        d[ticket[0]]=ticket[1]
        
    while key!= None: #O(N)
        results.append(key)
        print key
        key = d.get(key,None)
    
    return results

if __name__ == "__main__":
    main()
    