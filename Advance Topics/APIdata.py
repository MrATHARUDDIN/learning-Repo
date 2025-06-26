# API stands for Application Programming Interface.
# It allows two applications (or parts of code) to talk to each other.

import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# print(response) it will print response [200] Means working
print(response.json()) # now you can see the json data

print("")

#---------------------------------------  Post method ------------------------------- #

url2 = "https://jsonplaceholder.typicode.com/posts"

# Data to be sent
data = {
    "userID": 100,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

# A POST request to the API
Post_req = requests.post(url2, json=data)
# Print the response
print(Post_req.json())