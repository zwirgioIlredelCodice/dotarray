import sys

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print('benvenuto in Dotarray')

stack = []

c_token = []

evaluated = False

variables = {}
functions = {}

block_n = 0

def execute(text):
	# parse command
	c_token = text.split()
	
	# execute
	i_token = 0
	
	global stack
	
	while i_token < len(c_token):
		
		if c_token[i_token] == '.': # append element in stack array
			i_token += 1
			if c_token[i_token].isalnum():
				stack[-1].append(int(c_token[i_token]))
				
			
			elif c_token[i_token].startswith("'") and c_token[i_token].endswith("'"):
				string = c_token[i_token][1:-1]
				stack[-1].append(string)
		
		elif c_token[i_token] == ':': #create stack array
			stack.append([])
			
		elif c_token[i_token] == ',': #pop element in stack array
			stack[-1].pop()
		
		elif c_token[i_token] == ';': #pop stack array
			stack.pop()
			
		elif c_token[i_token] == ':,;;':
			n = stack.pop()
			n = n[0]
			temp = stack.pop()
			for i_token in temp:
				stack.append([i_token, n])
		
		elif c_token[i_token] == ':;:;':
			temp2 = stack.pop()
			temp1 = stack.pop()
			for i_token in range(len(temp1)):
				stack.append([temp1[i_token], temp2[i_token]])
		
		elif c_token[i_token] == '..:':
			union = []
			for arr in stack:
				for num in arr:
					union.append(num)
			stack = [union]
		
		elif c_token[i_token] == '@=':
			i_token += 1
			t = stack.pop()
			variables[c_token[i_token]] = t
		
		elif c_token[i_token] == '=@':
			i_token += 1
			stack.append(variables[c_token[i_token]])
			
		elif c_token[i_token] == '+': 
			s = stack
			stack = []
			for arr in s:
				n = 0
				for i_arr in arr:
					n += i_arr
				stack.append([n])
		
		elif c_token[i_token] == '-':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = n - arr[i_arr]
				stack.append([n])
		
		elif c_token[i_token] == '*':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n *= arr[i_arr]
				stack.append([n])
		
		elif c_token[i_token] == '/':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n /= arr[i_arr]
				stack.append([n])
		
		elif c_token[i_token] == '>':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n > arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == '=f{':
			i_token += 1
			fn_name = c_token[i_token]
			fn = []
			i_token += 1
			while c_token[i_token] != 'f}':
				fn.append(c_token[i_token])
				i_token += 1
			functions[fn_name] = fn
		
		elif c_token[i_token] == 'f=':
			i_token += 1
			fn_name = c_token[i_token]
			for t in functions[fn_name]:
				c_token.append(t)
		
		elif c_token[i_token] == '?{':
			if stack[-1] == [0]:
				block_n += 1
				
				while c_token[i_token] != '?}' and c_token[i_token] != '<?}' and block_n != 0:
					i_token += 1
		
		elif c_token[i_token] == '?}':
			if block_n > 0:
				block_n -= 1
			i_token += 1
		
		elif c_token[i_token] == '<?}':
			
			if block_n > 0:
				block_n -= 1
			
			while c_token[i_token] != '?{':
				i_token -= 1
			i_token -= 1 # serve per eseguire '?{' così da ricontrollare tipo loop
		
		elif c_token[i_token] == '!debug': #debug
			print('stack =', stack)
			print('variables=', variables)
			
		elif c_token[i_token] == '!fn': #debug
			print(functions)
		
		elif c_token[i_token] == '!print':
			print(stack)
		
		else:
			print(RED,'token',c_token[i_token], 'not recognised !',RESET)
		
		i_token += 1

		
def repl():
	
	command = ''
	
	while command != '!quit':
		
		command = input('\t# ')
			
		execute(command)
		
		if len(stack) > 0:
			print()
			print(stack)
			print()

def test():
	global stack
	global variables
	global functions

	t_code = [':', ';', ': . 666', ':,;;', ':;:;', '..:', '+', '-', '*', '/', '>']
	t_in = [[], 
			[[]],
			[],
			[[1, 2, 3,], 
			[10]], 
			[[1, 2, 3,], 
			[10, 20, 30]], 
			[[1,10],[2,20],[3,30]], 
			[[1,10],[2,20],[3,30]], 
			[[1,10],[2,20],[3,30]],
			[[1,10],[2,20],[3,30]],
			[[1,10],[2,20],[3,30]],
			[[1,10],[20, 2],[3,30]]
			]
	t_output = [[[]],
				[],
				[[666]],
				[[1,10],
				[2,10],
				[3,10]],
				[[1,10],
				[2,20],
				[3,30]],
				[[1,10,2,20,3,30]],
				[[11],[22],[33]],
				[[-9],[-18],[-27]],
				[[10],[40],[90]],
				[[0.1],[0.1],[0.1]],
				[[0],[1],[0]]
				]
	
	print('\ttest')
	for i in range(len(t_code)):

		stack = t_in[i]
		execute(t_code[i])
		if stack == t_output[i]:
			print(GREEN,t_code[i],'passed stack=',RESET, stack)
		else:
			print(RED, t_code[i],'not passed stack=',RESET, stack)
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		repl()
	elif sys.argv[1] == 'test':
		test()
	else:
		print('arg not supported')