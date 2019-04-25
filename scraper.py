from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
    
    time.sleep(1)
    dropDown = browser.find_element_by_xpath("""//*[@id="dijit_form_FilteringSelect_0_popup"]""")
    options = [x for x in dropDown.find_elements_by_css_selector(".dijitReset.dijitMenuItem")]
    #this fixes the scroll issue
    browser.execute_script("arguments[0].scrollIntoView(true);",options[count])
    options[count].click()

    #get each class list
    courseList = [x for x in browser.find_elements_by_css_selector(".courseExpandIcon")]

    dropCount = 0
    while dropCount < len(courseList):
        
        time.sleep(1)
        courseList = [x for x in browser.find_elements_by_css_selector(".courseExpandIcon")]
        browser.execute_script("arguments[0].scrollIntoView(true);",courseList[dropCount])
        courseList[dropCount].find_element(By.TAG_NAME, 'img').click()
        dropCount = dropCount+1

        meetingTimeList = [x for x in browser.find_elements_by_css_selector(".sectionMeetingTimesDiv")]
        numCoursesList = [x for x in browser.find_elements_by_class_name("courseOpenSectionsDenominator")]
        
        numStr = numCoursesList[dropCount].text[2:]
        timeCount = 0
      
        while timeCount < int(numStr):
            time.sleep(1)
            meetingTimeList = [x for x in browser.find_elements_by_css_selector(".sectionMeetingTimesDiv")]
            browser.execute_script("arguments[0].scrollIntoView(true);",meetingTimeList[timeCount])
            dayList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeDay')
            hoursList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeHours')
            campusList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeCampus')
            buildingAndRoomList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeBuildingAndRoom')
            timeCount = timeCount+1


            scrapeCount = 0

            while scrapeCount < len(dayList):
                dayList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeDay')
                hoursList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeHours')
                campusList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeCampus')
                buildingAndRoomList = meetingTimeList[timeCount].find_elements(By.CLASS_NAME, 'meetingTimeBuildingAndRoom')
                print(dayList[scrapeCount].text, hoursList[scrapeCount].text, campusList[scrapeCount].text, buildingAndRoomList[scrapeCount].text)
                scrapeCount = scrapeCount+1
            
            print('-----------------')


           
      
           



    browser.find_element_by_xpath("""//*[@id="widget_dijit_form_FilteringSelect_0"]/div[1]/input""").click()
    
    count = count + 1

    
browser.quit()