from job_manager import JobManager
from rss import RSSManager
from states import StateManager
from discord_poster import DiscordPoster

states = StateManager('states')
upwork_feed = RSSManager()
upwork_feed.parse_feed()
upwork_jobs = JobManager(upwork_feed, states)

jobs = upwork_jobs.get_new_jobs()

dp = DiscordPoster(jobs)

dp.post_all_jobs()
