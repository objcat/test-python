# description: key_model
# date: 2020/5/30 11:22
# author: objcat
# version: 1.0


from plugin.afk_helper.key_map import KeyMap
from plugin.afk_helper.adb import adb
import json


class Key:

    def __init__(self, json=None):

        if json is None:
            return

        self.name = None
        self.en_name = None
        self.next = None
        self.img = None
        self.point = None
        self.distance = None
        self.cut_ratio = None

        self_dict = self.__dict__

        contain = ['point', 'distance', 'cut_ratio']

        pass

        for key in self_dict:
            try:
                self_dict[key] = json[key]
                # 如果有二层key, 使用分辨率来取
                if contain.__contains__(key):
                    try:
                        self_dict[key] = json[key][adb.ratio_key]
                    except:
                        self_dict[key] = None
                        pass
            except:
                pass


class KeyList:

    def __init__(self, KeyMap):
        self.challenge_boss = Key()
        self.second_challenge_boss = Key()
        self.battle = Key()
        self.retry = Key()
        self.next = Key()
        self.white_place = Key()
        self.king_challenge = Key()
        self.king_tower_continue = Key()

        keymap_dict = KeyMap.__dict__
        self_dict = self.__dict__
        for key in self_dict:
            self_dict[key] = Key(keymap_dict[key])
        pass

        print("初始化key_list成功", self.__dict__)


key_list = KeyList(KeyMap)
