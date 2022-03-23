from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': { 'images': 2, 'javascript': 2, 
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
driver= webdriver.Chrome(options=options,executable_path=r"\Drivers\chromedriver91.exe") #driver path
driver.get("https://www.amazon.in/gp/product/B08FV5GC28")#product page
first=driver.find_element_by_id("nav-link-accountList")
first.click()
email=driver.find_element_by_id("ap_email")
email.send_keys("abc@gmail.com")#email id
continuee=driver.find_element_by_id("continue")
continuee.click()
password=driver.find_element_by_id("ap_password")
password.send_keys("pass")#password
remme=driver.find_element_by_name("rememberMe")
remme.click()
siginbtn=driver.find_element_by_id("signInSubmit")
siginbtn.click()



while True:   
    try:
        buynow=driver.find_element_by_id("buy-now-button")
    except NoSuchElementException:
        print("not yet")
        driver.refresh()
    else:
        print("yes")
        buynow.click()
        break
        
address=driver.find_element_by_id("address-book-entry-0")
addresbtn=address.find_element_by_link_text("Deliver to this address")
addresbtn.click()
addcvv=driver.find_element_by_name("addCreditCardVerificationNumber0")
addcvv.send_keys("123")#cvv no.

revieworder=driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
revieworder.click()

try:
    placeorder = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "placeYourOrder"))
    )
except:
    print()
    
#placeorder=driver.find_element_by_id("placeYourOrder")
placeorder.click()
print(driver.title)
