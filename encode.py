class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        str_lens = []
        if len(strs) == 0:
            print ' invalid '
            return False
        print strs
        
        for string in strs:
            print string, len(string)
            str_lens.append(len(string))
            for i in string:
                value = chr((ord(i)+5))
                result += value
        # end char
        result += 'X'
        # append lengths
        for i in str_lens:
            result += str(i)
            result +="O" 

        # append the no. of strings
        result += str(len(strs))
        return result 
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        string = ''
        holder = s[::-1]
        holder = holder[:holder.find('X')]
        print holder
        no_of_strings = int(holder[0])
        holder = holder[1:]
        print holder, no_of_strings
        holder = holder.split('O')
        holder.remove('')
        holder = holder[::-1]
        string_pointer = 0
        string_number = 0
        print holder
        if len(s) == 0:
            print ' invalid '
            return False
        for i in range(0,no_of_strings):
            string = ''
            print holder[string_number]
            for j in range(0,int(holder[string_number])):
                print string, j
                string += chr((ord(s[string_pointer+j])-5))
            string_pointer += int(holder[string_number])
            string_number += 1
            print string
            result.append(string)
        return  result    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
if __name__ == '__main__':
    codec = Codec()
    a = codec.encode(["this is","a","fucking test"])
    print a
    print codec.decode(a)