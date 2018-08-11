import re
import scrapy
import json

from jenifly_scrapy.items import MusicItem

class MusicSpider(scrapy.Spider):
    name = 'musicj'
    # allowed_domains = ['music.163.com']
    # start_urls = ['https://music.163.com/#/discover/toplist']

    # def parse(self, response):
    #     lists = response.xpath('//tbody/tr')
    #     for row in lists:
    #         td = row.xpath("td")
    #         music = MusicItem()
    #         music['_id'] = re.sub('\D', '', td[1].xpath('div/div/div/span/a/@href').extract()[0])
    #         # music['rank']  = td[0].xpath("div/span[@class='num']/text()").extract()[0]
    #         # music['name']  = td[1].xpath("div/div/div/span/a/b/@title").extract()[0]
    #         # music['singer']  = td[3].xpath("div/@title").extract()[0]
    #         # music['duration']  = td[2].xpath("span/text()").extract()[0]
    #         yield music

    allowed_domains = ['music.163.com']
    with open('musicInfo.json', 'rb') as f:
        data = json.load(f)
    start_urls = ['https://music.163.com/#/song?id=1299557768']   #%s'%_id['_id'] for _id in data]

    def parse(self, response):
        print('------------------------------'+response.xpath['//div[@class="tit"]/em/text()']).extract()[0]
# https://music.163.com/api/song/lyric?id=574566207&lv=1
# http://music.163.com/song/media/outer/url?id=