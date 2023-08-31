import requests
import json

ur = requests.get('https://api.thecatapi.com/v1/breeds/abys')


#x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):
print(ur)
print(ur.headers) #ur.status_code
print(ur.text)
def jprint(str_obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(str_obj, sort_keys=True, indent=4)
    print(text)
jprint(ur.json())