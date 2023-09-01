import re
from splinter import Browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random


#take in the survey code
print('Please enter the code located on the bottom of the receipt')
print('Enter the code separated by hyphens, with no other characters')
print('e.g., 0123-456-789-012-345')
receipt_code = input().split('-')

#take in survey date
print('Please enter the date on the receipt in DD-MM-YYYY format, separated by hyphens')
print('e.g., 06-20-2023')
receipt_date = input().split('-')

#take in survey time
print("Please enter the time the survey was printed, by typing 0, 1, 2, or 3")
print("0: 8AM-12PM")
print("1: 12PM-3PM")
print("2: 3PM-5PM")
print("3: 5PM-9PM")
receipt_time = input()

#user info is stored already
#change this if others are using the program


#go to webpage
browser = Browser('chrome')
browser.visit('http://tellaldi.us')
driver = browser.driver


#select language prompt
browser.find_by_id('option_934913_404244').first.click() #english
browser.find_by_id('nextPageLink').first.click() #next

#fill in code blanks
browser.find_by_id('promptInput_386097_0').fill(receipt_code[0])
browser.find_by_id('promptInput_386097_1').fill(receipt_code[1])
browser.find_by_id('promptInput_386097_2').fill(receipt_code[2])
browser.find_by_id('promptInput_386097_3').fill(receipt_code[3])
browser.find_by_id('promptInput_386097_4').fill(receipt_code[4])

#fill in date
browser.find_by_id('promptInput_386007').fill(receipt_date)

#fill in time
element_times = browser.find_by_id('prompt_content_386008').first #select dropdown


#determine which option to select
#856927 is the first option, with the following options
#incrementing by one
option = 856927+(int(receipt_time))
element_times.select(str(option))



#next page
browser.find_by_id('nextPageLink').first.click() #next

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.css, 'label[class="ui-checkbox"]')))

#what areas did you visit in the store
r = random.SystemRandom()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, 'label.ui-checkbox')))
checkboxes = browser.find_by_css('label.ui-checkbox')
number_of_loops = r.randint(1,11) # randomly choose the number of checkboxes that will be selected
counter = 1

NUM_CHECKBOXES = 11
NUM_CHECKBOXES_TO_SELECT = 3

print("Number of checkboxes found:")
print(len(browser.find_by_css('label.ui-checkbox')))

#select the chosen number of boxes, in a random order
while counter <= NUM_CHECKBOXES_TO_SELECT:
    checkbox_index = r.randint(0, (len(checkboxes)-1))
    print("clicking checkbox index:", checkbox_index)
    browser.find_by_css('label.ui-checkbox')[r.randint(0, (len(checkboxes)-1))].check()
    counter+=1
    time.sleep(1) 

element_rate = browser.find_by_id('nextPageLink').first.click() #next

#rate satisfaction with location
browser.find_by_css('div.last')[1].click()
#element_rate = browser.find_by_id("prompt_484675")
#element_rate.select("1114559")

time.sleep(5)

#rate recommending to a friend
browser.find_by_css('div.last')[2].click()
#element_rate.select("1114564")

time.sleep(5)


browser.find_by_id('nextPageLink').first.click() #next
#skip page describing experience
browser.find_by_id('nextPageLink').first.click() #next

#rate cleanliness of store
element_rate = browser.find_by_id("prompt_484678")
element_rate.select("1114574")

#rate neatness of store
element_rate = browser.find_by_id("484679")
element_rate.select("1114579")

#rate ease of moving in the store
element_rate = browser.find_by_id("484680")
element_rate.select("1114584")

browser.find_by_id('nextPageLink').first.click() #next

#rate friendliness of staff
element_rate = browser.find_by_id("485082")
element_rate.select("1115609")

#rate happiness with quality of products
element_rate = browser.find_by_id("484681")
element_rate.select("1114589")

#rate time at checkout
element_rate = browser.find_by_id("484682")
element_rate.select("1114594")

browser.find_by_id('nextPageLink').first.click() #next

#were products in stock
element_yn = browser.find_by_id("prompt_485081")
element_yn.select("1115603")

#did the cashier handle product well
element_yn = browser.find_by_id("prompt_485083")
element_yn.select("1114595")

#did the cashier ring things up correctly
element_yn = browser.find_by_id("prompt_386747")
element_yn.select("858735")

browser.find_by_id('nextPageLink').first.click() #next

#were cleaning wipes available
element_yn = browser.find_by_id("prompt_449830")
element_yn.select("1036834")

#was hand sanitizer available
element_yn = browser.find_by_id("prompt_461204")
element_yn.select("1061008")

browser.find_by_id('nextPageLink').first.click() #next

#what is ur experience with aldi app
element_mult = browser.find_by_id("prompt_485291")
element_mult.select("1115949")

browser.find_by_id('nextPageLink').first.click() #next

#what is ur experience with aldi grocery delivery
element_mult = browser.find_by_id("prompt_485301")
element_mult.select("1115981")

#what is ur familiarity with aldi curbside pickup
element_mult = browser.find_by_id("prompt_485303")
element_mult.select("1115989")

browser.find_by_id('nextPageLink').first.click() #next

#describe what products you want (optional)
browser.find_by_id('nextPageLink').first.click() #next

#demographic page
#age (18-24)
element_mult = browser.find_by_id("prompt_386076")
element_mult.select("857079")

#how often do you shop at aldi (1+ /week)
element_mult = browser.find_by_id("prompt_485306")
element_mult.select("1115997")

#do you have any children (no)
element_mult = browser.find_by_id("prompt_485308")
element_mult.select("1116006")

#household income (25-50k)
element_mult = browser.find_by_id("prompt_485309")
element_mult.select("1116008")

browser.find_by_id('nextPageLink').first.click() #next

#would you like to enter for gift card
element_mult = browser.find_by_id("prompt_403404")
element_mult.select("932876")

#fill in name, address
browser.find_by_id('prompt_386083').fill("Camron") #first name
browser.type(Keys.TAB)
browser.type("Rule") #last name
browser.type(Keys.TAB)
browser.type("8629 Millstream Drive") #address
browser.type(Keys.TAB)
browser.type("Glen Allen") #city

browser.find_by_id("prompt_386750") #select state dropdown
browser.type("v")
browser.type(Keys.TAB)

browser.find_by_id("prompt_386088").fill("23228") #select zip code box
browser.type(Keys.TAB)

browser.type("8049379066")
browser.type(Keys.TAB)

browser.type("camronrule@gmail.com")
browser.type(Keys.TAB) #move to ask about subscribing to email list
browser.type(Keys.ENTER) #submit page

#do you agree to privacy policy
element_mult = browser.find_by_id("494324")
element_mult.select("1135070")

browser.find_by_id('nextPageLink').first.click() #next



time.sleep(10)