from tkinter import Tk, Label, Entry, Button, StringVar

generator_story = Tk()
generator_story.title('Generator Story')
generator_story.resizable(0, 0)

#Functions
def create_story_from_template_1():
  w_1_story_1 = word_1_input.get()
  w_2_story_1 = word_2_input.get()
  w_3_story_1 = word_3_input.get()

  result_text.set(f'This {w_1_story_1.capitalize()} bring me a {w_2_story_1.capitalize()} to {w_3_story_1.capitalize()} a lot.')

def create_story_from_template_2():
  w_1_story_2 = word_1_input.get()
  w_2_story_2 = word_2_input.get()
  w_3_story_2 = word_3_input.get()

  result_text.set(f'Even the {w_1_story_2.capitalize()} can be {w_2_story_2.capitalize()} if the {w_3_story_2.capitalize()} smile.')

def create_story_from_template_3():
  w_1_story_3 = word_1_input.get()
  w_2_story_3 = word_2_input.get()
  w_3_story_3 = word_3_input.get()

  result_text.set(f'Your {w_1_story_3.capitalize()} would be more {w_2_story_3.capitalize()} when the beautiful {w_3_story_3.capitalize()} run.')


#Variables
result_text = StringVar()

#GUI
word_1_input = Entry(generator_story, width = 50, font = 'Arial 20')
word_2_input = Entry(generator_story, width = 50, font = 'Arial 20')
word_3_input = Entry(generator_story, width = 50, font = 'Arial 20')

story_label = Label(generator_story, width = 60, height = 15, 
                    relief = 'groove', textvariable = result_text, font = 'Arial 15')

word_1_label = Label(generator_story, text = 'Word 1')
word_2_label = Label(generator_story, text = 'Word 2')
word_3_label = Label(generator_story, text = 'Word 3')

label_message_option = Label(generator_story, text = 'Choose your template and create your story!')

button_template_1 = Button(generator_story, text = 'Template_1', width = 28, command = create_story_from_template_1)
button_template_2 = Button(generator_story, text = 'Template_2', width = 28, command = create_story_from_template_2)
button_template_3 = Button(generator_story, text = 'Template_3', width = 28, command = create_story_from_template_3)

#Calls
word_1_label.grid(row = 0, column = 0, padx = 5, pady = 2)
word_1_input.grid(row = 1, column = 0, padx = 5, pady = 2)

word_2_label.grid(row = 2, column = 0, padx = 5, pady = 2)
word_2_input.grid(row = 3, column = 0, padx = 5, pady = 2)

word_3_label.grid(row = 4, column = 0, padx = 5, pady = 2)
word_3_input.grid(row = 5, column = 0, padx = 5, pady = 2)

label_message_option.grid(row = 6, column = 0, padx = 5, pady = 2)

button_template_1.grid(row = 7, column = 0, padx = 5, pady = 2, columnspan = 1, sticky = 'W')
button_template_2.grid(row = 7, column = 0, padx = 5, pady = 2, columnspan = 1)
button_template_3.grid(row = 7, column = 0, padx = 5, pady = 2, columnspan = 1, sticky = 'E')

story_label.grid(row = 8, column = 0, padx = 5, pady = 2)

generator_story.mainloop()