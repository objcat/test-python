
import xlrd


def parse_excel():
    # 获取excel文档内容
    result = []
    wordbook = xlrd.open_workbook('./属性文档.xlsx')
    # 获取所有sheet
    total_sheet = wordbook.nsheets

    for i in range(total_sheet):
        # 获取sheet中的内容
        sheet_content = wordbook.sheet_by_index(i)
        # 装所有行
        rows = []
        # 创建字典
        sheet_dic = {"name": sheet_content.name, "rows": rows}
        # 获取所有行
        total_row = sheet_content.nrows
        # 遍历成我需要的数据
        for item in range(total_row):
            row = sheet_content.row_values(item)
            rows.append({"key": row[0], "value": row[1], "type": row[2]})
        result.append(sheet_dic)
    return result

def getModel(arr):
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
  @property (nonatomic, copy) NSString *{i['key'].lower()};
"""
        result += append
    print(result)



def getKeyList(arr):
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
        result += f'@"{i["key"].lower()}": @"{i["key"].lower()}",\n'

    foot = """
             };
}    
    """
    result += foot

    print(result)

def getDBSQL(arr):
    """
    获取创建表的sql文
    :return:
    """
    result = ""
    for i in arr:
        result += f"{i['key']} {i['type']} NOT NULL DEFAULT '', \n"
    print(result)


def get3(arr):
    for sheet_dic in arr:
        print(f"开始生成{sheet_dic['name']}")
        getModel(sheet_dic['rows'])
        getKeyList(sheet_dic['rows'])
        getDBSQL(sheet_dic['rows'])


if __name__ == '__main__':
    # 解析excel
    arr = parse_excel()
    get3(arr)









