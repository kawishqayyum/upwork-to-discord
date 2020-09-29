from rss import RSSManager
from states import StateManager
from job_manager import JobManager
from discord_poster import DiscordPoster

states = StateManager('states')
upwork_feed = RSSManager()
upwork_jobs = JobManager(upwork_feed, states)
dp = DiscordPoster()

jobs = upwork_jobs.get_new_jobs()
dp.post_all_jobs(jobs)
