from time import sleep

side_right = '\\'
side_left = '/'
height = 20
base = 0

counter_1 = 0
counter_2 = height

velocity = .1

for increment_to_right in range(height):
	counter_1 += 1
	print(counter_1 * '+', side_right[-1])
	sleep(velocity)

	if counter_1 == height:
		for decrement_to_left in range(height, 1, -1):
			counter_2 -= 1
			print(counter_2 * '+', side_left[0])
			sleep(velocity)