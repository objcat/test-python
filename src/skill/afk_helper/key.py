# description: 按键位置记录
# date: 2020/5/24 21:34
# author: objcat
# version: 1.0

from skill.afk_helper.size import size

# 挑战首领
challenge_boss = {"name": "挑战首领", "point": {
    "default": (size.width(356), size.height(1088)),
    "720x1280": (356, 1088),
    "1080x2340": (552, 2091),
}}
# 弹出上的挑战首领(有时候会出现)
second_challenge_boss = {"name": "弹窗上的挑战首领", "point": {
    "default": (size.width(356), size.height(980)),
    "720x1280": (356, 980),
    "1080x2340": (539, 1673),
}}
# 战斗
battle = {"name": "战斗", "point": {
    "default": (size.width(356), size.height(1223)),
    "720x1280": (356, 1223),
    "1080x2340": (526, 2255),
}}
# 再次挑战
retry = {"name": "再次挑战", "point": {
    "default": (size.width(356), size.height(1140)),
    "720x1280": (356, 1140),
    "1080x2340": (526, 1926),
}}
# 空白区域
white_place = {"name": "点击空白", "point": {
    "default": (539, 223)
}}
