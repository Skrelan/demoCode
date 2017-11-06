'''
/**
 * snapchat -> snap chat
 * playground -> play ground
 * TheGreatesHashTagEver -> The Greates Hash Tag Ever
 *
 *
 */
 
 holder = ""
 hello world
   
 helloworldcake
 
 def 
 # break down words
 h = ''
 for char
    h += char
    if h in english:
        # break down words for the rest of string
        
    
 result = []

 
 abcedfghlm
 
 if holder in english:
    
 Goal: break a single word down into multiple words seperated by spaces.
 Input :word (string), english(list) 
 Output: result (string)
'''

def find_words(word,english):
    print "in",word
    h = ''
    for i in range(0,len(word)):
        h += word[i]
        
        if h in english:
            res = find_words(word[i+1:],english) #lloworld
            if not res :
                continue
            else:
                # print "#",res
                h += " "+res
                return h
                
    if (h == word) and (h not in english):
        return None
    return h

    
print find_words("snapchatcake",["he","hell","hello","world","cake","snap","chat"])