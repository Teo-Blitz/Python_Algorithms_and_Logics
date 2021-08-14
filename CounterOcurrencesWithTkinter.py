from tkinter import Tk, Label, Text, Button, Entry, StringVar, Scrollbar

tracker_word = Tk()
tracker_word.title('Tracker Word')
tracker_word.resizable(0, 0)
tracker_word.geometry('600x620')

#Functions
def track_the_word():
    get_word_from_text = text_operate.get(1.0, 'end-1c')

    do_list = get_word_from_text.split()

    get_word_to_track = collect_word_to.get()

    counter = 0

    for word in do_list:
        if get_word_to_track.lower() == word.lower():
            counter += 1

            if counter != 1:
                value_to_show_from_main_text.set('The word [%s] was tracked %d times.' % (get_word_to_track.capitalize(), counter))
            else:
                value_to_show_from_main_text.set('The word [%s] was tracked %d time.' % (get_word_to_track.capitalize(), counter))
    

#Variables
value_to_show_from_main_text = StringVar()

#GUI
scrollbar_tracker = Scrollbar(tracker_word)
text_operate = Text(tracker_word, 
                    width = 52, height = 20,
                    yscrollcommand = scrollbar_tracker.set,
                    bg = '#d0d181',
                    fg = '#1d326d', 
                    selectbackground = '#c2ccc2',
                    font = 'Arial 15 bold')

message_label = Label(tracker_word, text = 'Type your word to track the number of ocurrences from a text or a sentence.')
collect_word_to = Entry(tracker_word)
get_the_value_button = Button(tracker_word, text = 'Track it!', command = track_the_word)
show_value_label = Label(tracker_word, textvariable = value_to_show_from_main_text, width = 70, relief = 'sunken', pady = 10)


#Calls
scrollbar_tracker.pack(side = 'right', fill = 'y')
text_operate.pack()
message_label.pack()
collect_word_to.pack()
get_the_value_button.pack()
show_value_label.pack()

#Other Operations
text_operate.focus()
scrollbar_tracker.config(command = text_operate.yview)

tracker_word.mainloop()