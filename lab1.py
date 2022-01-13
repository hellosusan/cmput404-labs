import requests

# virtualenv step 4:
#print(requests.__version__)

# curl step 5:
# response = requests.get('http://www.google.com/')
# print("Status Code: ", response.status_code)
# print("Body:")
# print(response.text)

# curl step 10:
response = requests.get('https://raw.githubusercontent.com/hellosusan/cmput404-labs/main/lab1.py')
print(response.text)
