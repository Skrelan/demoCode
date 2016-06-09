###
#
# 1. The test plan will consist of checks for water level , if soap is present , if clothes are present at
#    the start of every cycle ( soak, rinse, etc )
#
# 2. Automation will be done by creating an instance of the class and prompting the user for
#    commands using the console/termianl of machine with the help of a while loop
#
# 3. Assumption done below
#
# 4. The output (True for sucess/False for Failure ) test cases could be written on to a file or a document
#
###
#
# Let's consider the parameters involved:
# 1. Items put into the WM - water, clothes, soap
# 2. Constraints - quantity of water, maximum load
# 3. Controls - soak, rinse, wash, spin
#
# Assumptions:
# 1. Water level remains constant unless manipulated on
# 2. Inorder to do spin, wash must be done
# 3. Inorder to do wash, rinse must be done
# 4. Inorder to do rinse, soak must be done
#
###
import time

# Mac and Linux users use this version of the function:

import select
import sys

def raw_input_with_timeout(timeout):
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
    return None


# Windows users use this: 
#
#import msvcrt
#def raw_input_with_timeout(timeout): #custom Raw_input
#	finish = time.time() + timeout
#	result = []
#	while True:
#		if msvcrt.kbhit():
#			result.append(msvcrt.getche())
#			if result[-1] == '\r':  
#				return ''.join(result)
#			time.sleep(0.1)        
#		else:
#			if time.time() > finish:
#				return None
		
class WashingMachine:
	def __init__(self,capacity):
		self.water_level = 0               #tracks the water level
		self.max_level = capacity       #Sets the max_capacity
		self.min_level = capacity//2    #Sets the minimum required water level for function
		self.priority= 0						#Sets the priority level to insure proper flow of work
		#Start process with 0: soak -> 1:wash -> 2:rinse -> 3:spin.
		self.active = False				#Checks if a process is running
		self.soap = False					#Flag for Soap
		self.clothes = False 				#Flag for clothes 
		
	def soak(self,soap,clothes): #this soaks the clothes, if clothes present. Soaking doesn't use soap
		self.clothes = clothes
		if (self.priority >= 0) & (self.clothes):				
			self.priority = max(1,self.priority)
			self.active = True
			self.soap = soap
			print "soak in progress in order to cancel please enter X any time"
			while self.water_level < self.max_level: #raising water level 
				value = raw_input_with_timeout(1)
				try:
					if value[0] == 'X':
						self.cancel()
						return False
				except:
					print "soaking"
				self.water_level = self.water_level + 1
			print "soak done"
			self.active = False
			return True

	def wash(self):				#this washes the clothes, if 1) soaking is done 2) soap is present 3) water is present
		if self.priority >= 1:
			if self.soap == False:
				print "Please add the Soap and try again"
				soaps = int(raw_input("please enter the soap: 1 Yes / 0 No "))
				if soaps == 1:
					self.soap = True
				else :
					return False
			self.priority = max(2,self.priority)
			if self.water_level < self.min_level:
				print "Not enough water"
				return 0
			else:
				print "wash in progress in order to cancel please enter X any time"				
				self.active = True
				timer = 6
				while timer > 0:
					timer = timer - 1
					value = raw_input_with_timeout(1)
					try:
						if value[0] == "X":
							self.cancel()
							return False
					except:
						print "washing"	
				self.soap = False #soap is only made False when wash is complete 
				self.active = False 
				print "wash is done"
				return True
		else:
			print"wash is not possible."
			return
	
	def rinse(self):     #this rinses out the soap from the clothes, if 1) washing is done 2) water is present
		if (self.priority >= 2):
			self.priority = max(3,self.priority)
			if self.water_level < self.min_level:
				print "Not enough water"
				return
			else:
				print "wash in progress in order to cancel please enter X any time"
				print "rinse in progress"
				self.active = True
				while self.water_level > self.min_level + 1:
					self.water_level = self.water_level - 1
					value = raw_input_with_timeout(0.8)
					try:
						if value[0] == "X":
							self.cancel()
							return False
					except:
						print "rinsing"
				print "Rinse is Done"
				self.active = False
				return True
		else:
			print"rinse is not possible"
			return False
	
	def spin(self): #this spins out the water from clothes, if 1) rinse is done 2) minimum water is present 
		if self.priority >= 3:
			self.priority = max(4,self.priority)
			if self.water_level < self.min_level:
				print "not enough water"
				return
			else:
				self.active = True 
				while self.water_level > 0:
					self.water_level = self.water_level - 1
					value = raw_input_with_timeout(0.5)
					try:
						if value[0] == "X":
							self.cancel()
							return False
					except:
						print "spin"	
				print "spin in Done"
				self.active = False
				return True
		else:
			print"spin is not possible"
			return
	
	def cancel(self): #this cancels the process.
		print"\nCancel cycle !"
		if self.active == True:
			self.priority = 0
			self.active = False
			self.soap = False					 
			while(self.water_level>0):
				self.water_level = self.water_level - 1
				time.sleep(0.1)
			self.active = False
			return
		else:
			print "Machine is not running "
		
####################################################################
text_file = open("Logs.txt","w")  #Stores user logs
text_file.write("The User Activity Log with results\n")

Results = {"Soak_True":0,"Soak_False":0,"Wash_True":0,"Wash_False":0,"Rinse_True":0,"Rinse_False":0,"Spin_True":0,"Spin_False":0}

turboWash = WashingMachine(10)
c = "Text holder"
print "Soak | Wash | Rinse | Spin"
soap = int(raw_input("please enter the soap: 1 Yes / 0 No "))
if soap == 1:
	soap = True
else:
	soap = False
clothes = int(raw_input("please enter number of clothes: "))
if clothes <= 0:
	print "Invalid number of clothes"	
else :
	turboWash.clothes = True
	while c != "":
		c= raw_input("\nEnter 0: soak -> 1:wash -> 2:rinse -> 3:spin. \nEnter nothing to end\n")
		if c != "":
			c = int(c)
			if c == 0:
				ans = turboWash.soak(soap,clothes)
				writes = "\nUser clicked Soak with result " + str(ans)
				text_file.write(writes)
				if ans:
					Results["Soak_True"] = Results.get("Soak_True",0)+1
				else:
					Results["Soak_False"] = Results.get("Soak_False",0)+1
			if  c == 1:
				ans = turboWash.wash()
				writes = "\nUser clicked Wash with result " + str(ans)
				text_file.write(writes)
				if (ans):
					Results["Wash_True"] = Results.get("Wash_True",0)+1
				else:
					Results["Wash_False"] = Results.get("Wash_False",0)+1
			if c == 2:
				ans = turboWash.rinse()
				writes = "\nUser clicked Rinse with result " + str(ans)
				text_file.write(writes)
				if (ans):
					Results["Rinse_True"] = Results.get("Rinse_True",0)+1
				else:
					Results["Rinse_False"] = Results.get("Rinse_False",0)+1
			if c == 3:
				ans = turboWash.spin()
				writes = "\nUser clicked Spin with result " + str(ans)
				text_file.write(writes)
				if (ans):
					Results["Spin_True"] = Results.get("Spin_True",0)+1
				else:
					Results["Spin_False"] = Results.get("Spin_False",0)+1
		
text_file.close()
print "\n Results are as below: \n",Results	
print"\n Open Logs.txt for an easier read"
		
####
#
#  Credits: Suryaa Kumara Relan
#
####