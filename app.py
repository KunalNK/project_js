import urllib.request, json

url = "https://gorest.co.in/public-api/users"
response = urllib.request.urlopen(url)
mydata = json.loads(response.read())
print(type(mydata['data']))
for person in mydata['data']:
    names=(person['name'])
    print(names)
    
   