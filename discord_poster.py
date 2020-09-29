import json
import requests


with open('webhook.json', mode='r') as json_file:
	webhook_url = json.load(json_file)['WEBHOOK_URL']

class DiscordPoster:
	def __init__(self, jobs):
		self.jobs = jobs

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

		result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})


	def post_all_jobs(self):
		for job in self.jobs:
			self.post_job(job)
