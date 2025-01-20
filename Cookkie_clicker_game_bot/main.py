from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
def check_max(current_money):
    j=0
    for product_price in money_list:
        if current_money>product_price:
            j = money_list.index(product_price)
    return j

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
money = driver.find_elements(By.CSS_SELECTOR,'#store b ')
money_list= [int(i.text.split("-")[1].replace(",","").strip()) for i in money[:len(money)-1] ]
items = driver.find_elements(By.CSS_SELECTOR,'#store div')
id_list = [j.get_attribute("id") for j in items]
seconds = time.time() +1
end = time.time() +20
cookie = driver.find_element(By.ID, "cookie")
while end>=time.time():
    cookie.click()
    if seconds<time.time():
        my_money = driver.find_element(By.ID,"money")
        current_money = int(my_money.text.replace(",",""))
        package = driver.find_element(By.ID,id_list[check_max(current_money)])
        package.click()
        seconds = time.time() + 8
cookie_per_sec = driver.find_element(By.ID,"cps")
print(cookie_per_sec.text)
