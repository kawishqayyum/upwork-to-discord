import requests
import json
import time

RSS_FEED_URL = 'https://www.upwork.com/ab/feed/topics/rss?'

with open('creds.json', mode='r') as json_file:
	params = json.load(json_file)

with open('webhook.json', mode='r') as json_file:
	WEBHOOK_URL = json.load(json_file)['WEBHOOK_URL']

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


if __name__=='__main__':
	
	while(True):
		webhook(WEBHOOK_URL)
		time.sleep(3)