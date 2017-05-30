import re
def special_palindrome(s):
	if len(s) == 0:
		return False
	start = 0
	end = len(s)-1
	# for i in range(0,len(s)):
	while start<end:
		print "pass"
		if not re.search('[a-z A-Z]',s[start]):
			start+= 1
			continue
		if not re.search('[a-z A-Z]',s[end]):
			end-=1
			continue
		if not s[start] == s[end]:
			return False
		start+=1
		end-=1
	return True

print special_palindrome('ab*^#cb*a')