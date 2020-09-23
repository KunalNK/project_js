import urllib.request, json
import csv

url = "https://gorest.co.in/public-api/users"
response = urllib.request.urlopen(url)
mydata = json.loads(response.read())
print(type(mydata['data']))

with open('myname.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Name','Emails', 'Gender'])
    for person in mydata['data']:
       names=person['name']
       emails=person['email']
       gender=person['gender']
       
       print(names)
       thewriter.writerow([names,emails,gender])
    
    
   