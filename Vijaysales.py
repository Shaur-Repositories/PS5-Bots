
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
DRIVER_PATH=r"\Drivers\chromedriver91.exe"
#driver= webdriver.Chrome(DRIVER_PATH)

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': { 'images': 2, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2 }}
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver= webdriver.Chrome(options=options,executable_path=r"\Drivers\chromedriver91.exe")

driver.get("https://www.vijaysales.com/Login")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtSignInUsername"))).send_keys("phn no") #phone no.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtSignInPassword"))).send_keys("pass") # pass
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnSignInLogin"))).click()

driver.get("https://ps5.vijaysales.com/Sony-PS5-Console.html")
#driver.get("https://www.vijaysales.com/sony-ps4-bloodborne-game-of-the-year-edition/11312")
while True:   
    try:
        buynow=driver.find_element_by_id("ContentPlaceHolder1_btnAddToCart")
    except NoSuchElementException:
        print("not yet")
        driver.refresh()
    else:
        print("yes")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnAddToCart"))).click()
        break
    

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtPincode"))).send_keys("pin code ") #pin code
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ProceedtoPay"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rdo0"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "deliverhere0"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btngreenpay"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Radio6"))).click()

#debit card details
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "creditcard"))).send_keys("card no.")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtExpDate"))).send_keys("card exp date")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCvv"))).send_keys("cvv")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtOwnerName"))).send_keys("name on card")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnNewCardPay"))).click()
