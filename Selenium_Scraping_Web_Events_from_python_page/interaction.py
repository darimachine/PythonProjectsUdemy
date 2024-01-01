from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.CSS_SELECTOR,'a[title="Special:Statistics"]')
#articles = driver.find_element(By.CSS_SELECTOR,'#articlecount a[1]')
print(type(articles.text))
print(int(articles.text.replace(",","")))
