import time
import json
import requests
import feedparser
from urllib.parse import urlencode
from html2text import html2text
from datetime import datetime, timedelta

RSS_FEED_URL = 'https://www.upwork.com/ab/feed/topics/rss?'

with open('creds.json', mode='r') as json_file:
	params = json.load(json_file)

with open('webhook.json', mode='r') as json_file:
	webhook_url = json.load(json_file)['WEBHOOK_URL']

try:
	with open('urls.txt', 'r') as f:
		urls = f.readlines()
		urls = [url.rstrip() for url in urls]

except FileNotFoundError as err:
	print('[-] urls.txt not found!')

	with open('urls.txt', 'w+') as f:
		print('[+] urls.txt created')

	urls = []


def url_is_new(url_str):
    if url_str in urls:
        return False
    else:
        return True


def webhook(webhook_url):
	data = {}
	data['username'] = 'Upwork'
	data['content'] = 'This is a test message'

	headers={"Content-Type": "application/json"}

	result = requests.post(webhook_url, data=json.dumps(data), headers=headers)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print('Message sent successfully')

def get_feed_data():
	rss = RSS_FEED_URL + urlencode(params)
	feeds = feedparser.parse(rss)

	
	last_feed = feeds['entries'][0]

	project_title = last_feed['title'].split(' - Upwork')[0]

	data = {}
	data['content'] = project_title
	data['embeds'] = []

	embed = {}
	embed['color'] = 7330372
	embed['title'] = project_title
	embed["url"] = last_feed['id']
	embed["description"] = html2text(last_feed['summary'])
	embed['timestamp'] = datetime(*last_feed['published_parsed'][:6]).isoformat()
	# embed['footer'] = {'text': 'This is a sample footer'}

	data['embeds'].append(embed)

	result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# if __name__=='__main__':
	
# 	while(True):
# 		webhook(WEBHOOK_URL)
# 		time.sleep(3)