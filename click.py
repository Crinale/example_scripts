import pyautogui
import keyboard

print(pyautogui.position())
pyautogui.FAILSAFE = True

def clickcookie():
	pyautogui.PAUSE = .5
	pyautogui.click(x=194, y=388,clicks=1000, interval=.001)

while True:
	clickcookie()
	if keyboard.is_pressed('q'):
		break

