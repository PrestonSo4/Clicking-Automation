"""
import webbrowser
import pyautogui as p
from time import sleep
def clickImage(file, con):
    from time import sleep
    while True:
        try:
            imageX, imageY = p.locateCenterOnScreen(file, confidence=con)
            p.moveTo(imageX,imageY)
            pClick()
            break
        except:
            print('Not found')
            sleep(0.001)
    
    time.sleep(1)
path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(path).open_new('https://contrastsecurity--qa.my.salesforce.com/0065200000BXrTp')
clickImage('button1.png', 0.8)
""""