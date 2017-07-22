# coding:utf-8
import random
import time
from faker import Faker

# 生成数
CREATE_COUNTS = 10000

# insert文
insertSQL = ""

# 期間内からランダムな時間(YYYY-mm-dd hh:ii:ss)を生成
def generateRandomDateTime(from_datetime, to_datetime):
    format = '%Y-%m-%d %H:%M:%S'
    from_time = time.mktime(time.strptime(from_datetime, format))
    to_time   = time.mktime(time.strptime(to_datetime,   format))
    return time.strftime(format, time.localtime(
        from_time + random.random() * (to_time - from_time)
    ))

# サンプルで生成したSQLをファイル保存
def saveSampleSQL(inserSQL):
	fp = open('sample_insert.sql', 'w')
	fp.write(insertSQL)
	fp.close()


# ランダムなSQLを生成
insertSQL = "INSERT INTO user (name, created_at) VALUES "

values = ''
for i in range(CREATE_COUNTS):
    name       = Faker('en_US').name()
    created_at = generateRandomDateTime('2017-07-01 00:00:00', '2017-07-31 00:00:00')

    values += "('{}', '{}'),".format(name, created_at)

insertSQL += values[:-1]

saveSampleSQL(insertSQL)
