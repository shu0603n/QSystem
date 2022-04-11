from flask import Flask,request
from flask import render_template
from pandas import isnull

import psycopg2
import database
# web: gunicorn apl_name : app --log-file -
#実行方法
#コマンドプロンプトで下記を実行。
"""
set FLASK_APP=app
set FLASK_ENV=development
flask run

$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
$flask run
"""
#停止方法
"""
コンソールで[Ctrl + C]

再度flask runで起動できる
"""
"""
#SQLsetuzoku

heroku pg:psql postgresql-silhouetted-72488 --app q-sys-tem
"""

# 方法1
app = Flask(__name__)
"""
$ flask run
"""
# 方法2
#if __name__ == "__main__":
#    app = Flask(__name__)
#    app.run(debug=True)
"""
$ python app.py
"""
@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():

    print('login処理開始')

    #DataBaseクラスをインスタンス化
    db = database.DataBase

    #DBの接続情報を取得
    con = db.connect()

    #画面から送られてきたパラメータを変数に代入
    user_id = request.form.get("user_id")
    password = request.form.get("password")

    #SQL文にバインド変数を代入する。
    sql =  "select * from user_pass WHERE user_id = '%s'  AND password = '%s'" % (user_id, password)

    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)

    #DB接続を終了
    con.close()

    if len(res) == 0:
        #不一致のメッセージをindex.htmlに返す
        message='パスワードが一致しませんでした'
        return render_template('index.html',user_id=user_id,message=message)
    else:
        #dashboard.htmlに遷移
        return render_template('dashboard.html',user_id=user_id)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/kokyaku")
def kokyaku():
    return render_template('kokyaku.html')

@app.route("/kokyakuList")
def kokyakuList():
    return render_template('kokyakuList.html')

@app.route("/yoyaku")
def yoyaku():
    return render_template('yoyaku.html')

@app.route("/uriage")
def uriage():
    return render_template('uriage.html')

@app.route("/seisan")
def seisan():
    return render_template('seisan.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/menu")
def menu():
    user_id='sss'
    return render_template('dashboard.html',user_id=user_id)

@app.route("/index")
def signin():
    return render_template('index.html')

@app.route("/test/<str>")
def test(str):
    return f'変数は→{ str }です'
