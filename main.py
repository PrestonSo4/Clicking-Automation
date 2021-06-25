'''
NOTE:

In order for this to work you need this command in the CMD prompt
C:\{Path to your chrome} --remote-debugging-port=5050 --user-data-dir="{folder for the test data}"
'''
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
def clickOn(xpath):
    from time import sleep
    while True:
        try:
            driver.find_element_by_xpath(xpath).click()
            sleep(2)
            break
        except:
            print('Not found')
            sleep(0.001)        
options = Options()
options.add_experimental_option('debuggerAddress', 'localhost:5050')
path = 'C:\\Users\\Preston\\Python projects\\chromedriver.exe'  
driver = webdriver.Chrome(options = options)
driver.get('https://contrastsecurity--qa.my.salesforce.com/0065200000BXrTp')    
driver.maximize_window()
clickOn('//*[@id="topButtonRow"]/input[3]')
clickOn('//*[@id="00NG000000Fffpe"]')
clickOn('//*[@id="opp11"]')
clickOn('//*[@id="00N5200000Cye2U"]')
clickOn('//*[@id="00NG000000FDbEg"]')
clickOn('//*[@id="topButtonRow"]/input[3]')