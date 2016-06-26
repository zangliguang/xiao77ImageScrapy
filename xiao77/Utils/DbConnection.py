import pymysql
import pymysql.cursors
import datetime

# try:
#     connection = pymysql.connect(host='localhost',
#                                  user='root',
#                                  db='db_liguang_se',
#                                  charset='utf8',
#                                  cursorclass=pymysql.cursors.DictCursor)
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "select * from image"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print('-----------------------------')
#         print('*****************************')
#         print(result)
# finally:
#     print("finally")
#     connection.close()


try:
    # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_liguang_se', port=3306, charset='utf8')
    insertsql = "INSERT INTO image_info (image_id, image_title,image_type,image_link_head,image_link_tail,image_date,image_count,image_create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur = conn.cursor()  # 获取一个游标
    # cur.execute('select * from image_info')
    # data = cur.fetchall()
    # for d in data:
    #     # 注意int类型需要使用str函数转义
    #     print(d)
    # cur.execute('select * from image_info')
    # print(cur.fetchall())
    cur.execute("SET NAMES utf8")
    sta = cur.execute(insertsql, (
        "1", 'image_title', 'image_type', 'image_link_head', 'image_link_tail', 'image_date', 0, datetime.datetime.now()
    ))
    result = cur.fetchall()
    print(sta)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
except  Exception:
    print("发生异常")
    print(Exception)
