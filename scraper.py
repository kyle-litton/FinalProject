from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "/Users/kylelitton/FinalProject/chromedriver"
browser = webdriver.Chrome(driver_path)

browser.get("http://sis.rutgers.edu/soc/#subjects?semester=92019&campus=NB&level=U")
browser.implicitly_wait(10)
browser.find_element_by_xpath("""//*[@id="widget_dijit_form_FilteringSelect_0"]/div[1]/input""").click()



