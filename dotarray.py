# questo è veramente bello
print('benvenuto in Dotarray')

stack = []

command = ''
c_token = []

evaluated = False

variables = {}
functions = {}

while command != '!quit':
	
	command = input('\t# ')
	
	# parse command
	c_token = command.split()
	
	# execute
	i = 0
	
	while i < len(c_token):
		
		evaluated = False
		
		if c_token[i] == '.': # append element in stack array
			stack[-1].append(int(c_token[i-1]))
		
		elif c_token[i] == ':': #create stack array
			stack.append([])
			
		elif c_token[i] == ',': #pop element in stack array
			stack[-1].pop()
		
		elif c_token[i] == ';': #pop stack array
			stack.pop()
			
		elif c_token[i] == ':,;;':
			n = stack.pop()
			n = n[0]
			temp = stack.pop()
			for i in temp:
				stack.append([i, n])
		
		elif c_token[i] == ':;:;':
			temp2 = stack.pop()
			temp1 = stack.pop()
			for i in range(len(temp1)):
				stack.append([temp1[i], temp2[i]])
		
		elif c_token[i] == '..:':
			arr = []
			for nums in stack:
				arr.append(nums[0])
			stack = [arr]
		
		elif c_token[i] == '=@':
			t = stack.pop()
			variables[c_token[i-1]] = t
		
		elif c_token[i] == '@=':
			stack.append(variables[c_token[i-1]])
			
		elif c_token[i] == '+': 
			s = stack
			stack = []
			for arr in s:
				n = 0
				for i in arr:
					n += i
				stack.append([n])
		
		elif c_token[i] == '-':
			s = stack
			stack = []
			for arr in s:
				n = 0
				for i in arr:
					n -= i
				stack.append([n])
		
		elif c_token[i] == '=f{':
			fn_name = c_token[i-1]
			fn = []
			i += 1
			while c_token[i] != 'f}':
				fn.append(c_token[i])
				i += 1
			functions[fn_name] = fn
		
		elif c_token[i] == 'f=':
			fn_name = c_token[i-1]
			for t in functions[fn_name]:
				c_token.append(t)
		
		elif c_token[i] == '!debug': #debug
			print('stack =', stack)
			print('variables=', variables)
			
		elif c_token[i] == '!fn': #debug
			print(functions)
		
		i += 1
	
	if len(stack) > 0:
		print()
		print(stack)
		print()
	