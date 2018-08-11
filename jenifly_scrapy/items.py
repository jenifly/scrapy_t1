import scrapy


class MusicItem(scrapy.Item):
    _id = scrapy.Field()
    # name = scrapy.Field()
    # rank = scrapy.Field()
    # singer = scrapy.Field()
    # duration = scrapy.Field()
    # album = scrapy.Field()
    # pic_url = scrapy.Field()
    # lrc_url = scrapy.Field()
    # song_url = scrapy.Field()

class DoubanMovieCommentItem(scrapy.Item):
    bookname = scrapy.Field()        # 书名
    useful_num = scrapy.Field()      # 多少人评论有用
    people = scrapy.Field()          # 评论者
    time = scrapy.Field()            # 评论时间
    comment = scrapy.Field()         # 评论