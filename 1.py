import requests

#request = requests.get('http://api.open-notify.org')
#print(request.text)
#print(request.status_code)
#request2 = requests.get('http://api.open-notify.org/fake-endpoint')
#print(request2.status_code)
#people = requests.get('http://api.open-notify.org/astros.json')
#print(people.text)
#people_json  = people.json()
#print(people_json)
#To print the number of people in space
#print("Number of people in space:",people_json['number'])
#To print the names of people in space using a for loop
#for p in people_json['people']:
#   print(p['name'])

parameter = {"rel_rhy":"jingle"}
print(type(parameter))
request = requests.get('https://api.datamuse.com/words',parameter)
rhyme_json = request.json()
print(type(rhyme_json))
for i in rhyme_json[0:3]:
 print(i['word'],end=" ")