def conjugate_verbs(verb_to_conjugate, tense_verb):
	dict_regular_verbs_present_tense_conj_one = {	
	'eu' : 'o',
	'tu' : 'as',
	'ele' : 'a',
	'nós' : 'amos',
	'vós' : 'ais',
	'eles' : 'am'}

	dict_regular_verbs_past_tense_conj_one = {	
	'eu' : 'ei',
	'tu' : 'aste',
	'ele' : 'ou',
	'nós' : 'amos',
	'vós' : 'astes',
	'eles' : 'aram'}

	dict_regular_verbs_future_tense_conj_one = {	
	'eu' : 'arei',
	'tu' : 'arás',
	'ele' : 'ará',
	'nós' : 'aremos',
	'vós' : 'areis',
	'eles' : 'arão'}

	dict_new = dict()

	separate_root = verb_to_conjugate[:-2]

	if 'present' in tense_verb:
		for lines in dict_regular_verbs_present_tense_conj_one.keys():
			ending = dict_regular_verbs_present_tense_conj_one.get(lines)
			word_final = separate_root + ending

			dict_new[lines] = word_final

		for conjugation in dict_new.items():
			print(conjugation)
	
	elif 'past' in tense_verb:
		for lines in dict_regular_verbs_past_tense_conj_one.keys():
			ending = dict_regular_verbs_past_tense_conj_one.get(lines)
			word_final = separate_root + ending

			dict_new[lines] = word_final

		for conjugation in dict_new.items():
			print(conjugation)

	else:
		for lines in dict_regular_verbs_future_tense_conj_one.keys():
			ending = dict_regular_verbs_future_tense_conj_one.get(lines)
			word_final = separate_root + ending

			dict_new[lines] = word_final

		for conjugation in dict_new.items():
			print(conjugation)		

print('This a portuguese verb conjugator. Only first declension here!')

verb_user = str(input('Type here your verb: '))
tense_user = str(input('What tense do you want? Type [present], [past] or [future]: ').lower())
conjugate_verbs(verb_user, tense_user)