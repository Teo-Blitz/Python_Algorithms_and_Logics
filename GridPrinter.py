def simple_line():
	size_x = 5
	
	print('+' + '-' * size_x + '+', end = ' ')
	print('+' + '-' * size_x + '+', end = ' ')
	print('+' + '-' * size_x + '+')

def simple_column():
	size_y = 5

	print('|' + ' ' * size_y + '|', end = ' ')
	print('|' + ' ' * size_y + '|', end = ' ')
	print('|' + ' ' * size_y + '|')

def twice_column():
	simple_line()
	simple_column()
	simple_column()	

def double_twice_column():
	twice_column()
	twice_column()
	simple_line()

def grid_complete():
	double_twice_column()
	double_twice_column()

grid_complete()