from tkinter import Tk, Label, Entry, Button, StringVar

Check_Fatorial = Tk()
Check_Fatorial.title('Check Fatorial')
Check_Fatorial.geometry('200x200')


#Function
def show_factorial():
  get_index = get_value.get()
  counter_to_factorial = 1

  for number in range(1, int(get_index) + 1):
    counter_to_factorial *= number

  process_value.set(f'O fatorial de {get_index} é {counter_to_factorial}.')

#Variables
process_value = StringVar()

#GUI
get_value = Entry(Check_Fatorial)
button_show_fatorial = Button(  Check_Fatorial, 
                                text = 'Check Fatorial',
                                command = show_factorial)

show_label = Label(Check_Fatorial, textvariable = process_value)

#Calls
get_value.pack()
button_show_fatorial.pack()
show_label.pack()

#Other Commands
get_value.focus()

Check_Fatorial.mainloop()