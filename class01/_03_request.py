
# 调用api 这里指调用别的api
# 需要安装requests库  pip install requests

import requests

# 模拟调用其他的请求
def bilibili_api():

    # 调用三方提供的post接口
    res = requests.post(
        url="http://localhost:5000/sign",
        json={
            "order_id": "asdf123"
        })

    print(res.json())

if __name__ == '__main__':
    bilibili_api()