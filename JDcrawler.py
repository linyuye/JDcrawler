import requests
import json
import time
# 基础URL
base_url = "https://api.m.jd.com/"

# 查询参数
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    'Cookie':"改成自己的cookie"
}
page = 0
# 发送请求
while True:
    params = {
        "appid": "item-v3",
        "functionId": "pc_club_productPageComments",
        "client": "pc",
        "clientVersion": "1.0.0",
        "body": json.dumps({
            "productId": 10049758232411,#修改成你想爬取的商品id号
            "score": 0,
            "sortType": 5,
            "page": page,
            "pageSize": 10,
            "isShadowSku": 0,
            "fold": 1,
            "bbtf": "",
            "shield": ""
        }),
    }
    response = requests.get(base_url, params=params, headers=headers)
    # 检查响应
    if response.status_code == 200:
        data = response.json()
        comments = data.get('comments', [])

        if not comments:  # 如果没有更多评论，退出循环
            print("已经没有更多评论")
            break

        for comment in comments:
            print(comment['content'])

        page += 1  # 增加页数
        time.sleep(1)  # 添加延迟，避免请求过于频繁
    else:
        print(f"请求失败，状态码: {response.status_code}")
        break  # 如果请求失败，退出循环

    print(f"已经爬取第{page}页")
