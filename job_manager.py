from datetime import datetime
from html2text import html2text
from job import Job

class JobManager:
    def __init__(self, rss, state):
        self.rss = rss
        self.state = state

    def new_jobs_available(self):
        last_link = self.state.get_value('last_link')

        if last_link is False:
            return True

        current_last_link = self.rss.feed['entries'][0]['link']
        if current_last_link == last_link:
            return False
        else:
            return True

    def get_new_jobs(self):
        if not self.new_jobs_available():
            print('No new jobs available, waiting')
            return []

        last_link = self.state.get_value('last_link')
        jobs = self.rss.feed['entries']

        #+------------------------------------------+
        #|      CASE I: if no last_link in states   |
        #+------------------------------------------+
        if not last_link:
            self.state.add_value('last_link', jobs[0].link)
            return Job.create_from_list(jobs)

        new_jobs = 0
        
        #+---------------------------------------------+
        #|CASE II: last_link not equal to current_last |
        #+---------------------------------------------+
        for job in jobs:
            if job['link'] != last_link:
                new_jobs += 1
            else:
                print('Find new jobs: {}'.format(new_jobs))
                self.state.add_value('last_link', jobs[0].link)
                jobs = jobs[:new_jobs]
                return Job.create_from_list(jobs)