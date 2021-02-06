# description: read_excel
# date: 2021/2/6 16:30
# author: objcat
# version: 1.0

# pip install xlrd==1.2.0
import xlrd

wordbook = xlrd.open_workbook('./1.xlsx')

# 获取sheet名字
# sheetnames= wordbook.sheet_names()
# targetname = sheetnames[1]
# print(targetname)

# 获取sheet内容
sheet_content = wordbook.sheet_by_index(1)

rows = sheet_content.row_values(3)
cols = sheet_content.col_values(1)
print(cols)


