import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('outpit.json', 'w')

response_dict = r.json()

json.dump(response_dict, outfile, indent=4)

list_of_repos = response_dict['items']

# Number of Repos

print(f'Number of Repos: {len(list_of_repos)}')

first_repo = list_of_repos[0]

#for key in first_repo:
#    print(key)

# print practice

# the name

print('Name of Repo:', first_repo['name'])

# the owner

print('Name of Owner:', first_repo['full_name'])

# number of stars

print('Number of StarGazers:', first_repo['stargazers_count'])

# url of repo

print('URL of Repo:', first_repo['owner']['html_url'])

# when it was created

print('Created:', first_repo['created_at'])

# when it was last updated

print('Last Updated:', first_repo['updated_at'])

# description

print('Description:', first_repo['description'])

#

repos, stars = []

for row in list_of_repos[:10]:
    repos.append(row['name'])
    stars.append(row['stargazers_count'])

from plotly.graph_objs import Bar
from plotly import offline

data = [
    {
    'type':'bar',
    'x': repos,
    'y': stars,
    'marker':{
        'color':'rgb(60,100,150)'
        'line':{'width':1.5, 'color':'rgb(25,25,25)'}
    }
    'opacity':0.6:

    }
]

my_layout = {
    'title':'Most Starred Python Repos on GitHub'
    'xaxis':{'title':'repository'}
    'yaxis':{'title':'stars'}
}

fig = {'data':data, 'layout': my_layout}

offline.plot(fig, filename='python_repos.html')