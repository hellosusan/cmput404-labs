import requests

# virtualenv step 4:
#print(requests.__version__)

# curl step 5:
response = requests.get('http://www.google.com/')
print("Status Code: ", response.status_code)
print("Body:")
print(response.text)