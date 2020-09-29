from datetime import datetime
from html2text import html2text


class Job:
    def __init__(self, job_title, job_link, job_published, job_summary):
        self._set_title(job_title)
        self._set_timestamp(job_published)
        self._set_description(job_summary)
        self.link = job_link

    def _set_title(self, title):
        postfix = " - Upwork"
        postfix_position = title.rfind(postfix)
        if postfix_position != -1:
            title = title[0:postfix_position]

        self.title = title

    def _set_timestamp(self, published_parsed):
        published = datetime(*published_parsed[:6]).isoformat()
        self.timestamp = published

    def _set_description(self, summary):
        summary = html2text(summary)
        self.description = summary

    @staticmethod
    def create_from_list(job_list):
        jobs = []
        for job in job_list:
            job = Job(job["title"], job["link"], job['published_parsed'], job['summary'])
            jobs.append(job)

        return jobs