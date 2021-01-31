# description: ke
# date: 2021/1/18 3:16 下午
# author: objcat
# version: 1.0


import matplotlib.pylab as plt
from tools import zdate

# 饼状图
def pie():
    labels = 'frogs', 'hogs', 'dogs', 'logs'
    sizes = 15, 20, 45, 10
    colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
    explode = 0, 0.1, 0, 0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()

# 折线图
def broken_line():
    begin = "2021-01-01"
    end = "2021-01-15"

    begin_date = zdate.str_to_date(begin)
    end_date = zdate.str_to_date(end)

    total_day = (end_date - begin_date).days + 1

    arr = []
    for_begin_date = begin_date
    for i in range(total_day):
        if i is 0:
            arr.append(for_begin_date)
        else:
            for_begin_date = zdate.nextday(for_begin_date)
            arr.append(for_begin_date)

    arr2 = []
    for date in arr:
        arr2.append(zdate.date_to_str_d(date))


    arr3 = [0, 0, 0, -1, -1, 1, 1, 0, 0, 0, 0, 3, -1, 0, 2]
    # for i in range(total_day):
    #     arr3.append(i)


    x_data = arr2
    y_data = arr3
    plt.plot(x_data, y_data)
    plt.show()


if __name__ == '__main__':
    broken_line()


