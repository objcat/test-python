# description: 按键位置记录
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

from plugin.afk_helper.size import size


class KeyMap:

    # 挑战首领
    challenge_boss = {
        "name": "挑战首领",
        "point": {
            "default": (size.width(356), size.height(1088)),
            "720x1280": (356, 1088),
            "1080x2340": (552, 2091),
        }
    }

    # 弹出上的挑战首领(有时候会出现)
    second_challenge_boss = {
        "name": "弹窗上的挑战首领",
        "point": {
            "default": (size.width(356), size.height(980)),
            "720x1280": (356, 980),
            "1080x2340": (539, 1673),
        }
    }

    # 战斗
    battle = {
        "name": "战斗",
        "en_name": "battle",
        "point": {
            "default": (size.width(356), size.height(1223)),
            "720x1280": (356, 1223),
            "1080x2340": (526, 2255),
        }}

    # 再次挑战
    retry = {
        "name": "再次挑战",
        "en_name": "retry",
        "img": "./img/retry.png",
        "point": {
            "default": (size.width(356), size.height(1140)),
            "720x1280": (356, 1140),
            "1080x2340": (526, 1926),
        },
        "distance": {
            "720x1280": "31.575305938720703",
            "1080x2340": "19.899747848510742"
        }
    }

    # 下一关
    next = {
        "name": "下一关", "en_name": "next", "img": "./img/next.png",
        "point": {
            "default": (size.width(356), size.height(1140)),
            "720x1280": (356, 1140),
            "1080x2340": (535, 1872),
        },
        "distance": {
            "720x1280": "48.0312385559082",
            "1080x2340": "36.0"
        }
    }

    # 空白区域
    white_place = {
        "name": "点击空白", "point": {
            "default": (539, 223)
        }
    }

    # 王座之塔
    king_challenge = {
        "name": "王座之塔挑战",
        "en_name": "king_challenge",
        "point": {
            "default": (size.width(356), size.height(1223)),
            "720x1280": (349, 890),
            "1080x2340": (533, 1990),
        }
    }

    # 王座之塔继续
    king_tower_continue = {
        "name": "王座之塔继续",
        "en_name": "king_tower_continue",
        "img": "./img/touch_screen_continue.png",
        "point": {
            "default": (size.width(356), size.height(1140)),
            "720x1280": (356, 1140),
            "1080x2340": (535, 1872),
        },
        "distance": {
            "720x1280": "31.575305938720703",
            "1080x2340": "20.784608840942383"
        },
        "cut_ratio": {

            "1080x2340": "0.7"
        }
    }
