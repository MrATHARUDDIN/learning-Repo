# API stands for Application Programming Interface.
# It allows two applications (or parts of code) to talk to each other.

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# print(response) it will print response [200] Means working
print(response.json()) # now you can see the json data



#---------------------------------------  Post method ------------------------------- #

url2 = "https://jsonplaceholder.typicode.com/posts"

# Data to be sent
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}