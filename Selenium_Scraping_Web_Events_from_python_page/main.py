from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chromer_driver_path = "C:/Users/Serhan/Documents/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromer_driver_path))
driver.get('https://www.python.org/')

time = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
text = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
time_list = [event.get_attribute("datetime").split("T")[0] for event in time]
text_list = [text.text for text in text]
print(time_list)
print(text_list)
# bez list comprehension
final_dict = {}
for i in range(len(time_list)):
    final_dict[i]={
        'time':time_list[i],
        'name':text_list[i]
    }
#----------------------------------------------
final_dict={i:{'time':time_list[i], 'name':text_list[i]} for i in range(len(time_list))} #sus list comrpehension
#----------------------------------------------
print(final_dict)
#----------------------------------------------------------------------------
# ako nqmam driverite
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#----------------------------------------------------------------------------

# driver.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/?_encoding=UTF8&pd_rd_w=aD5Jb&content-id=amzn1.sym.6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_p=6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_r=QM5EE95G9JVHW3TWHJFQ&pd_rd_wg=KUzMh&pd_rd_r=6f77a9a6-a40e-44c4-a9bf-90e7b37ce04b&ref_=pd_gw_ci_mcx_mr_hp_d")
# price = driver.find_element(By.XPATH,"//td[@class='a-span12']")
# price_1 = driver.find_element(By.CSS_SELECTOR, "span.a-offscreen+span")
# xpath_price = driver.find_element(By.XPATH,'//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
# print(price.text)
# print(price_1.text)
# print(xpath_price.text)
# driver.close() # close va 1 tab
# driver.quit() # close va vsichki tabove
