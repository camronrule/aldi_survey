import re
from splinter import Browser
import time


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
print("Please enter the hour the receipt was printed, followed by 'AM' or 'PM'")
print('e.g., 11AM')
receipt_time = input()

#user info is stored already
#change this if others are using the program



#go to webpage
browser = Browser('chrome')
browser.visit('http://tellaldi.us')

#select language prompt
browser.find_by_id('option_934913_404244').first.click() #english
browser.find_by_id('nextPageLink').first.click() #next

#fill in code blanks
#browser.find_by_id('promptInput_386097_0').fill(receipt_code[0])
#browser.find_by_id('promptInput_386097_1').fill(receipt_code[1])
#browser.find_by_id('promptInput_386097_2').fill(receipt_code[2])
#browser.find_by_id('promptInput_386097_3').fill(receipt_code[3])
#browser.find_by_id('promptInput_386097_4').fill(receipt_code[4])

#fill in date
#browser.find_by_id('promptInput_386007').fill(receipt_code)

#fill in time
browser.find_by_text('8:00am').click() #select dropdown



time.sleep(10)