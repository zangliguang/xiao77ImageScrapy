# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from scrapy.http import Request


class ImagecrawlSpider(scrapy.Spider):
    name = "imageCrawl"
    allowed_domains = ["http://x77525.com/bbs/"]
    start_urls = (
        'http://x77525.com/bbs/',
    )

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        all_a = soup.find_all('a', class_='mr10')
        # 遍历所catlog
        # for a in all_a:
        #     print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))
        yield Request(self.allowed_domains[0] + all_a[0].get('href'), callback=self.parseCatLog, dont_filter=True)
        # for i in range(len(all_a)):
        #     # catlog_url=self.allowed_domains[0] + all_a[i].get('href')
        #     # print(all_a[i].contents[0] + ":" +catlog_url)
        #     yield Request(self.allowed_domains[0] + all_a[i].get('href'), callback=self.parseCatLog, dont_filter=True)
        #
        #     if i == 12:
        #         break
        pass

    def parseCatLog(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        all_a = soup.find_all('a', class_='subject_t f14')
        # 遍历所catlog
        # for a in all_a:
        #     print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))

        for i in range(len(all_a)):
            # images_url=self.allowed_domains[0] + all_a[i].get('href')
            # print(all_a[i].contents[0] + ":" + images_url)
            yield Request(self.allowed_domains[0] + all_a[i].get('href'),
                          callback=lambda response, title=all_a[i].contents[0]: self.parseImage(response, title),
                          dont_filter=True)

        pagesSpan = soup.find('div', class_='pages')
        pageAs = pagesSpan.findAll('a')
        currentPage = int(pagesSpan.find('b').contents[0])
        if currentPage == 1:
            href = pageAs[len(pageAs) - 1].get('href')
            lastPage = href.split('=')[2]
            for i in range(currentPage+1, int(lastPage)+1):
                yield Request(href+str(i), callback=self.parseCatLog,dont_filter=True)

        pass

    def parseImage(self, response, title):
        soup = BeautifulSoup(response.body, "lxml")
        divs = soup.find('div', class_='f14 mb10')
        images = divs.find_all('img')
        # # 遍历所有img
        i = 0
        for img in images:
            i += 1
            print(title + ("第%d张" % (i) + ":" + img.get('src')))

        pass
