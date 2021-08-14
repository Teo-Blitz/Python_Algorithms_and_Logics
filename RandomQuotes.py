from tkinter import Tk, Label, Button, StringVar
from random import choice

#SetupStart
memo_verses = Tk()
memo_verses.title('Memo Verses')
memo_verses.geometry('1024x600')
memo_verses.resizable(False, False)

#VariableProcess
get_string = StringVar()

dict_sentences = {
        0 : 'The way to get started is to quit talking and begin doing. -Walt Disney',
        1 : "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
        2 : "Life is what happens when you're busy making other plans. -John Lennon"
        }

        #You can add infinites quotes.

#FunctionZone
def set_verses():
	len_dict_sentences = len(dict_sentences)
	choice_options = range(0, len_dict_sentences)
	choice_sentence = choice(choice_options)

	get_string.set(dict_sentences.get(choice_sentence))

#GUI
label_verse = Label(memo_verses,
					textvariable = get_string,
					width = 100,
					height = 10,
					font = 'Ubuntu 12', 
					bd = 5,
					relief = 'groove')
button_set_verse = Button(memo_verses, text = 'Set Daily Verse', command = set_verses)

#Layout
label_verse.pack()
button_set_verse.pack()

memo_verses.mainloop()