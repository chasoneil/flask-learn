

# 第一个flask demo

from flask import Flask, request, jsonify

app = Flask(__name__)

# 访问的URL
@app.route("/index")
def index():
    print('index executed...')
    return "success"

@app.route("/err")
def err():
    return "error"

# 通过URL拼接传递参数
# 需要导入request
# 使用url进行测试  http://localhost:5001/param?username=chason
# 这个方法只支持 get 请求
@app.route('/param')
def param():
    uname = request.args.get("username")        # 通过get(key)
    print("uname: %s" % uname)
    return "success"

# 处理post请求并携带参数
# post 的参数都在请求体中
# 测试需要使用postman这样的工具
@app.route('/post_param', methods=["POST"])
def param_p():
    uname = request.form.get("username")        # 用于获取 form-data 格式的
    print('uname:', uname)
    return "success"

# json 格式的数据的获取方式
@app.route("/json", methods=["POST"])
def get_json():
    print(request.json)
    print(type(request.json))       # 返回的是一个字典类型  dict
    return "success"

# 返回给用户 JSON 数据
# flask 提供了一个json 格式化的工具 jsonify
@app.route("/ret_json", methods=["POST"])
def ret_json():
    return jsonify({"result": True, "data":"操作成功"})

if __name__ == '__main__':
    # app.run()                             # 默认的端口是 5000
    app.run(host="127.0.0.1", port=5001)    # 可以自己指定