
import xmltodict



f = open("./DMSGestureRecognition.xml")
str = f.read()
dict = xmltodict.parse(str)
print(dict)