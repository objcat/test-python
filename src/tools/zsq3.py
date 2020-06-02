# description: zsqlite
# date: 2020/6/2 2:10 下午
# author: objcat
# version: 1.0

import sqlite3


class User:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None


class Zsq3:

    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)

    def close(self):
        self.db.close()

    def execute(self, sql):
        if sql == None:
            print("sql为空")
            return False
        self.db.execute(sql)
        self.db.commit()

    def insert(self, obj):
        sql = self.__make_insert_sql(obj, True)
        self.execute(sql)
        pass

    def __make_insert_sql(self, obj, checkNone):

        # 对象转字典
        dic = obj.__dict__
        print(dic)

        flag = 0

        for key in dic:
            if dic[key] != None:
                flag = 1
                break

        if flag == 0:
            return None

        # 获取表名
        table = obj.__class__.__name__.lower()

        # 构造header
        header = f"insert into {table} "

        # 构造body
        body = "("
        for key in dic:
            if checkNone:
                if dic[key] != None:
                    body = body + key + ","

        # 如果最后一个字符是逗号: 切掉
        if body[len(body) - 1:] == ',':
            body = body[:-1]

        body = body + ")" + " values ("

        for key in dic:
            if checkNone:
                if dic[key] != None:
                    body = body + "'" + dic[key] + "'" + ","

        # 如果最后一个字符是逗号: 切掉
        if body[len(body) - 1:] == ',':
            body = body[:-1]
        sql = header + body + ")"

        return sql


db = Zsq3("./test.db")


def start():
    sql = """
create table if not exists user (
	id integer not null
		constraint user_pk
			primary key autoincrement,
	name text default '',
	age text default ''
);
    """



    pass


if __name__ == '__main__':
    start()
