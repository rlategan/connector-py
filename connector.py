import json
from datetime import date, datetime
from urllib.request import urlopen

start_date = "2023-06-12"
todays_date = str(date.today())

url = "https://www.nytimes.com/games-assets/connections/game-data-by-day.json"
response = urlopen(url)
data = json.loads(response.read())

delta = datetime.strptime(todays_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")
id = data[delta.days]['id']
#print(delta.days)

groups_list = list(data[delta.days]['groups'])
items_list = list(data[delta.days]['groups'].values())

for i in range(0,4):
    print('level: ' + str(items_list[i]['level']))
    print(groups_list[i] + ":\n" + ', '.join(items_list[i]['members']) + "\n")

