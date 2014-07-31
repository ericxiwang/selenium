from selenium import webdriver
import PyQt4
from selenium.webdriver.support.ui import Select
#from selenium.common.exception

from selenium.webdriver.common.keys import Keys

import time
import os

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://developer.ymcgames.com") # Load page

#elem = browser.find_element_by_id("login_email") # Find the query box
#elem.send_keys("eric@ymcnetwork.com" + Keys.RETURN)



time.sleep(0.2) # Let the page load, will be added to the API

#elem = browser.find_element_by_class_name("navicons")

browser.find_element_by_class_name("navicons").click()


###################### login module ######################
elem = browser.find_element_by_id("login_email")  #locate by id
elem.send_keys("eric@ymcnetwork.com")  #put in the text
elem = browser.find_element_by_id("login_password")  #same
elem.send_keys("q1w2e3r4")   #same
browser.find_element_by_id("login_button").click()  #click submit


###################### login end #########################



###################### select one game and enter #####################
browser.find_element_by_partial_link_text("YMC").click()

### switch into analytics ###

a = browser.find_element_by_partial_link_text('Analytics').click()
'''
time.sleep(2)

left_nav = browser.find_elements_by_css_selector('a')

print len(left_nav)'''

browser.find_element_by_partial_link_text('Reveune').click()

time.sleep(3)
'''
browser.find_element_by_partial_link_text("Revenue").click()

time.sleep(3)

browser.find_element_by_partial_link_text("ARPU").click()

time.sleep(3)

browser.find_element_by_partial_link_text("ARPPU").click()

time.sleep(3)
'''
##################### se

time.sleep(1)




time.sleep(2)
#browser.close()
