from asyncio.constants import ACCEPT_RETRY_DELAY
from ftplib import all_errors
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

url = 'https://www.4icu.org/us/universities/'


# GET UNIVERSITIES LINKS
def get_all_links():

    driver.get(url)

    try: 
        
        loader = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/div[2]/table"))
        )
       
        container = driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/table')

        all_links = container.find_elements(By.TAG_NAME,'a')
        
        outerlinks = []

        for link in all_links:
            outerlinks.append(link.get_attribute('href'))

        print(outerlinks,"outerlinks")

        for link in outerlinks:
            driver.get(link)

            loader = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[5]/div/div[2]/div"))
            )
            container_inner = driver.find_element(By.XPATH,'/html/body/div/div[5]/div/div[2]/div')
            all_links_inner = container_inner.find_elements(By.TAG_NAME,'a')

            for link_inner in all_links_inner:
                links.append(link_inner.get_attribute('href'))
            
        print(links,"links")

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
   
get_all_links()