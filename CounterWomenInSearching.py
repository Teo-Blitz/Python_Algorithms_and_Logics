age_list_total = [] 
age_list_female = [] 
counter_female = 0 

while True:
	gender_user = str(input('Type [M] if man, [W] if woman: ').upper())

	if 'W' in gender_user: 

		age_user_female = int(input('Are you between 18 and 35 years old? Type your age: '))

		if age_user_female >= 18 and age_user_female <= 35:
			age_list_female.append(age_user_female) 
			age_list_total.append(age_user_female)
			print(age_list_female)

		color_hair_female = str(input('Do you have blond hair and green eyes? Type [Y] or [N]: ').upper())

		if 'Y' in color_hair_female:
			counter_female += 1 
			print(counter_female)

		else:
			age_list_total.append(age_user_female) 

	else:
		age_total_question = int(input('How old are you?: '))
		age_list_total.append(age_total_question)

	max_age_users = max(age_list_total)

	flag_user = str(input('Do you want to continue? Type [Y] or [N]: ').upper())

	if 'Y' in flag_user:
		continue
	
	else:
		print(f'There are {counter_female} women with green eyes and blond hair. ')
		print(f'They are between 18 and 35 years old.')
		print(f'The oldest person is {max_age_users} years old.')
		break
