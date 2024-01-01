import requests
import datetime as dt
USERNAME = "darimachine"
TOKEN = "hfoljhnfeqwphfqbflqjqads"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH = "graph2"
user_parameters={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#suzdavaNE USER
# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param = {
    "id":GRAPH,
    "name":"Programing Graph",
    "unit":"Hour and Min",
    "type":"float",
    "color":"ichou",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
today = dt.datetime.now()

#grafika suzdavane
# respone = requests.post(url=graph_endpoint,json=graph_param,headers=headers
#                         )
# print(respone.text)
#update
# response = requests.put(url=f"{graph_endpoint}/{GRAPH}",headers=headers,json=graph_param)
# print(response.text)
#dobavqne pixel i aktualizirane
graph_post_add_pixel = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"3",
}
pixel_creat_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# dobavqne
#response = requests.post(url=pixel_creat_endpoint, headers=headers, json=graph_post_add_pixel)
#update
#response = requests.put(url=f"{pixel_creat_endpoint}/{str(int(today.strftime('%Y%m%d'))-1)}", headers=headers, json={"quantity":"7"})
#delete
response = requests.delete(url=f"{pixel_creat_endpoint}/{today.strftime('%Y%m%d')}", headers=headers)

print(response.text)