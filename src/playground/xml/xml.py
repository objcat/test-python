# description: xml
# date: 2021/1/26 23:55
# author: objcat
# version: 1.0

import xmltodict


f = open("./test.xml")
str = f.read()
f.close()
print(str)
# str = "<sence>1</sence>"
xml = xmltodict.parse(str)
print(dict)