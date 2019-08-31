# Class Central Spider
This is a Scrapy project to scrape courses from from https://classcentral.com.

## Extracted data
The extracted data looks like this sample:
      [
        {
            "subject_name": "Learn Computer Science", 
            "course_name": "Machine Learning", 
            "course_url": "https://www.classcentral.com/course/coursera-machine-learning-835"
        }
      ]


## Spiders

This project contains a spider and you can list them using the `list`
command:

    $ scrapy list
    subjects

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl subjects

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl subjects -o courses.json
