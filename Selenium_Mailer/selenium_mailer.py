import time, sys, os, pyperclip, pyautogui
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    load_dotenv()
    receiver = input('Write reciever email: ')
    title = input('Write title for your mail: ')
    message = input('Write the message: ')

    # Create web driver
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open a webpage
    driver.get("https://mail.google.com/mail")

    # Insert email
    input_field = driver.find_element('xpath','//*[@id="identifierId"]')
    pyperclip.copy(os.getenv('EMAIL'))
    input_field.send_keys(Keys.CONTROL, 'v')

    # Next -
    NextLink = driver.find_element('xpath', '//*[@id="identifierNext"]/div/button')
    NextLink.click()

    time.sleep(5)
    # Insert password
    input_field = driver.find_element('xpath','//*[@id="password"]/div[1]/div/div[1]/input')
    pyperclip.copy(os.getenv('PASS'))
    input_field.send_keys(Keys.CONTROL, 'v')

    # Next -
    NextLink = driver.find_element('xpath', '//*[@id="passwordNext"]/div/button')
    NextLink.click()

    # Open pop-up to write new email
    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    
    # Inserting receiver email 
    time.sleep(10)
    pyperclip.copy(receiver) # pyperclip.copy(sys.argv[1])
    pyautogui.hotkey('ctrl', 'v')

    # Insert title
    pyautogui.hotkey('tab')  
    pyperclip.copy(title)
    pyautogui.hotkey('ctrl', 'v')

    # Insert message
    pyautogui.hotkey('tab')  
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    
    # Send email
    pyautogui.hotkey('ctrl', 'enter')   

    time.sleep(10)
    driver.quit()

main()
