def function1(value, number):   
	if (number == 0):          # 1
		return 1                  # 1
	elif (number == 1):        # 1     
		return value              # 1
	else:
		return value * function1(value, number-1) 
		 # 2 +T(n - 1)
		
# if n = 0 ----> T(0) = 1
# if n = 1 ----> T(1) = 2
# if n = 2 ----> T(2) = 

# T(n) = 6 + T(n - 1)
# T(n) = O(n)




def recursive_function2(mystring,a, b):
	if(a >= b ):      # 1
		return True   # 1
	else:
		if(mystring[a] != mystring[b]): 	# 1
			return False                   # 1
		else:
			return recursive_function2(mystring,a+1,b-1)      # 1 + T(n+1) + T(n - 1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)  # 1 + T(n - 1)

# T(n) = 6 + T(n + 1) + T(n - 1) + T(n - 1)
# T(n) = 6 + T(n - 1)
# T(n) = O(n)





def function3(value, number):
	if (number == 0):          # 1
		return 1               # 1
	elif (number == 1):        # 1
		return value           # 1
	else:
		half = number // 2      # 2
		result = function3(value, half)    # 1 + T(n/2)
		if (number % 2 == 0):             # 2 + T(n/2)
			return result * result         # 1
		else:
			return value * result * result  # 2

# T(n) = 12 + T(n/2) + T(n/2)
# T(n) = 12 + T(n)
# T(n) = O(n)