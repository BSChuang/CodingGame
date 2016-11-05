import pyautogui

sleepTime = 1
pyautogui.click()
print(pyautogui.position())
score = pyautogui.screenshot('score.png', region=(993, 205, 87, 23))

while True:
    scorePrev = score
    pyautogui.time.sleep(sleepTime)
    pyautogui.press('up')
    score = pyautogui.screenshot('score.png', region=(993, 205, 87, 23))
    if score == scorePrev:
        pyautogui.press('right')
        pyautogui.press('up')
        score = pyautogui.screenshot('score.png', region=(993, 205, 87, 23))
        if score == scorePrev:
            pyautogui.press('left')
