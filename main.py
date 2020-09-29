from rss import RSSManager
from states import StateManager
from job_manager import JobManager
from discord_poster import DiscordPoster
from time import sleep

states = StateManager('states')
upwork_feed = RSSManager()
upwork_jobs = JobManager(upwork_feed, states)
dp = DiscordPoster()

while(True):
	jobs = upwork_jobs.get_new_jobs()[::-1]
	dp.post_all_jobs(jobs)

	sleep(60)