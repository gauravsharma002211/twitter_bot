import requests

# endpoint = "https://www.google.com"
# endpoint = "http://localhost:8000/api"
endpoint = "https://twitter.com/kurthschneider"
# endpoint = "http://httpbin.org/anything"

response = requests.get(endpoint,json={"json":"this is json data clientside"})


print(response.text)
print(type(response.text))
print(response.status_code)