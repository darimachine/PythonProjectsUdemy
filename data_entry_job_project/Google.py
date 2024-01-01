import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
FORMULQR_URL = "https://forms.gle/gNSEL1FM2qUDWpP66"
class FillForm():
    def __init__(self):
        self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.__driver.get(FORMULQR_URL)
        self.__wait = WebDriverWait(self.__driver,15)
    def fill_form(self,link,adres,price):
        for index in range(len(link)-1):
            link_entry = self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
            adress_entry = self.__wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            price_entry = self.__wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            submit_btn = self.__wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'RveJvd')))
            adress_entry.send_keys(adres[index])
            price_entry.send_keys(price[index])
            link_entry.send_keys(link[index])
            submit_btn.click()
            another_form = self.__wait.until(EC.visibility_of_element_located((By.TAG_NAME,'a')))
            another_form.click()

