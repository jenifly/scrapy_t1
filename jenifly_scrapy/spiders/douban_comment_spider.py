import re
import scrapy

from PIL import Image
from faker import Factory
from jenifly_scrapy.items import DoubanMovieCommentItem
import urllib.parse as urlparse

class ComentSpider(scrapy.Spider):
    name = 'douban_comment'
    allowed_domains = ['accounts.douban.com', 'douban.com']
    start_urls = [
        'https://www.douban.com/accounts/login'
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    formdata = {
        'form_email': '1439916120@qq.com',
        'form_password': '1439916120zyls',
        'login': '登录',
        'source': 'None'
    }

    def start_requests(self):
        return [scrapy.Request(url='https://www.douban.com/accounts/login', 
                               headers=self.headers, meta={'cookiejar': 1}, 
                               callback=self.parse_login)]

    def parse_login(self, response):
        if 'captcha_image' in str(response.body):
            print('Copy the link:')
            link = response.xpath('//img[@class="captcha_image"]/@src').extract()[0]
            print(link)
            captcha_solution = input('captcha-solution:')
            captcha_id = urlparse.parse_qs(urlparse.urlparse(link).query, True)['id']
            self.formdata['captcha-solution'] = captcha_solution
            self.formdata['captcha-id'] = captcha_id
        return [scrapy.FormRequest.from_response(response,
                                                 formdata=self.formdata,
                                                 headers=self.headers,
                                                 meta={'cookiejar': response.meta['cookiejar']},
                                                 callback=self.after_login
                                                 )]

    def after_login(self, response):
        account = response.xpath('//a[@class="bn-more"]/span/text()').extract_first()
        if account is None:
            print("登录失败")
            self.start_requests()
        else:
            print("登录成功,当前账户为 %s" %account)
            self.headers['Host'] = "movie.douban.com"
            yield scrapy.Request(url='https://movie.douban.com/chart',
                                    meta={'cookiejar': response.meta['cookiejar']},
                                    headers=self.headers,
                                    callback=self.parse_movice_urls)

    def parse_movice_urls(self, response):
        # for item in response.xpath('//tr[@class="item"]'):
        # url = 'https://movie.douban.com/subject/'+re.sub(r'\D', '', item.xpath('td[2]/div/a/@href').extract()[0])+'/comments'
        url = 'https://movie.douban.com/subject/27605698/comments'
        yield scrapy.Request(url=url,
                          meta={'cookiejar': response.meta['cookiejar']},
                          headers=self.headers,
                          callback=self.parse_comment)
        yield scrapy.Request(url=url,
                          meta={'cookiejar': response.meta['cookiejar']},
                          headers=self.headers,
                          callback=self.parse_next_page,
                          dont_filter = True)

    def parse_next_page(self, response):
        print(response.status)
        try:
            next_url = response.urljoin(response.xpath('//a[@class="next"]/@href').extract()[0])
            print ("下一页")
            print (next_url)
            yield scrapy.Request(url=next_url,
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse_comment,
                              dont_filter = True)
            yield scrapy.Request(url=next_url,
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse_next_page,
                              dont_filter = True)
        except:
            print ("Next page Error")
            return

    def parse_comment(self, response):
        print (response.status)
        try:
            content = response.xpath('//div[@id="content"]')
            comment = DoubanMovieCommentItem()
            comment['bookname'] = content.xpath('//h1/text()').extract()[0].strip()
            for item in content.xpath('//div[@class="comment-item"]'):
                comment['people'] = item.xpath('div[2]/h3/span[2]/a/text()').extract()[0]
                comment['useful_num'] = item.xpath('div[2]/h3/span[1]/span/text()').extract()[0].strip()
                comment['time'] = item.xpath('//span[@class="comment-time "]/@title').extract()[0]
                comment['comment'] = item.xpath('div[2]/p/span/text()').extract()[0]
                yield comment
        except:
            print ("Error")
            return