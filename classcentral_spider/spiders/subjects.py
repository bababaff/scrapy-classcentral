# -*- coding: utf-8 -*-
import scrapy


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://classcentral.com/subjects']

    # scrapy crawl subjects -a subject="subject that you wanna scrape"
    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            # log to the terminal
            self.logger.info(f"---> Scraping {self.subject} subject. <---")

            subject_url = response.xpath(
                f"//a[contains(@title, '{self.subject}')]/@href").get()  # '/subject/cs'

            yield scrapy.Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            # log to the terminal
            self.logger.info("---> Scraping all subjects. <---")

            subjects = response.xpath(
                "//*[@class='unit-block padding-right-small']/a/@href").getall()

            for subject in subjects:
                yield scrapy.Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        # 'Learn Mathematics | Free Online Courses | Class Central'
        # 'Learn Mathematics'
        subject_name = response.xpath("//title/text()").get()
        subject_name = subject_name.split("|")[0].strip()

        courses = response.xpath(
            "//*[@itemtype='http://schema.org/Event']")

        for course in courses:

            course_name = course.xpath(
                ".//*[@class='text--charcoal text-2 medium-up-text-1 block course-name']/@title").get()

            course_url = course.xpath(
                ".//*[@class='text--charcoal text-2 medium-up-text-1 block course-name']/@href").get()
            abs_course_url = response.urljoin(course_url)

            yield {
                'subject_name': subject_name,
                'course_name': course_name,
                'course_url': abs_course_url
            }
        next_page_url = response.xpath(
            "//*[@rel='next']/@href").get()  # '/subject/maths?page=2'
        # https://www.classcentral.com/subject/maths?page=2
        abs_next_page_url = response.urljoin(next_page_url)

        if next_page_url:
            yield scrapy.Request(abs_next_page_url, callback=self.parse_subject)
