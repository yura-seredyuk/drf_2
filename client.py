from pprint import pprint
import json
import requests


#      GET
# response = requests.get('http://127.0.0.1:8000/address/7')
# pprint(response.json())

#      POST
# post_data = {'country':"Ukraine", 'city':"Rivne", 'zip_code': 33026,'street':"Soborna str. 16", 'apartament':400}

# response = requests.post(
#             'http://127.0.0.1:8000/address/',
#             data=post_data)
# print(response.json(), response.status_code)

#      PUT
update_data = {
    # "country": "Ukraine",
    # "city": "Rivne",
    # "zip_code": 33026,
    # "street": "Soborna str. 16",
    # "apartament": 218
}
response = requests.put('http://127.0.0.1:8000/address/5/', data=update_data)
print(response.status_code)

#      DELETE
# response = requests.delete('http://127.0.0.1:8000/address/6')
# print(response.status_code)







