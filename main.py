from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time
from credentials import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

driver = webdriver.Edge()
driver.get("https://www.linkedin.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")


username.send_keys(LINKEDIN_EMAIL)
password.send_keys(LINKEDIN_PASSWORD)
password.send_keys(Keys.RETURN)

time.sleep(20)


driver.get("https://www.linkedin.com/jobs")

time.sleep(5)

search_box = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search_box.send_keys("Data")
search_box.send_keys(Keys.RETURN)


##chatgpt code
# job_list = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
# job_cards = job_list.find_elements(By.TAG_NAME, "li")

time.sleep(10)
job_cards = driver.find_elements(By.XPATH, '//li[@data-occludable-job-id]')


id_list = []

for cards in job_cards:
     try:
         id = cards.get_attribute("data-occludable-job-id")
         id_list.append(id)
         
         print(f"JOB ID: {id}")
         
     except Exception as e:
         print(f"Error, {e}")
        
        
for ids in id_list:
    job_search = driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId={id}&geoId=106808692&keywords=data&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mt4"]'))
        )
        job_search_desc = driver.find_elements(By.XPATH, '//div[@class="mt4"]/p')
    
        for job_desc in job_search_desc:        
            desc = job_desc.find_elements(By.TAG_NAME, "span")
            print(len(desc))
            
            for descs in desc:
                print(descs.text)
    
    except Exception as e:
        print(f"Error, {e}")
        
    break
driver.quit()