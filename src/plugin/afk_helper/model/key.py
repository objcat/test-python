# description: key_model
# date: 2020/5/30 11:22
# author: objcat
# version: 1.0


from plugin.afk_helper.key_map import KeyMap
from plugin.afk_helper import gl


class Key:

    def __init__(self, json=None):

        self.name = None
        self.en_name = None
        self.next = None
        self.img = None
        self.point = None
        self.distance = None
        self.cut_ratio = None

        if json is None:
            return

        self_dict = self.__dict__

        contain = ['point', 'distance', 'cut_ratio']

        for key in self_dict:
            try:
                self_dict[key] = json[key]
                # 如果有二层key, 使用分辨率来取
                if contain.__contains__(key):
                    try:
                        self_dict[key] = json[key][gl.adb.rp]
                    except:
                        self_dict[key] = None
                        pass
            except:
                pass


class KeyList:

    def __init__(self):
        self.challenge_boss = Key()
        self.second_challenge_boss = Key()
        self.battle = Key()
        self.retry = Key()
        self.next = Key()
        self.white_place = Key()
        self.king_challenge = Key()
        self.king_tower_continue = Key()
        self.xuan_pai = Key()
        self.zhua_pai = Key()

    @classmethod
    def init_with_key_map(cls):
        """通过key_map初始化
        在程序早期,使用key_map作为数据存储工具, 但这有个问题就是无法灵活的进行存取
        所以最新版的程序都是使用sqlite进行存储了
        :return: keylist
        """
        keylist = cls()
        keylist_dict = keylist.__dict__
        keymap_dict = KeyMap.__dict__
        for key in keylist_dict:
            keylist_dict[key] = Key(keymap_dict[key])
        # print("初始化key_list成功", keylist.__dict__)
        return keylist

    @classmethod
    def init_with_db(cls, db):
        """通过sqlite初始化
        :return:
        """
        keylist = cls()
        keylist_dict = keylist.__dict__
        arr = db.select_dic_list(Key, where=f"rp='{gl.adb.rp}'")
        if len(arr) <= 0:
            gl.zstr.log("初始化key_list失败, 没有设备对应的key, 请在数据库中添加")
            return
        for dic in arr:
            name = dic['en_name']
            try:
                obj = keylist_dict[name]
                try:
                    # 把字符串转化为元组
                    dic['point'] = eval(dic['point'])
                except:
                    pass
                obj.__dict__ = dic
            except Exception as e:
                continue
        gl.zstr.log("初始化key_list成功")
        return keylist


def start():
    pass


if __name__ == '__main__':
    start()
