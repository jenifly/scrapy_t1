import json
import codecs

import MySQLdb

class WYYFPipeline(object):
  
    # def __init__(self):
    #     self.file = codecs.open('musicInfo.json', 'w', encoding='utf-8')
    #     self.file.write('[')

    def process_item(self, item, spider):
        # self.file.write(json.dumps(dict(item), ensure_ascii=False) + ",\n")
        return item

    # def spider_closed(self, spider):
    #     self.file.close()
    # dbconfig = {
    #     host:"localhost",
    #     user：'root',
    #     passwd:'root',
    #     db:'jienfly_music',
    #     port:3306,
    #     charset:'utf-8'
    # }

    # def __init__(self):
    #     self.connect = MySQLdb.connect(**self.dbconfig)
    #     self.cursor = self.connect.cursor();

    # def process_item(self, item, spider):
    #     sql = "insert into user(name,created) values(%s,%s)"  
    #     param = ("aaa",int(time.time()))    
    #     n = cursor.execute(sql,param)    
    #     return item