import random
GermanDict = {}
GermanDict['roof'] = 'Das Dach'
GermanDict['door handle'] = 'Die Klinke'
GermanDict['curtains'] = 'Der Vorhang'
GermanDict['wall'] = 'Die Wand'
GermanDict['ceiling'] = 'Die Decke'
GermanDict['floor'] = 'Der Boden'
GermanDict['bedroom'] = 'Das Zimmer'
GermanDict['entrance hall'] = 'Der Flur'
GermanDict['stairs'] = 'Die Treppe'
GermanDict['furniture'] = 'Die Möbel'
GermanDict['desk'] = 'Der Tisch'
GermanDict['chair'] = 'Der Stuhl'
GermanDict['light switch'] = 'Der Lichtschalter'
GermanDict['fan'] = 'Der Ventilator'
GermanDict['kitchen'] = 'Die Küche'
GermanDict['bathroom'] = 'Das Badezimmer'
GermanDict['dining room'] = 'Das Esszimmer'
GermanDict['laundry'] = 'Die Waschküche'
GermanDict['sala de estar'] = 'Das Wohnzimmer'
GermanDict['garage'] = 'Die Garage'
GermanDict['balcony'] = 'Der Baikon'
GermanDict['garden'] = 'Der Garten'
GermanDict['gate'] = 'Der Pforte'
GermanDict['like'] = 'mögen'
GermanDict['do'] = 'tun'
GermanDict['leave'] = 'abfahren'
GermanDict['birthday'] = 'Der Geburtstag'
GermanDict['color'] = 'Die Farbe'
GermanDict['bread'] = 'Das Brot'
GermanDict['conversation'] = 'Das Gespräch'
GermanDict['offer'] = 'Das Angebot'
GermanDict['food'] = 'Das Essen'
GermanDict['tuition'] = 'Der Unterricht'
GermanDict['favorable'] = 'günstig'
GermanDict['July'] = 'Der Juli'
GermanDict['hand in'] = 'abgeben'
GermanDict['take'] = 'holen'
GermanDict['important'] = 'wichtig'
GermanDict['meet'] = 'treffen'
GermanDict['disco'] = 'Die Disco'
GermanDict['keys'] = 'Der Schlüssel'
GermanDict['back'] = 'zurück'
GermanDict['weight'] = 'Das Gewicht'
GermanDict['winter'] = 'Das Frühling'
GermanDict['chicken'] = 'Das Hänhchen'
GermanDict['early'] = 'früh'
GermanDict['congratulate'] = 'gratulieren'
GermanDict['overnight'] = 'übernachten'
GermanDict['platform'] = 'Der Bahnsteig'
GermanDict['kiosk'] = 'Der Kiosk'


tA = 0
tE = 0
while True:
	SeparatorList = []
	for k in GermanDict.keys():
		SeparatorList.append(k)

	RandomWord = random.choice(SeparatorList)

	UserValue = str(input('Type here the word {} in german: '.format(RandomWord.upper())))

	for k,v in GermanDict.items():
		if RandomWord == k and UserValue == v:
			print('The correcgt german word {} is {}. Nice!'.format(RandomWord.upper(), UserValue))
			tA += 1
		
		if RandomWord == k and UserValue != v:
			print('The correct german word {} is {}. {} is wrong. Try again!'.format(RandomWord.upper(), v.upper(), UserValue))
			tE += 1
	
	FlagUser = str(input('Type [0] if you want to stop or type [1] and continue: '))
	
	if '0' in FlagUser:
		print('Thanks!')
		print('You got it {} times.'.format(tA))
		print('You missed {} times.'.format(tE))
		break
	if '1' in FlagUser:
		continue
