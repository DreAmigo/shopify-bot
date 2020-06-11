import urllib, json
from selenium import webdriver
import time
start = time.time()

##
# User Information 
##
first_name='Name';
family_name='Last Name';
email='youremail@gmail.com';
address='12345 Some Street';
country='AU';
city='Mermaid Beach';
postcode='4218';
state='QLD';
mobile='0421667754';
CCNumber="1"
CCName="Test"
CCExpiry="11/25"
CCVerification="123"

##
# Site information
##
domain = "https://www.culturekings.com.au"
handle = 'jordan-jordan-air-jordan-1-mid-black-red-white-2'
url = domain + "/products/" + handle + ".json"

##
# Product information
##
shoeSize = "18"
quantity = "1"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--headless") # Comment that line to see script running in Chrome.
driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)

response = urllib.urlopen(url)
data = json.loads(response.read())

checkoutDetails = 'checkout[shipping_address][first_name]='+ first_name +'&checkout[shipping_address][last_name]='+ family_name +'&checkout[email]='+ email +'&checkout[shipping_address][address1]='+ address +'&checkout[shipping_address][city]='+ city +'&checkout[shipping_address][zip]='+ postcode +'&checkout[shipping_address][country_code]='+ country +'&&checkout[shipping_address][province_code]='+ state +'&checkout[shipping_address][phone]='+ mobile;

for i in data['product']['variants']: 
    if ((i['inventory_quantity'] > 0) and (i['title'] == shoeSize)):
        link = domain + '/cart/'+ str(i['id']) +':'+ quantity +'?'+ checkoutDetails;
        driver.get(link)

        # Add to Cart
        print('1. Added to the cart...');
        
        # Click continue to shipping
        time.sleep(3)
        driver.find_element_by_id('continue_button').click()
        print('2. Selecting Shipping...');
        
        # Click continue to Payment
        time.sleep(3)
        driver.find_element_by_id('continue_button').click()
        print('3. Filling up Payment...');
        
        # Same as shipping address
        time.sleep(4)

        # Find CC details
        driver.find_element_by_id('checkout_different_billing_address_false').click() # Same as shipping address
        driver.find_element_by_xpath("//*[contains(@id, 'checkout_payment_gateway_')]").click(); # Click by Credit Card

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-number-')]"))
        driver.find_element_by_id("number").send_keys(CCNumber);

        driver.switch_to.parent_frame();

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-name-')]"))
        driver.find_element_by_id("name").send_keys(CCNumber);

        driver.switch_to.parent_frame();

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-expiry-')]"))
        driver.find_element_by_id("expiry").send_keys(CCExpiry);

        driver.switch_to.parent_frame();

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-verification_value-')]"))
        driver.find_element_by_id("verification_value").send_keys(CCVerification);

        print('4. Credit Card details ready...');
        driver.switch_to.parent_frame();

        # try to process payment.
        driver.find_element_by_id('continue_button').click()
        print('5. Processing payment...');

        time.sleep(8)
        
        # Pray to work ;) 
        order = driver.find_element_by_xpath("//span[@class='os-order-number']").get_attribute('innerHTML');
        print(order);
        print('Checkout total: ', time.time()-start, 'seconds.')