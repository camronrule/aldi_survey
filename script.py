from splinter import Browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pickle
import os.path

if not os.path.isfile('data.txt'): #if user data has not been saved before
    user_info = []
    print("Please enter the following information, pressing enter after each item:")
    print("First name:\nLast name:\nStreet address:\nCity\nZip code\nPhone number (no spaces, parentheses, or hyphens)\nEmail")
    import pickle
import os.path

if not os.path.isfile('data.pkl'): #if user data has not been saved before
    user_info = [None] * 7
    print("Please enter the following information, pressing enter after each item:")
    print("First name:\nLast name:\nStreet address:\nCity\nZip code\nPhone number (no spaces, parentheses, or hyphens)\nEmail")
    
    for i in range(7):
        user_info += input()

    #create file and pickle
    with open('data.pkl', 'wb') as f:
        pickle.dump(user_info, f)
        f.close()
    for i in range(7):
        user_info[i] = input()

    #create file and pickle
    with open('data.pkl', 'wb') as f:
        pickle.dump(user_info, f)
        f.close()

#take in the survey code
print('Please enter the code located on the bottom of the receipt')
print('Enter the code separated by hyphens, with no other characters')
print('e.g., 0123-456-789-012-345')
#receipt_code = input().split('-')
receipt_code = ["2685","480","002","005","016"]

#take in survey date
print('Please enter the date on the receipt in DD-MM-YYYY format, separated by hyphens')
print('e.g., 06-20-2023')
#receipt_date = input().split('-')
receipt_date = ["09","01","23"]

#take in survey time
print("Please enter the time the survey was printed, by typing 0, 1, 2, or 3")
print("0: 8AM-12PM")
print("1: 12PM-3PM")
print("2: 3PM-5PM")
print("3: 5PM-9PM")
#receipt_time = input()
receipt_time = "0"

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

#select the chosen number of boxes, in a random order
while counter <= NUM_CHECKBOXES_TO_SELECT:
    checkbox_index = r.randint(0, (len(checkboxes)-1))
    browser.find_by_css('label.ui-checkbox')[r.randint(0, (len(checkboxes)-1))].check()
    counter+=1

browser.find_by_id('nextPageLink').first.click() #next

#rate satisfaction with location
browser.find_by_css('div.last')[1].click()

#rate recommending to a friend
browser.find_by_css('div.last')[2].click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(1.5)
#skip page describing experience
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(1.5)
#rate cleanliness of store
browser.find_by_css('div.last')[1].click()

#rate neatness of store
browser.find_by_css('div.last')[2].click()

#rate ease of moving in the store
browser.find_by_css('div.last')[3].click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(1.5)
#rate friendliness of staff
browser.find_by_css("div.last")[1].click()

#rate happiness with quality of products
browser.find_by_css('div.last')[2].click()

#were products in stock
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(1.5)
#did the cashier handle product well
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(1.5)
#time spent at checkout met my expectations
browser.find_by_css('div.last').click()

#did the cashier ring things up correctly
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

##################################
time.sleep(1.5)
#were cleaning wipes available
browser.find_by_text("1").click()

#was hand sanitizer available
browser.find_by_text("1").last.click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(1.5)
#what is ur experience with aldi app
browser.find_by_text("I know ALDI has a mobile app but I have never used it").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(1.5)
#what is ur experience with aldi grocery delivery
browser.find_by_text("I know ALDI has grocery delivery but I have never tried it").click()

#what is ur familiarity with aldi curbside pickup
browser.find_by_text("I know ALDI has curbside pickup but I have never tried it").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(1.5)
#describe what products you want (optional)
browser.find_by_id('nextPageLink').first.click() #next

####################################
time.sleep(1.5)
#demographic page
#age (18-24)
browser.find_by_text("18 to 24").click()

#how often do you shop at aldi (1+ /week)
browser.find_by_text("One or more times per week").click()

#do you have any children (no)
browser.find_by_text("No").click()

#household income (25-50k)
browser.find_by_css('div.menuItem').last.click()
#browser.find_by_text("$")[2].click()
browser.find_by_id('nextPageLink').first.click() #next

####################################
time.sleep(1.5)

#would you like to enter for gift card
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(1.5)
browser.find_by_text("Yes").click()
time.sleep(5)

#retrieve user info in case it was already stored
with open('data.pkl', 'rb') as f:
    user_info = pickle.load(f)

    key = Keys()

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
    browser.type('promptField', key.TAB)
    time.sleep(.5)

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