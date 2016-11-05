import pyautogui
print(pyautogui.position())
square = []
i = 0
for b in range(0, 4):
    for a in range(0, 4):
        i += 1
        x = 725 + a * 120
        y = 385 + b * 120
        print(str(i) + ' | ' + str(x) + ', ' + str(y))
        square.append(pyautogui.screenshot(str(i) + '.png', region=(x, y, 95, 95)))

for pos in pyautogui.locateAllOnScreen(square[13]):
    print(pos)
#im2 = pyautogui.screenshot('2.png', region=(710, 370, 120, 120)) 
#im3 = pyautogui.screenshot('3.png', region=(710, 373, 120, 120)) 
#for pos in pyautogui.locateAllOnScreen(im2):
#    print(pos)