def counter_ocurrences_words(word_in_text):
	dict_ocurrences = dict()
	polish_text = word_in_text.split()

	for string in polish_text:
		if string in dict_ocurrences:
			dict_ocurrences[string] += 1
		else:
			dict_ocurrences[string] = 1

	print(dict_ocurrences)


simple_text = 'the boy is amazing and the girl is smart'
counter_ocurrences_words(simple_text)