'''
This script automatically fills out the Aldi survey that is printed on
their receipts. The most positive answers are chosen. The survey asks for user info for
a chance to win a gift card. This information is taken at the beginning of the program and
stored in a pickle, if the user has not inputted it before. Options which are not subjective 
are chosen randomly. The user is able to provide a image.heic file and have the survey 
code be automatically loaded in using OCR through pytesseract.

Written by Camron Rule
Summer/Fall 2023
'''

from splinter import Browser
from selenium.webdriver.common.keys import Keys #necessary to type user data at end
from selenium.webdriver.support.ui import WebDriverWait #used to make sure that page is loaded before continuing (line 103)
from selenium.webdriver.support import expected_conditions as EC #same here
from selenium.webdriver.common.by import By #and here
import time #used to wait before choosing next function - although this may not be needed TODO!!!
import random #used to choose a random number of departments visited (line 102)
import pickle #used to store and load user data
import os.path #used to see if pickle file has been created (line 12)
import text #processes image.heic to get survey code


if not os.path.isfile('data.pkl'): #if user data has not been saved before
    user_info = [None] * 8
    print("========================================")
    print("Please enter the following information, pressing enter after each item:")
    print("First name:\nLast name:\nStreet address:\nCity\nState\nZip code\nPhone number (no spaces, parentheses, or hyphens)\nEmail\n")
    
    for i in range(7):
        user_info[i] = input()

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

print("========================================")
print("Would you like to provide a .heic image of your receipt?")
print("If not, you will have to input the survey code manually.")
print("Y / N")

receipt_code = []

if (input().upper() == "Y"):
    receipt_code = text.main().split('/')

else:
    #take in the survey code
    print("========================================")
    print('Please enter the code located on the bottom of the receipt')
    print('Enter the code separated by /, with no other characters')
    print('e.g., 0123/456/789/012/345\n')
    #receipt_code = input().split('-')
    receipt_code = ["2685","480","002","005","016"]

    #take in survey date
    print('Please enter the date on the receipt in DD-MM-YYYY format, separated by hyphens')
    print('e.g., 06-20-2023\n')
    #receipt_date = input().split('-')
    receipt_date = ["10","07","23"]

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
time.sleep(0.5)

#select type of survey - receipt 1 (only numbers in survey code)
browser.find_by_css('div.menuItem').first.click()
browser.find_by_id('nextPageLink').first.click() #next

#fill in code blanks
for i in range(0,5):
    browser.find_by_id('promptInput_386097_'+str(i)).fill(receipt_code[i])

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
time.sleep(.5)
#skip page describing experience
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(.5)
#rate cleanliness of store
browser.find_by_css('div.last')[1].click()

#rate neatness of store
browser.find_by_css('div.last')[2].click()

#rate ease of moving in the store
browser.find_by_css('div.last')[3].click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(.5)
#rate friendliness of staff
browser.find_by_css("div.last")[1].click()

#rate happiness with quality of products
browser.find_by_css('div.last')[2].click()

#were products in stock
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(.5)
#did the cashier handle product well
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

#################################
time.sleep(.5)
#time spent at checkout met my expectations
browser.find_by_css('div.last').click()

#did the cashier ring things up correctly
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

##################################
time.sleep(.5)
#were cleaning wipes available
browser.find_by_text("1").click()

#was hand sanitizer available
browser.find_by_text("1").last.click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(.5)
#what is ur experience with aldi app
browser.find_by_text("I know ALDI has a mobile app but I have never used it").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(.5)
#what is ur experience with aldi grocery delivery
browser.find_by_text("I know ALDI has grocery delivery but I have never tried it").click()

#what is ur familiarity with aldi curbside pickup
browser.find_by_text("I know ALDI has curbside pickup but I have never tried it").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(.5)
#describe what products you want (optional)
browser.find_by_id('nextPageLink').first.click() #next

####################################
time.sleep(.5)
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
time.sleep(.5)

#would you like to enter for gift card
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

###################################
time.sleep(.5)
browser.find_by_text("Yes").click()
time.sleep(0.5)

#retrieve user info in case it was already stored
with open('data.pkl', 'rb') as f:
    user_info = pickle.load(f)

    #fill in name, address
    browser.find_by_id('promptInput_386083').fill(user_info[0]) #first name
    browser.find_by_id('promptInput_386083').type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id('promptInput_386084').type(user_info[1]) #last name
    browser.find_by_id('promptInput_386084').type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id('promptInput_386085').type(user_info[2]) #address
    browser.find_by_id('promptInput_386085').type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id('promptInput_386086').type(user_info[3]) #city
    browser.find_by_id('promptInput_386086').type(Keys.TAB)
    time.sleep(.5)

    pulldown = browser.find_by_css("select") #select state dropdown
    pulldown.click()
    time.sleep(0.25)
    pulldown.type(user_info[4][0]) #first letter of state
    pulldown.type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id("promptInput_386088").fill(user_info[5]) #select zip code box
    browser.find_by_id("promptInput_386088").type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id('promptInput_386089').type(user_info[6]) #phone nunmber
    browser.find_by_id('promptInput_386089').type(Keys.TAB)
    time.sleep(.5)

    browser.find_by_id('promptInput_386090').type(user_info[7]) #email
    browser.find_by_id('promptInput_386090').type(Keys.TAB) 
    time.sleep(.5)

    browser.find_by_css('div.booleanText').click() #agree to emailing list
    browser.find_by_id('nextPageLink').first.click() #next
    time.sleep(.5)

################################

#do you agree to privacy policy
browser.find_by_text("Yes").click()
browser.find_by_id('nextPageLink').first.click() #next

#page changes to aldi.us if survey was submitted
if (browser.url == ('https://www.aldi.us')):
    print('Success! Thank you for using this program')
    print('  _________\n /         \\\n |  /\\ /\\  |\n |    -    |\n |  \\___/  |\n \\_________/'); #smiley face :)


time.sleep(1)