import json
import feedparser
from urllib.parse import urlencode
from os import environ

class RSSManager:
	def __init__(self):
		self._set_url()
		self.feed = None

	def _get_params(self):

		return {
			'securityToken':environ.get('securityToken'), 
			'userUid':environ.get('userUid'),
			'orgUid':environ.get('orgUid')
		}


	def _set_url(self):
		params = self._get_params()
		RSS_FEED_URL = 'https://www.upwork.com/ab/feed/topics/rss?'

		self.url = RSS_FEED_URL + urlencode(params)

	def parse_feed(self):
		try:
			feed = feedparser.parse(self.url)
			if feed['status'] == 200:
				self.feed = feed 

		except Exception as e:
			print(e)