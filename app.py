import urllib.request, json
import csv

url = "https://gorest.co.in/public-api/users"
response = urllib.request.urlopen(url)
mydata = json.loads(response.read())
print(type(mydata['data']))

with open('myname.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Name','Emails'])
    for person in mydata['data']:
       names=(person['name'])
       emails=(person['email'])
       print(names)
       thewriter.writerow([names,emails])
    
    
   