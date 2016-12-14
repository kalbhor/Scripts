import requests
import pprint
from urllib.request import urlopen
from appscript import app, mactypes



time = 'week'
limit = '1'
params = {'t': time, 'limit': limit }

response = requests.get('https://www.reddit.com/r/wallpapers/top.json', params = params)
status = response.status_code
response = response.json()

try:
    url = response['data']['children'][0]['data']['url']
except KeyError:
	print(str(status) + ' :(')
	exit()

url = urlopen(url)
#app('Finder').desktop_picture.set(mactypes.File(url.read()))
#Find fix for MacOS Sierra
