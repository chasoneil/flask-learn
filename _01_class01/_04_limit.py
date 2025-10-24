

from flask import Flask, request, jsonify

app = Flask(__name__)

# 用户访问的时候，如果用户的token合法，则让用户访问
# 否则，拒绝用户的访问
# 我们编辑一个token.txt 文件，使用 uuid 生成每个用户的uuid 用户访问的时候携带uuid

@app.route("/login", methods=["POST"])
def login():
    """
    用户访问的时候 url?token=xxxx
    如果token合法，则让用户访问，否则拒绝
    :return:
    """
    token = request.args.get("token")
    if not token:
        return jsonify({"result": False, "data":"认证失败"})

    # 校验token合法性
    user_dict = get_user_dict()
    if token not in user_dict:
        return jsonify({"result": False, "data": "认证失败"})

    return jsonify({"result": True, "data":"认证成功，欢迎你," + user_dict.get(token)})


def get_user_dict():
    user_dict = {}
    with open("token.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            token, name = line.split(",")
            user_dict[token] = name
    return user_dict

if __name__ == '__main__':
    app.run()