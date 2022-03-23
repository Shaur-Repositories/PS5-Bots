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
driver= webdriver.Chrome(options=options,executable_path=r"\Drivers\chromedriver91.exe")#drive path
#driver.get(r"https://shopatsc.com/products/sony-wi-c200-wireless-bluetooth-in-ear-headphones-with-mic-15-hours-battery-life-quick-charge-magnetic-earbuds-tangle-free-cord-and-with-1-year-warranty?variant=32556887277707")
driver.get(r"https://shopatsc.com/collections/playstation-5/products/playstation-5-console-store")

while True: 
    try:
        driver.find_element_by_id("pincode_input")
    except NoSuchElementException:
        print("not yet")
        driver.refresh()
    else:
        print("yes")
        break

driver.find_element_by_id("pincode_input").send_keys("111111") #pin code
driver.find_element_by_id("check-delivery-submit").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/input[1]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Cart')]"))).click()
#driver.find_element_by_xpath("//a[contains(text(),'View Cart')]").click()
driver.find_element_by_id("checkout_button").click()



"""
To Log in
driver.find_element_by_partial_link_text("Log in").click()
driver.find_element_by_id("customer_email").send_keys("Email") #email
driver.find_element_by_id("customer_password").send_keys("pass") #pass
driver.find_element_by_xpath("//input[@value='Login']").click()
driver.find_element_by_id("continue_button")
"""


driver.find_element_by_id("checkout_email").send_keys("email")
driver.find_element_by_id("checkout_shipping_address_first_name").send_keys("fname")
driver.find_element_by_id("checkout_shipping_address_last_name").send_keys("lname")
driver.find_element_by_id("checkout_shipping_address_address1").send_keys("Address -1 ")
driver.find_element_by_id("checkout_shipping_address_address2").send_keys("Address -2")
driver.find_element_by_id("checkout_shipping_address_city").send_keys("Address -3")
driver.find_element_by_id("checkout_shipping_address_province").send_keys("Address -4")
driver.find_element_by_id("checkout_shipping_address_phone").send_keys("1234567890") #phn no
driver.find_element_by_id("checkout_remember_me").click()

driver.find_element_by_id("continue_button").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "continue_button"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "continue_button"))).click()


print("end")