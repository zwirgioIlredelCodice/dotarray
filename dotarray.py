import sys
import copy

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

def execute(text):
	# parse command
	c_token = text.split()
	
	# execute
	i_token = 0
	block_n = 0
	
	global stack
	
	while i_token < len(c_token):
		
		if c_token[i_token] == '.': # append element in stack array
			i_token += 1
			is_float = False

			try:
				float(c_token[i_token])
				is_float = True
			except:
				is_float = False

			if is_float:
				stack[-1].append(float(c_token[i_token]))
			
			else:
				string = c_token[i_token].replace('_', ' ')
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
			var = copy.deepcopy(variables[c_token[i_token]]) # bug strano cosi non passa per reference senno cambiai stack e cambiava anche var
			stack.append(var)
			
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
		
		elif c_token[i_token] == '%':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n %= arr[i_arr]
				stack.append([n])
		
		elif c_token[i_token] == '>':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n > arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == '>=':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n >= arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == '<':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n < arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == '<=':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n <= arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == '==':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n == arr[i_arr])
				stack.append([n])

		elif c_token[i_token] == 'and':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n & arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == 'or':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n | arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == 'xor':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = int(n ^ arr[i_arr])
				stack.append([n])
		
		elif c_token[i_token] == 'not':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in arr:
					n = int(i_arr)
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
		
		elif c_token[i_token] == '<?}':
			
			if block_n > 0:
				block_n -= 1
			
			while c_token[i_token] != '?{':
				i_token -= 1
			i_token -= 1 # serve per eseguire '?{' così da ricontrollare tipo loop
		
		elif c_token[i_token] == '"': #coment
			i_token += 1
			while c_token[i_token] != '"':
				i_token += 1

		elif c_token[i_token] == '!debug': #debug
			print('stack =', stack)
			print('variables=', variables)
			
		elif c_token[i_token] == '!fn': #debug
			print(functions)
		
		elif c_token[i_token] == '!print':
			print(stack)
		
		elif c_token[i_token] == '!quit':
			pass
		
		else:
			print(RED,'token',c_token[i_token], 'not recognised at i_token', i_token, RESET)
		
		i_token += 1

		
def repl():
	
	command = ''
	
	while command != '!quit': # L oop
		
		command = input('\t# ') # R eand
			
		execute(command) # E xecute
		
		if len(stack) > 0: # P rint
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

def exec_file(filename):
	f = open(filename, "r")
	program = f.read()
	execute(program)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		repl()
	elif sys.argv[1] == 'test':
		test()
	else:
		exec_file(sys.argv[1])