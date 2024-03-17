from selenium import webdriver
import pandas as pd  
from selenium.webdriver.support.ui import Select
import time

df = pd.read_excel('data.xlsx') #read excel file name data.xlsx

browser = webdriver.Chrome() #for opening the browser
browser.get('https://demoqa.com/automation-practice-form')

for i in df.index:
    entry = df.loc[i]
     
    #For Name  
    fname_input = browser.find_element("id", 'firstName')
    fname_input.send_keys(entry['First name'])

    lname_input = browser.find_element("id", 'lastName')
    lname_input.send_keys(entry['Last name'])
    
    #For Email
    email_input = browser.find_element("id", 'userEmail')
    email_input.send_keys(entry['Email'])

    #For Gender
    gender_xpath = f"//input[@name=\"gender\"][@value=\"{entry['Gender']}\"]"
    gender_input = browser.find_element("xpath", gender_xpath)
    gender_input.click()

    #For Mobile
    mobile_input = browser.find_element("id", 'userNumber')
    mobile_input.send_keys(entry['Mobile'])

    #For Hobby
    hobbies_str = entry['Hobbies']
    hobbies = hobbies_str.split(', ')

    for h in hobbies:
        hobby_xpath = f"//input[@type=\"checkbox\"][@value=\"{h}\"]"
        hobby_input = browser.find_element("xpath", hobby_xpath)
        hobby_input.click()

    #For Address
    address_input = browser.find_element_by_id('currentAddress')
    address_input.send_keys(entry['Current Address'])

    time.sleep(15)

    #For Submit
    submit_btn = browser.find_element_by_css_selector('input[type="submit"]')
    submit_btn.click() 

  




