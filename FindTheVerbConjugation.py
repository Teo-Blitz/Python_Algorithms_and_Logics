def check_conjugation_verb(verb_example):
	ending_list = ['ar', 'er', 'ir', 'or']

	if verb_example.endswith(ending_list[0]):
		print('This is a first conjugation verb.')

	elif verb_example.endswith(ending_list[1]) or verb_example.endswith(ending_list[3]):
		print('This is a second conjugation verb.')

	else:
		print('This is a third conjugation verb.')

verb_user = str(input('Type here your portuguese verb: '))
check_conjugation_verb(verb_user)