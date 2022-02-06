from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#EXCEPTION TREAT
from selenium.common.exceptions import NoSuchElementException

#USED TO ORDER PRODUCTS
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

#CONFIG
username = "standard_user"
password = "secret_sauce"
url = "https://www.saucedemo.com/"

#OPEN BROWSER
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#INSERT USERNAME
username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]');
username_field.send_keys(username);

#INSERT PASSWORD
username_field = driver.find_element(By.XPATH, '//*[@id="password"]');
username_field.send_keys(password);

#LOGIN
login_btn = driver.find_element(By.XPATH, '//*[@id="login-button"]');
login_btn.click();

#ORDER BY PRICE (low to high)
filter_btn = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select');
filter_options = Select(filter_btn);
filter_options.select_by_visible_text('Price (low to high)')


#ADD PRODUCTS ONE BY ONE

#FIND FIRST PRODUCT
#product1 = driver.find_element(By.NAME , 'add-to-cart-sauce-labs-onesie');
#product1.click();

#FIND SECOND PRODUCT
#product1 = driver.find_element(By.NAME , 'add-to-cart-test.allthethings()-t-shirt-(red)');
#product1.click();


#ADD PRODUCTS IN LIST
products = ['sauce-labs-onesie', 'test.allthethings()-t-shirt-(red)'];
print(products);

for i in products:
    name = 'add-to-cart-' + i;
    print(name);
    try:
        element = driver.find_element(By.NAME , name);
        element.click();
    except NoSuchElementException as ex:
        print(ex);

input();