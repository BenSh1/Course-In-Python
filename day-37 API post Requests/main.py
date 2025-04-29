import requests
from datetime import datetime
from datetime import timedelta

USERNAME = "ben124"
TOKEN = "mfdv56bkj45dfgdf6g"  # generate by yourself but the length of the token must be between 8-128 characters
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

# ====================================================
# Create your user account on the site
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# ====================================================
# Create a graph definition and Get the graph!
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ====================================================
# Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

"""
today = datetime(year=2024, month=11,day=30)
print(today)
print(today.strftime("%Y%m%d"))
"""

"""
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycle today?"),
}
"""

#response = requests.post(url= pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

# ====================================================
# update a pixel

today = datetime.now()
yesterday = today - timedelta(days=1)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

new_pixel_data = {
    "quantity": "4.5",
}

#response = requests.post(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

# ====================================================
# Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.post(url= delete_endpoint, headers=headers)
#print(response.text)
