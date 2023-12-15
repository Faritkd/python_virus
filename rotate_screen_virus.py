import rotatescreen as Rs
import time
# The first one is in a for loop which is suitable for testing.
current_screen = Rs.get_primary_display()
angle_list = [90, 180, 270, 0]

for i in range(5):
    for j in angle_list:
        current_screen.rotate_to(j)
        time.sleep(0.3)
# __________________________________________________________________________
# This version is an infinite loop which is more annoying. The timer is set to 3 seconds for convenience in testing.
current_screen = Rs.get_primary_display()
angle_list = [90, 180, 270, 0]

while True:
    for j in angle_list:
        current_screen.rotate_to(j)
        time.sleep(3)

# you can use "ctrl+alt+del" to stop the process.
