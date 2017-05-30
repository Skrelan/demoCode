## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

'''
/*

### Apriori Problem

Given a list of transactions, How can we calculate the frequency counts of all possible item-sets?

For example,

[INPUT] list of transactions
| -- | -------------------------------------|
| ID | Purchased items                      |
| -- | -------------------------------------|
| 1  | "apple", "banana", "lemon"           |
| 2  | "banana", "berry", "lemon", "orange" |
| 3  | "banana", "berry", "lemon"           |
| -- | -------------------------------------|


[OUTPUT] frequency counts of all possible item-sets. Note: some outputs are omitted for brevity.
| ---------------------------- | --------- |
| Itemset                      | Frequency |
| ---------------------------- | --------- |
| berry                        | 2         |
| apple, banana                | 1         |
| apple, lemon                 | 1         |
| banana, berry                | 2         |
| banana, lemon                | 3         |
| ...                                      |
| apple, banana, lemon         | 1         |
| banana, berry, lemon         | 2         |
| ...                                      |
| banana, berry, lemon, orange | 1         |
| ...                                      |
| ---------------------------- | --------- |

*/

import java.util.*;

public class Apriori {
    public static void main(String[] args){
    }
}
'''

'''
Goal: Find the frequency of all sub-combinations in input
Inputs: List[List[]
Output: Dictonary

'''

'''
set -> apple, bana....
holder.append(set())
'''

'''
1. You want to generate all combinations for A given transaction
-- You want a sorted transaction because you want to store the key as a string

a,b,c

[]

a
[a]
b
[ab b]
[a ab b]
c
[ac abc bc c]
[a ab b ac abc bc a]

'''
from copy import copy

def shopping(lists_of_purchases):
    holder = {}
    for trans in lists_of_purchases:
        trans.sort()
        output = []
        # trans = [a,b,c]
        for fruit in trans:
            wip = copy(output)
            wwip = []
            # print 'output', output,'wip', wip
            for i in wip:
                wwip.append(i[0]+fruit)
                
            wwip.append(fruit)
            output.append(wwip)
        
        for val in output:
            for key in val:
                holder[key] = holder.get(key,0) + 1
        print output 
    print holder, len(holder)
       
    
if __name__ == '__main__':
    shopping([['apple','banana','lemons'],
        ['apple','banana','lemon'],
        ['banana','chery','orange']])
    
# I think I got it, if you are still there?



        
        
            
            
            
    
