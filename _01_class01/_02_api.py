
from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟一个用户请求 用户发送 order_id
# 我们返回签名的sign
@app.route("/sign", methods=["POST"])
def sign():
    """
    要求用户请求的参数格式 {"order_id":"..."}
    :return:
    """
    order_id = request.json.get("order_id")
    if not order_id:
        return jsonify({"result": False, "data":"参数错误"})

    # 执行算法计算签名 sign
    sign = 'abc' + order_id + '123'
    return jsonify({"result": True, "data": sign})

if __name__ == '__main__':
    app.run()                             # 默认的端口是 5000
