# coding: utf-8
from datetime import datetime

from flask_sockets import Sockets

from views.todos import todos_view

import score, rank
from views.analysis import analysis_view
from flask import Flask,request,render_template

import leancloud
leancloud.init("MNB3coPRoycu9RzhssaSiN8g-gzGzoHsz", "2dI4wII5rpfaGpc6P6hpSGml")
TestObject = leancloud.Object.extend('TestObject')

app = Flask(__name__)
sockets = Sockets(app)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')

app.register_blueprint(analysis_view, url_prefix='/analysis')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def time():
    return str(datetime.now())

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/me')
def Score():
    return score.cjcx()

'''
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        test_object = TestObject()
        test_object.set('username', username)
        test_object.set('psw', password)
        test_object.save()
        try:
            return score.cjcx(username, password)
        except:
            message = "登录失败"
            return render_template('login.html',message=message)
    return render_template('login.html')

@app.route("/jwxt",methods=['GET','POST'])
def jwxt():
    if request.method =='POST':
        username = request.form['username']
        try:
            return jiaowuchu.login(username)
        except:
            message = "登录失败"
            return render_template('jwxt.html',message=message)
    return render_template('jwxt.html')

@app.route('/rank')
def Rank():
    return rank.Rank()
'''

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

if __name__=='__main__':
    app.run(threaded=True)