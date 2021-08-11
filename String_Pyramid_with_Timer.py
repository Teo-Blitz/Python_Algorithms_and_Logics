from time import sleep

def process_string_to_pyramid(string_unpolished, speed_to_print):
	slice_string = string_unpolished.split()
	del_spaces = ''.join(slice_string)

	for sliced_string in range(len(del_spaces)):
		print(del_spaces[:sliced_string + 1])
		sleep(speed_to_print)

string_from_user = str(input('Type your word or sentence here: '))
velocity_by_time = float(input('How fast do you want?: '))


process_string_to_pyramid(string_from_user, velocity_by_time)
