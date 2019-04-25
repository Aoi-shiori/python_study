# coding =utf-8
import pymysql




class MySql:
    def __init__(self):
        self.DBconfig = {
                'host': '192.168.0.11',
                'port': 3306,
                'user': 'root',
                'password': 'conlin360',
                'db': 'test',
                # 'charset': 'utf8mb4', #字符集设置
                # 'cursorclass': pymysql.cursors.DictCursor,
         }

    def conn_db(self):#连接数据库
        conn = pymysql.connect(**self.DBconfig)
        cursor = conn.cursor()
        return conn, cursor

    def db_query(self,cursor, sql):  # 数据库查询
        cursor.execute(sql)
        return cursor

    def db_update(self,cursor,sql):#数据库更新
        sta=cursor.execute(sql)
        return sta

    def db_delete(self, cursor, Deid):
            for id in Deid.split(' '):
                sta = cursor.execute("delete from help_topic where help_topic_id =%d" % int(id))
            return sta



    def main_run(self):
        Deid = '541 542'
        sql ="select *from help_topic"
        #1.创建链接
        conn, cursor =self.conn_db()
        #2.调用数据库操作函数返回结果
        # self.db_query(cursor, sql)
        # row_1 = cursor.fetchone()   #获取第一行的数据
        #row_1 =cursor.fetchmany()    #获取前n行数据
        #row_1 = cursor.fetchall()   #获取所有数据
        # print("打印出查询结果", row_1)
        # sta=self.db_update(cursor,  """insert into help_topic(help_topic_id,name,help_category_id,description,example,url)
        #                                         VALUES('550','37','44','55','66','77')""")
        # if sta == 1:
        #     print("插入成功")
        # else:
        #     print("插入失败")
        self.db_delete(cursor, Deid)
        # 3.提交事务
        conn.commit()
        # 4.关闭连接
        #conndb.conn_close(conn, cursor)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # MySql.main_run()
    T=MySql()
    T.main_run()
