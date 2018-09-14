import random
import selenium.webdriver.support.ui as ui

from scrapy.http import HtmlResponse
from scrapy import signals
from selenium import webdriver

#采用中间件结合selenium
class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "music":
            driver = webdriver.Chrome('G:/Tools/selenium/chromedriver.exe') #指定使用的浏览器
            driver.get(request.url)
            driver.switch_to.frame('g_iframe') #移动到 iframe
            wait = ui.WebDriverWait(driver, 15)
            if wait.until(lambda driver: driver.find_element_by_id('toplist')):
                body = driver.page_source
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return