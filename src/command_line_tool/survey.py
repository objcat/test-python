from requests import request
import json
import sys


def start():
    arr = sys.argv
    if len(arr) < 2:
        print("参数错误!")
        return
    dataGroupCode = arr[1]
    data = {}
    if dataGroupCode == '3410065':
        data = {
            "dataGroupCode": "R1000007",
            "processId": "FC00I12",
            "runLevel": "1",
            "deptCode": "R6604",
            "operation": "2",
            "d01008": "3410065",
            "branchCode": "R",
            "userId": "01233",
            "gaUserId": "01233",
            "patternCode": "6",
            "loginBranchCode": "R",
            "d00322": "002",
            "itemId": "deleteBtn"
        }
    elif dataGroupCode == '3408458':
        data = {
            "dataGroupCode": "R1000007",
            "processId": "FC00I12",
            "runLevel": "1",
            "deptCode": "R6604",
            "operation": "2",
            "d01008": "3408458",
            "branchCode": "R",
            "userId": "01233",
            "gaUserId": "01233",
            "patternCode": "6",
            "loginBranchCode": "R",
            "d00322": "001",
            "itemId": "deleteBtn"
        }
    else:
        print("没有该id")
        return

    headers = {
        "Content-Type": "application/json"
    }

    req = request(url="http://192.168.9.170:8080/fcServerIpad/csf017105/u1", method="post", data=json.dumps(data),
                  headers=headers)
    print(req.content)


if __name__ == '__main__':
    start()
