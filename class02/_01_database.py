
# 连接MySQL执行操作
# 需要安装 pymysql  pip install pymysql

from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    token = request.args.get('token')
    if not token:
        return jsonify({'result': False, 'data': 'token校验失败'})

    result = get_user(token)

    if not result:
        return jsonify({'result': False, 'data': '认证失败'})

    name = result[1]
    return jsonify({'result': True, 'data': '认证成功,欢迎你:' + name})

def get_user(token):
    # 直连 MySQL
    conn = pymysql.connect(host='127.0.0.1', port=5200, user='glue', password='Glue01_glue', charset='utf8', db='demo')
    if not conn:
        return jsonify({'result': False, 'data': '数据库连接失败'})

    cursor = conn.cursor()
    cursor.execute('select * from t_user where token = %s', [token, ])
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    # result 是一个tuple 顺序是表的创建的顺序
    return result

if __name__ == '__main__':
    app.run()