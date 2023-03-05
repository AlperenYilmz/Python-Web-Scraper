## My attempt for Coding Allstars Trial Test, Python Web Scraper And Translater

- **href_collector.py** grabs href links in html file of a given url, concatenates relative urls with absolute url, writes down all the links in a txt file line by line.

- **html_leech.py** reads the txt file mentioned above, writes down html content regarding subpages within the main url.

- **dir_reader_translate.py** translates the text based content inside files written by **html_leech.py**, however, it also translates critical keywords of html codes, which disrupts the page structure, although translated content can be seen via terminal output.

- **linkos.txt** contains the scraped urls from given url, at this case, https://www.classcentral.com/

- Scraped html files size up to 350 mb
- Also note, for both .py files, don't forget to modify **headers** variable as your machine's user agent information.
