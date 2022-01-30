import requests
import datetime

# List of defense related words
defenseWords = ['submarine', 'army', 'navy', 'air force', 'military', 'department of defense', 'weapon',
'helicopter']

# Time period to search
yesterday = datetime.date.today() - datetime.timedelta(1)
unix_time= yesterday.strftime("%s")

# Loop through each search term and see what's there
for x in defenseWords:
    r = requests.get(url=
    f'http://hn.algolia.com/api/v1/search_by_date?tags=story&query={x}&numericFilters=created_at_i>={unix_time}')
    data = r.json()
    for y in data['hits']:
        print(f"{y['title']} hit on: {x}")