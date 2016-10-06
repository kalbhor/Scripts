import requests
from pync import Notifier

url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=5"
response = requests.get(url).json()

quote = response['thought']['quote']
author = response['thought']['thoughtAuthor']['name']

Notifier.notify(quote, title=author, open='https://en.wikipedia.org/wiki/'+author)


