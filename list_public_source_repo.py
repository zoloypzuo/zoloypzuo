import requests

link = ('https://api.github.com/users/zoloypzuo/repos')

api_link = requests.get(link)
api_data = api_link.json()

repos_Data = (api_data)

repos = []

[repos.append((items['name'], items['description'] or "")) for items in
 sorted(repos_Data, key=lambda item: -item['stargazers_count'])
 if items['private'] == False and items['fork'] == False]

print("name | description")
print("---|---")
for name, desc in repos:
    print(name, "|", desc)
