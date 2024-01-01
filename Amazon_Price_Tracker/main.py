import requests
from bs4 import BeautifulSoup
import smtplib
URL = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/?_encoding=UTF8&pd_rd_w=aD5Jb&content-id=amzn1.sym.6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_p=6e9da02f-f7a3-444f-aea6-9ef09ed8bb89&pf_rd_r=QM5EE95G9JVHW3TWHJFQ&pd_rd_wg=KUzMh&pd_rd_r=6f77a9a6-a40e-44c4-a9bf-90e7b37ce04b&ref_=pd_gw_ci_mcx_mr_hp_d"
MY_PRICE = 120
headers = {"User-Agent": "Defined",
           "Accept-Language":"bg-BG,bg;q=0.9,en;q=0.8"}


response = requests.get(URL,headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text,"lxml")
price = soup.find(name="span",class_="a-offscreen")
price = price.get_text()
price = float(price.split("$")[1])
print(price)
product_name = soup.find(name="span",id="productTitle").get_text().strip()
print(product_name)
if MY_PRICE>price:
    my_email= "darimachine6@gmail.com"
    password = "xkgjzdspqoelzwmx"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="serhi1334@gmail.com",msg=f"Subject:Amazon Price Alert\n\n{product_name} is ${price} now \n {URL} ".encode("utf8"))
# print(soup)
