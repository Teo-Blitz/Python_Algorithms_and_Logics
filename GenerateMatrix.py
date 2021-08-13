def generate_matrix(a, b, c):
	for i in zip(a, b, c):
		print(list(i))

a = [1, 2]
b = [2, 3]
c = [3, 4]

generate_matrix(a, b, c)