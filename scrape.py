from asyncio.constants import ACCEPT_RETRY_DELAY
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys
from datetime import datetime 
import json


driver = webdriver.Chrome("C:\\Program Files\\chromedriver.exe")
driver.maximize_window()


page_counter=1

items = []
links = []

# url = 'https://www.4icu.org/reviews/4950.htm'


# Opening JSON file
f = open('links.json')
 
# returns JSON object as
# a dictionary
links = json.load(f)

links = ["https://www.4icu.org/reviews/16896.htm"]


def scrapeuniversity(page_counter = 0):
    
    l = links[page_counter]
    if "reviews" not in l:
        scrapeuniversity(page_counter + 1)

    try:
        
        driver.get(l)

        title = ""
        img = ""
        country_rank=""
        world_rank= ""
        description= ""
        address= ""
        tel= ""
        fax= ""
        acr= ""
        founded_year= ""
        motto= ""
        colors= ""
        screenshot= ""
        site_link= ""
        gender= ""
        international_students= ""
        selection_types= ""
        admission_requirements= ""
        admission_rate= ""
        admission_office= ""
        student_enrollment= ""
        academic_staff= ""
        control_type= ""
        entity_type= ""
        academy_calendar= ""
        campus_setting= ""
        religious_affiliation= ""


        # BASIC
        try:
            title = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[2]/h1')
            title = title.text
        except: 
            pass
        
        try:
            img = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[1]/div/a/picture/img')
            img = img.get_attribute('src')
        except: 
            pass

        try:
            country_rank = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/a/strong')
            country_rank = country_rank.text
        except: 
            pass
        
        try:
            world_rank = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/a/strong')
            world_rank=world_rank.text
        except: 
            pass



        # DESCRIPTION
        try:
            description = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[2]/p')
            description = description.text
        except: 
            pass

        # LOCATION
        try:
            address = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td')
            address=address.text
        except: 
            pass

        try:
            tel = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td')
            tel=tel.text
        except: 
            pass

        try:
            fax = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td')
            fax=fax.text
        except: 
            pass


        # IDENTITY
        try:
            acr = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[2]/td')
            acr=acr.text
        except: 
            pass

        try:
            founded_year = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[3]/td')
            founded_year=founded_year.text
        except: 
            pass

        try:
            motto = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[4]/td')
            motto=motto.text
        except: 
            pass
        
        try:
            colors = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[5]/td')
            colors=colors.text
        except: 
            pass

        try:
            screenshot = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[6]/td/a/picture/img')
            screenshot=screenshot.get_attribute('src')
        except: 
            pass
        
        try:
            site_link = driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div/div[2]/table/tbody/tr[6]/td/a')
            site_link=site_link.get_attribute('href')
        except: 
            pass


        # ADMISSIONS

        try:
            gender = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[1]/td')
            gender=gender.text
        except: 
            pass
        
        try:
            international_students = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[2]/td')
            international_students=international_students.text
        except: 
            pass

        try:
            selection_types = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[3]/td')
            selection_types=selection_types.text
        except: 
            pass

        try:
            admission_requirements = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[4]/td')
            admission_requirements=admission_requirements.text
        except: 
            pass

        try:
            admission_rate = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[5]/td')
            admission_rate=admission_rate.text
        except: 
            pass

        try:
            admission_office = driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div[2]/div/div[2]/table/tbody/tr[6]/td')
            admission_office=admission_office.text
        except: 
            pass
        
        # SIZE AND PROFILE
        try:
            student_enrollment = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[1]/td')
            student_enrollment=student_enrollment.text
        except: 
            pass

        try:
            academic_staff = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[2]/td')
            academic_staff=academic_staff.text
        except: 
            pass

        try:
            control_type = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[3]/td')
            control_type=control_type.text
        except: 
            pass

        try:
            entity_type = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[1]/table/tbody/tr[4]/td')
            entity_type=entity_type.text
        except: 
            pass

        try:
            academy_calendar = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[2]/table/tbody/tr[1]/td')
            academy_calendar=academy_calendar.text
        except: 
            pass

        try:
            campus_setting = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[2]/table/tbody/tr[2]/td')
            campus_setting=campus_setting.text
        except: 
            pass

        try:
            religious_affiliation = driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[2]/div/div[2]/table/tbody/tr[3]/td')
            religious_affiliation=religious_affiliation.text
        except: 
            pass

          

        item = {
            "title": title,
            "img":img, 
            "country_rank":country_rank,
            "world_rank":world_rank,
            "description":description,
            "address":address,
            "tel":tel,
            "fax":fax,
            "acr":acr,
            "founded_year":founded_year,
            "motto":motto,
            "colors":colors,
            "screenshot":screenshot,
            "site_link":site_link,
            "gender":gender,
            "international_students":international_students,
            "selection_types":selection_types,
            "admission_requirements":admission_requirements,
            "admission_rate":admission_rate,
            "admission_office":admission_office,
            "student_enrollment":student_enrollment,
            "academic_staff":academic_staff,
            "control_type":control_type,
            "entity_type":entity_type,
            "academy_calendar":academy_calendar,
            "campus_setting":campus_setting,
            "religious_affiliation":religious_affiliation
        }

        items.append(item)

        with open('items.json', 'w') as outfile:
            json_items = json.dumps(items, indent = 4)
            outfile.write(json_items)

        scrapeuniversity(page_counter+1)
        
    except Exception as e:
        print("Error:",e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)

        scrapeuniversity(page_counter+1)
        # driver.quit()

    


        




def get_all_links(page_counter):

  
   


    try: 

        loader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "archive-property-item"))
        )
       


    except Exception as e:
        print("Error:",e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
       
      

    finally:
        pass
   
scrapeuniversity()