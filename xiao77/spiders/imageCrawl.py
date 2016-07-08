# -*- coding: utf-8 -*-
import scrapy
import os
import uuid
from bs4 import BeautifulSoup
from scrapy.http import Request

from xiao77.Utils.util import downImageViaMutiThread
from xiao77.items import ImageItem


class ImagecrawlSpider(scrapy.Spider):
    name = "imageCrawl"
    # base_dir = '/Users/zangliguang/Downloads/se_picture/'
    base_dir = os.path.join(os.getcwd(), "se_picture")
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
        for i in range(len(all_a)):
            # catlog_url=self.allowed_domains[0] + all_a[i].get('href')
            # print(all_a[i].contents[0] + ":" +catlog_url)
            catlog_dir_name = all_a[i].contents[0].replace('/', '-')
            # if not os.path.exists(catlog_dir_name):
            #     os.mkdir(catlog_dir_name)
            yield Request(self.allowed_domains[0] + all_a[i].get('href'),
                          callback=lambda response, catlog=catlog_dir_name: self.parseCatLog(response, catlog),
                          dont_filter=True)

            if i == 12:
                break
        pass

    def parseCatLog(self, response, catlog):
        soup = BeautifulSoup(response.body, "lxml")
        all_a = soup.find_all('a', class_='subject_t f14')
        # 遍历所catlog
        # for a in all_a:
        #     print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))

        # for i in range(len(all_a)):
        for i in range(len(all_a)):
            # images_url=self.allowed_domains[0] + all_a[i].get('href')
            # print(all_a[i].contents[0] + ":" + images_url)
            yield Request(self.allowed_domains[0] + all_a[i].get('href'),
                          callback=lambda response, catlog_name=catlog, title=all_a[i].contents[0]: self.parseImage(
                              response, catlog_name, title),
                          dont_filter=True)

        pagesSpan = soup.find('div', class_='pages')
        pageAs = pagesSpan.findAll('a')
        currentPage = int(pagesSpan.find('b').contents[0])
        catlogname = catlog
        if currentPage == 1:
            href = pageAs[len(pageAs) - 1].get('href')
            lastPage = href.split('=')[2]
            for i in range(currentPage + 1, int(lastPage) + 1):
                yield Request(self.allowed_domains[0] + href.replace(lastPage, str(i)),
                              callback=lambda response, catlog=catlogname: self.parseCatLog(response, catlog),
                              dont_filter=True)

        pass

    def parseImage(self, response, catlog_name, title):
        soup = BeautifulSoup(response.body, "lxml")
        divs = soup.find('div', class_='f14 mb10')
        images = divs.find_all('img')
        image_date = (soup.find('div', class_='tipTop').find_all('span'))[1].get('title')
        image = ImageItem()
        image['image_id'] = str(uuid.uuid1())
        image['image_title'] = title
        image['image_type'] = catlog_name
        image['image_count'] = len(images)
        image['image_date'] = image_date
        split = images[0]['src'].split('/')
        filename = split[len(split) - 1]
        image['image_link_head'] = images[0]['src'].replace(filename, '')
        image['image_link_tail'] = filename
        for i in range(1, len(images)):
            split = images[i]['src'].split('/')
            filename = split[len(split) - 1]
            image['image_link_tail'] += ',' + filename
        # print(image)
        # 遍历所有img
        # self.downLoadImage(catlog_name, images, title)
        yield image


        pass

    def downLoadImage(self, catlog_name, images, title):
        i = 0
        image_list = []
        dir_name = os.path.join(self.base_dir, catlog_name,title)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for img in images:
            i += 1
            image_list.append(img.get('src'))
        downImageViaMutiThread(image_list, dir_name)
