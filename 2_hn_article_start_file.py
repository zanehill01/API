import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')

json.dump(r.json(), outfile, indent=4)

url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile)

# 

submission_ids = r.json()

for row in submission_ids[:21]:

    url = (f'https://hacker-news.firebaseio.com/v0/item/{row}.json')

    r = requests.get(url)
    response_dict = r.json()

    print('Title:', response_dict['title'])
    print(f'Link: .com')
    try:
        print('Comments:', response_dict['descendants'])
    except:
        print('Comments: 0')