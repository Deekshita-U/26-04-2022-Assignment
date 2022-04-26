import pyautogui
import datetime
import time
import tkinter

#***************STAR PATTERN 1********************
n = int(input("Enter an odd number: "))
t = n // 2

for row in range(n):
    for col in range(n):
        if row + col == t or col - row == t or row - col == t or row + col == 3*t:
            print("*", end = "")
        else:
            print(end = " ")
    time.sleep(3)
    print()

#***************STAR PATTERN 2********************
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(end = " ")
    for k in range(0, i):
        print("* ", end = "")
    print()
    time.sleep(2)
for i in range(1, n):
    for j in range(0, n - i - 1):
        print(end = " ")
    for k in range(0, i + 1):
        print("* ", end = "")
    time.sleep(2)
    print()


#***************SCREENSHOT********************
ss = pyautogui.screenshot()



#***************SETTING FILE NAME********************
curr_time = datetime.datetime.now().replace(microsecond = 0)
print(type(curr_time))
Format = "%Y_%m_%d_%H_%M_%S"
curr_time = datetime.datetime.strftime(curr_time, Format)
file_name = 'hello' + curr_time + '.png'


#***************SAVING FILE********************
ss.save(file_name)
