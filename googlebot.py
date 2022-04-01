from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("rose on the ground")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    driver.quit()
link = driver.find_element(By.PARTIAL_LINK_TEXT, "On The Ground")
link.click()

driver.back()
driver.forward()
while (1):   
        time.sleep(30)     
        driver.back()
        driver.forward()
    