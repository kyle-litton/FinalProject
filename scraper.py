from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#change my name to your username
driver_path = "/Users/kylelitton/FinalProject/chromedriver"
browser = webdriver.Chrome(driver_path)

browser.get("http://sis.rutgers.edu/soc/#subjects?semester=92019&campus=NB&level=U")
browser.implicitly_wait(30)
browser.find_element_by_xpath("""//*[@id="widget_dijit_form_FilteringSelect_0"]/div[1]/input""").click()

dropDown = browser.find_element_by_xpath("""//*[@id="dijit_form_FilteringSelect_0_popup"]""")

options = [x for x in dropDown.find_elements_by_css_selector(".dijitReset.dijitMenuItem")]

#iterate over each option in drop down menu
count = 0

while count < len(options):
    
    time.sleep(2)
    dropDown = browser.find_element_by_xpath("""//*[@id="dijit_form_FilteringSelect_0_popup"]""")
    options = [x for x in dropDown.find_elements_by_css_selector(".dijitReset.dijitMenuItem")]
    options[count].click()


    browser.find_element_by_xpath("""//*[@id="widget_dijit_form_FilteringSelect_0"]/div[1]/input""").click()
    
    count = count + 1

    
browser.quit()