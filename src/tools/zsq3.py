# description: zsq3
# date: 2020/6/2 2:10 下午
# author: objcat
# version: 1.0

import sqlite3
import json


class User:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None

    def __str__(self) -> str:
        return json.dumps(self.__dict__)


class Zsq3:

    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()

    def insert(self, obj):
        """插入对象
        表明为对象的所属类名
        :param obj: 对象
        :return: 是否插入成功
        """
        sql = self.make_insert_sql(obj, False)
        try:
            self.con.execute(sql)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, classz, where):
        """删除
        :param classz: 类 (表名)
        :param where: 条件语句
        :return: 是否删除成功
        """
        table = classz.__name__.lower()
        sql = f"delete from {table} where " + where
        try:
            self.con.execute(sql)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, obj, where):
        """更新
        :param obj: 对象
        :param where: 条件
        :return: obj
        """
        table = obj.__class__.__name__.lower()
        sql = self.make_update_sql(obj, where, False)
        try:
            self.con.execute(sql)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False
        pass

    def select_all(self, classz):
        """查询全部
        根据类来查询所属表中的所有数据
        :param classz: 类 (表名)
        :return: list
        """
        table = classz.__name__.lower()
        sql = f"select * from {table}"
        arr = self.cur.execute(sql).fetchall()
        result = []
        for tup in arr:
            obj = self.tuple_to_obj(tup, classz)
            result.append(obj)
        return result

    def select(self, classz, where):
        """查询
        :param classz: 类 (表名)
        :param where: 条件
        :return: object
        """
        table = classz.__name__.lower()
        sql = f"select * from {table} where " + where
        tup = self.cur.execute(sql).fetchone()
        table = classz.__name__.lower()
        obj = self.tuple_to_obj(tup, classz)
        return obj
        pass

    def tuple_to_obj(self, tup, classz):
        """元组转化成对象
        :param tup: 元组
        :param classz: 类名
        :return: object
        """
        obj = classz()
        # 对象转字典
        dic = obj.__dict__
        i = 0
        for key in dic:
            dic[key] = tup[i]
            i += 1
        # 字典回输
        obj.__dict__ = dic
        return obj

    def make_insert_sql(self, obj, append_empty):
        """构造插入sql
        :param obj: 对象
        :param allow_empty: 是否拼接空值
        :return: sql
        """
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
            if not append_empty:
                if dic[key] is not None:
                    body = body + key + ","
            else:
                body = body + key + ","

        # 如果最后一个字符是逗号: 切掉
        if body[len(body) - 1:] == ',':
            body = body[:-1]

        body = body + ")" + " values ("

        for key in dic:
            if not append_empty:
                if dic[key] != None:
                    body = body + "'" + dic[key] + "'" + ","
            else:
                if dic[key] is None:
                    body = body + "''" + ","
                else:
                    body = body + "'" + dic[key] + "'" + ","

        # 如果最后一个字符是逗号: 切掉
        if body[len(body) - 1:] == ',':
            body = body[:-1]
        sql = header + body + ")"

        return sql

    def make_update_sql(self, obj, where, append_empty):
        """构建插入sql语句
        :param obj: 对象
        :param where: 条件
        :param append_empty: 是否拼接空值 None
        :return: sql
        """
        table = obj.__class__.__name__.lower()
        header = f"update {table} set "
        body = ""
        dic = obj.__dict__
        print(dic)
        for key in dic:
            if not append_empty:
                if dic[key] is not None:
                    body = body + key + "=" + "'" + dic[key] + "'" + ","
            else:
                if dic[key] is None:
                    body = body + key + "=" + "''" + ","
                else:
                    body = body + key + "=" + "'" + dic[key] + "'" + ","
        # 如果最后一个字符是逗号: 切掉
        if body[len(body) - 1:] == ',':
            body = body[:-1]
        sql = header + body + " where " + where
        print(sql)
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

    # user = db.select_by_key_value(User, key='id', value=10)
    # re = db.delete_by_key_value(User, key='id', value=10)
    # print(re)

    # 增
    # user = User()
    # user.name = "lisi"
    # user.age = '18'
    #
    # db.insert(user)

    # 删
    # db.delete(User, "id='11'")

    # 改
    # user = User()
    # user.age = '996'
    # db.update(user, "id='13'")

    # 查
    # print(db.select_all(User))
    # print(db.select(User, "id='13'"))

    pass


if __name__ == '__main__':
    start()
