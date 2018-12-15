# -*- coding: utf-8 -*-
import scrapy
from myclsmovies.items import MyclsmoviesItem
# 使用 item


class CrawlcodeSpider(scrapy.Spider):
    name = 'crawlcode'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4?offset=0']
    # 开始爬取的起始 url
    url_domain = 'http://maoyan.com/board/4'
    # 用于后续 url 的拼接

    def parse(self, response):
        dd = response.xpath('//dd')
        # 找到目标结构标签，后续就不用在全部代码里提取数据了
        for each in dd:
            movieranking = each.xpath('./i/text()').get()
            moviename = each.xpath('./a/@title').get()
            movietime = each.xpath('.//p[@class="releasetime"]/text()').get().split('：')[-1]
            movieactor = each.xpath('.//p[@class="star"]/text()').get().strip()  # 需要去掉换行符
            movielink = each.xpath('./a/@href').get()  # 完整连接需要拼接
            moviescore = ''.join(each.xpath('.//p[@class="score"]//text()').getall())
            item = MyclsmoviesItem(movie_ranking=movieranking,
                                   movie_name=moviename,
                                   movie_time=movietime,
                                   movie_actor=movieactor,
                                   movie_link=movielink,
                                   movie_score=moviescore
                                   )
            # 将每条数据写入字典
            yield item
            # 生成器的使用
        print('保存了一页')  # 注释
        next_page = response.xpath('//ul[@class="list-pager"]/li[last()]/a/@href').get()
        # 找下一页链接
        # ?offset=10
        # print(next_page)
        # end = response.xpath('//ul[@class="list-pager"]/li[last()]/a/@class').get()
        # if end != 'page_10':
        #     next_page_url = self.url_domain + next_page
        #     yield scrapy.Request(next_page_url, callback=self.parse)
        # else:
        #     print('*****全部爬取完成*****')
        #     return
        next_page_url = self.url_domain + next_page
        yield scrapy.Request(next_page_url, callback=self.parse)
        # 传入下一页链接，并使用 parse 来解析
        end = response.xpath('//ul[@class="list-pager"]/li[last()]/a/@class').get()
        # 检查是否是最后一页
        if end == 'page_10':
            print('*****全部爬取完成*****')
            return
