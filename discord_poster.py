import json
import requests


class DiscordPoster:
	def __init__(self):
		self._set_webhook()

	def _set_webhook(self):
		with open('webhook.json', mode='r') as json_file:
			self.webhook = json.load(json_file)['WEBHOOK_URL']

	def post_job(self, job):
		data = {}

		data['content'] = f'**{job.title}**'
		data['embeds' ] = []

		embed = {}
		embed['color'      ] = 7330372
		embed['title'      ] = job.title
		embed['url'        ] = job.link
		embed['description'] = job.description
		embed['timestamp'  ] = job.timestamp

		data['embeds'].append(embed)

		result = requests.post(self.webhook, data=json.dumps(data), headers={"Content-Type": "application/json"})

	def post_all_jobs(self, jobs):
		for job in jobs:
			self.post_job(job)
