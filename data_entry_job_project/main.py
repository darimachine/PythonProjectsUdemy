from Google import FillForm
from webscraping import ZillowScrap
from pprint import pprint
data = ZillowScrap()
links = data.list_of_links()
adresses = data.list_of_adresses()
prices = data.list_of_prices()
google_fil = FillForm()
google_fil.fill_form(links,adresses,prices)
pprint(links)
print(adresses)
print(prices)