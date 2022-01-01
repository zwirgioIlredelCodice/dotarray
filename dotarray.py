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
	i_token = 0
	
	while i_token < len(c_token):
		
		if c_token[i_token] == '.': # append element in stack array
			if c_token[i_token-1].isalnum():
				stack[-1].append(int(c_token[i_token-1]))
			
			elif c_token[i_token-1].startswith("'") and c_token[i_token-1].endswith("'"):
				string = c_token[i_token-1][1:-1]
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
		
		elif c_token[i_token] == '=@':
			t = stack.pop()
			variables[c_token[i_token-1]] = t
		
		elif c_token[i_token] == '@=':
			stack.append(variables[c_token[i_token-1]])
			
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
					n = n * arr[i_arr]
				stack.append([n])
		
		elif c_token[i_token] == '/':
			s = stack
			stack = []
			for arr in s:
				n = arr[0]
				for i_arr in range(1,len(arr)):
					n = n / arr[i_arr]
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
			fn_name = c_token[i_token-1]
			fn = []
			i_token += 1
			while c_token[i_token] != 'f}':
				fn.append(c_token[i_token])
				i_token += 1
			functions[fn_name] = fn
		
		elif c_token[i_token] == 'f=':
			fn_name = c_token[i_token-1]
			for t in functions[fn_name]:
				c_token.append(t)
		
		elif c_token[i_token] == '!debug': #debug
			print('stack =', stack)
			print('variables=', variables)
			
		elif c_token[i_token] == '!fn': #debug
			print(functions)
		
		i_token += 1
	
	if len(stack) > 0:
		print()
		print(stack)
		print()
	