# description: photo
# date: 2021/2/22 21:45
# author: objcat
# version: 1.0

import requests
import re
import json
import os



def start():
    url = "https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=1083968960&callback=shine1_Callback&t=688031792&mode=0&idcNum=4&hostUin=237249727&topicId=V10693Qt3xuQRL&noTopic=0&uin=237249727&pageStart=0&pageNum=50&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&callbackFun=shine1&_=1613999964110"
    header = {"cookie": "tvfe_boss_uuid=b980158a838f27c2; pgv_pvid=6216290733; RK=TEhxS0k/fk; ptcz=6b341b8fc762fa31ae848e52c4ccc8c96dcbd63bbc0017ee72eba85e7e1ea758; eas_sid=J126E103K675w9c7t1n7Q9i833; o_cookie=237249727; psrf_qqaccess_token=7C14DADC8AA60480F7E4348F827B5524; tmeLoginType=2; psrf_access_token_expiresAt=1621605979; psrf_qqrefresh_token=F1E4837770FDA8D7A08F9BBBFC40BF8A; euin=owolowvq7i-l; psrf_qqopenid=BA197462F3F7C43D1E78A94658166A01; psrf_qqunionid=; uid=69164401; pgv_info=ssid=s2106205134; uin=o0237249727; skey=@XO72RL8P7; p_uin=o0237249727; pt4_token=fkBbdRh*dn2ms7edSO-0aiU603FS9s3LpU*kqzUEAAE_; p_skey=K64dqb3Kb7zxnPUs6JTVng9BR3c4rW1368zTfm*4B8w_; Loading=Yes; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; qzmusicplayer=qzone_player_237249727_1613999957316"}
    res = requests.get(url, headers=header)
    partten = re.compile("shine1_Callback\((.*?)\);", re.S)
    j = re.findall(partten, res.text)[0]
    dic = json.loads(j)

    arr = dic["data"]["photoList"]
    print(len(arr))

    i = 0
    for item in arr:
        photo_url = item["url"]
        res = requests.get(photo_url)
        file_name = f"photo_{i}"
        path = f"./photos/{file_name}.png"
        if(os.path.exists(path)):
            i += 1
            continue
        f = open(path, "wb")
        f.write(res.content)
        f.close()
        i += 1
        print(f"保存第{i}张照片成功")





if __name__ == '__main__':
    start()