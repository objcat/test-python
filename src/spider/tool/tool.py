"""
 description: tool.py
 time: 2019/9/1 10:57
 author: objcat
 verson: 1.0
"""


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as txt:
        txt.write(content)
