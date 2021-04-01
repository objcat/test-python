


f = open(r"./1.txt", encoding='utf-8')

s = f.readlines()

f.close()

arr = []

def haveKey(key, arr):
    for i in arr:
        if i['key'] == key:
            return True
    return False

for i in s:
    i = i.split("\t", 1)
    dic = {"key": i[0], "value": i[1].replace("\n", "")}
    if not haveKey(i[0], arr):
        arr.append(dic)

print(arr)




def getModel():
    """
    生成model
    :return:
    """
    result = ""
    for i in arr:
        append = f"""
    /**
    *  {i['value']}
    */
    @property (nonatomic, copy) NSString *{i['key']};
        """
        result += append

    print(result)

def getKeyList():
    """
    生成JSONKeyPathsByPropertyKey
    :return:
    """
    result = ""
    head = """
+ (NSDictionary *)JSONKeyPathsByPropertyKey {

    return @{
    """
    result += head
    for i in arr:
        result += f'@"{i["key"]}": @"{i["key"]}",\n'

    foot = """
             };
}    
    """
    result += foot

    print(result)

def getDBSQL():
    """
    获取创建表的sql文
    :return:
    """
    result = ""
    result += "CREATE TABLE IF NOT EXISTS ZYTable (\n"
    for i in arr:
        result += f"{i['key']} text NOT NULL DEFAULT '', \n"
    result += "PRIMARY KEY (D01008, D00322, D36881)\n"
    result += ");"
    print(result)





if __name__ == '__main__':
    getModel()
    getKeyList()
    getDBSQL()









