import pyautogui
import keyboard
import pytesseract
import time
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(2)
screenshot = pyautogui.screenshot("screenshot.png", region=(200,450,1575,190))
whatToType = (pytesseract.image_to_string(('screenshot.png')))
print(whatToType)
time.sleep(0.05)
for char in whatToType:
    if char == "\n":
        keyboard.press_and_release("space")
    else:
        time.sleep(0.00000001)
        keyboard.write(char)