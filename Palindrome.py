def check_palindrome(word_to_check):
	check_word = ''

	for string in word_to_check:
		check_word = string + check_word

	if check_word in word_to_check:
		print(f'{word_to_check} == {check_word}: Palindrome')
	
	else:
		print(f'{word_to_check} != {check_word}: Not Palindrome')

user_word = str(input('Type here your word: ').lower())
check_palindrome(user_word)