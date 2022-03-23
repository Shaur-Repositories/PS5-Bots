from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time


options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': { 'images': 2, }}
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver= webdriver.Chrome(options=options,executable_path=r"\Drivers\chromedriver91.exe")#driver path


#login
driver.get("https://www.gamestheshop.com/")
driver.find_element_by_id("ctl00_lblSIGNIN").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtEmail").send_keys("email") #email
driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtPassword").send_keys("pass") #pass
driver.find_element_by_id("ctl00_ContentPlaceHolder1_chksignin").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSubmit").click()

driver.get("https://www.gamestheshop.com/PlayStation-5-Console/5111")
#driver.get("https://www.gamestheshop.com/Gears-5-for-XBOX-ONE/3303")
#driver.get("https://www.gamestheshop.com/Sparkfox-Premium-Braided-Data--Charge-Cable-Essential-accessories-for-use-with-PlayStation-5-/5346")




#set pin
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Check Pincode Serviceability')]"))
    ).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPincode"))).send_keys("111111")#pin code
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_btnPinSubmit"))).click()
driver.find_element_by_xpath("//body/form[@id='aspnetForm']/div[@id='divMessagePopup']/div[@id='LightBoxTopCrossDiv']/a[1]/img[1]").click()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_divOfferDetails"))).click()
a=driver.find_element_by_id("ctl00_ContentPlaceHolder1_divOfferDetails")
images = a.find_elements_by_tag_name('img')
#loop
while True:
    a=driver.find_element_by_id("ctl00_ContentPlaceHolder1_divOfferDetails")
    images = a.find_elements_by_tag_name('img')
    print(images)
    for image in images:
        imag=image.get_attribute('src')
    print(imag)
    
    if(imag == "https://s3-ap-southeast-1.amazonaws.com/cdn.gamestheshop.com/image/in-stock.png" or imag =="https://s3-ap-southeast-1.amazonaws.com/cdn.gamestheshop.com/image/offer-available.png"):
        break
    elif(imag=="https://s3-ap-southeast-1.amazonaws.com/cdn.gamestheshop.com/image/sold-out.png"):
        driver.refresh()
    else:
        print("new image found")

 
    
        


#WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
 #                       .until(EC.presence_of_element_located((By.CLASS_NAME, "addToCart-nw addToCart-nw-dv bo errorherebg-blu")))

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ADD TO CART')]"))
   ).click()

#a.find_element_by_class_name("addToCart-nw addToCart-nw-dv bo errorherebg-blu").click()


#after cart add
driver.find_element_by_id("spnItemCount").click()
#driver.find_element_by_id("ctl00_ContentPlaceHolder1_clsProcChkout").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "spnItemCount"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_clsProcChkout"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnLoggedinContinue"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'SHIP MY ORDER TO THIS ADDRESS')]"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnShippingContinue"))).click()
'''
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "divProceedToPayment"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "txtEmailpaytm"))).send_keys("abc@gmail.com")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "txtMobpaytmInput"))).send_keys("1234567890") Phone no.
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "btnPayPaytm"))).submit()
'''
