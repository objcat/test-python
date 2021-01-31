# description: cal
# date: 2021/1/8 11:06 上午
# author: objcat
# version: 1.0


import datetime
from tools import zdate

begin = "2020-12-21"
end = "2021-01-20"

money = 10000
annual_interest_rate = 0.045
day_interest_rate = annual_interest_rate / 365

begin_date = zdate.str_to_date(begin)
end_date = zdate.str_to_date(end)

print("建信养老飞月宝 29")
print(f"金额 {money} 元")
print(f"开始日期 {zdate.date_to_str_ymd(begin_date)}")
print(f"结束日期 {zdate.date_to_str_ymd(end_date)}")
print(f"等待期两天 {zdate.date_to_str_ymd(begin_date)} 和 {zdate.date_to_str_ymd(begin_date + datetime.timedelta(days=1))}")

# 涉及到钱的天数 加1是加上结束日期
total_day = (end_date - begin_date).days + 1

# 判断是否为周末
def is_workday(day):
    # Monday == 0 ... Sunday == 6
    if day.weekday() in [5, 6]:
        return False
    else:
        return True

# 所有日期打包
arr = []
for_begin_date = begin_date
for i in range(total_day):
    if i is 0:
        arr.append(for_begin_date)
    else:
        for_begin_date = zdate.nextday(for_begin_date)
        arr.append(for_begin_date)

print(f"金钱实际离手日 {len(arr)} 天")

# 排除等待日(两日)与结束日
arr.remove(begin_date)
arr.remove(begin_date + datetime.timedelta(days=1))
arr.remove(end_date)

# 排除周末(为了准确计算收益日)
arr2 = list(filter(is_workday, arr))

print(f"开始收益日期 {zdate.date_to_str_ymd(arr2[0])} 结束收益日(当天有收益) {zdate.date_to_str_ymd(zdate.lastday(end_date))} 续期日 {zdate.date_to_str_ymd(end_date)}")

# 周末没收益 但按照年化利率计算需要加上周末
print(f"收益日一共 {len(arr)} 天, 年化利率 {annual_interest_rate * 100}%, 日赚钱 {round(money * day_interest_rate, 1)} 元")
print(f"总收益约 {round(money * day_interest_rate * len(arr), 1)} 元")
