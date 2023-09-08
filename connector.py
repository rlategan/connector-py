import json
from datetime import date, datetime
from urllib.request import urlopen

start_date = "2023-06-12"
todays_date = str(date.today())
delta = datetime.strptime(todays_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")

url = "https://www.nytimes.com/games-assets/connections/game-data-by-day.json"
response = urlopen(url)
data = json.loads(response.read())
id = data[delta.days]['id']

groups_list = list(data[delta.days]['groups'])
items_list = list(data[delta.days]['groups'].values())

difficulties = ['straightforward','intermediate','hard', 'tricky']

for i in range(0,4):
    print('difficulty: ' + str(difficulties[i]))
    print(groups_list[i] + ":\n" + ', '.join(items_list[i]['members']) + "\n")

