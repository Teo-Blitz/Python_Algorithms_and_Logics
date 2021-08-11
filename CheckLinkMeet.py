def check_link_meet(link_user):
	len_link = len(link_user)
	splitted_link = []
	len_link_meet = len(link_user)

	if len_link_meet == 10:
		for string in link_user:
			if not '-' in string:
				splitted_link.append(string)

	else:	
		print('Try once again!')

	polished_link = ''.join(splitted_link)
	print(polished_link)


get_code_link_meet = str(input('Your link here: '))

check_link_meet(get_code_link_meet)	
