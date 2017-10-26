import json, requests

# Test Posts endpoint
print('Posts:')
url = 'http://127.0.0.1:8080/api/posts/'

headers={'Authorization': 'Token a6277a8131b6963ccfebe43629c6c1bcba25c60e'}

resp = requests.get(url=url, params=None, headers=headers)
data = json.loads(resp.text)

for post in data:
	content = post['content']
	pub_date = post['pub_date']
	print(content)
	print('-On: ' + pub_date)


# Test Profiles endpoint
print('')
print('Profiles:')
url = 'http://127.0.0.1:8080/api/profiles/'

headers={'Authorization': 'Token a6277a8131b6963ccfebe43629c6c1bcba25c60e'}

resp = requests.get(url=url, params=None, headers=headers)
data = json.loads(resp.text)

for profile in data:
	name = profile['name']
	description = profile['description']
	print(name)
	print(description)