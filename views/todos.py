# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

import leancloud

leancloud.init("MNB3coPRoycu9RzhssaSiN8g-gzGzoHsz", "2dI4wII5rpfaGpc6P6hpSGml")

TestObject = leancloud.Object.extend('TestObject')
test_object = TestObject()

class Todo(Object):
    pass

todos_view = Blueprint('todos', __name__)


@todos_view.route('')
def show():
    try:
        todos = Query(TestObject).descending('createdAt').find()
    except LeanCloudError as e:
        if e.code == 101:  # 服务端对应的 Class 还没创建
            todos = []
        else:
            raise e
    return render_template('todos.html', todos=todos)


@todos_view.route('', methods=['POST'])
def add():
    content = request.form['content']
    test_object.set('words', content)
    try:
        test_object.save()
    except LeanCloudError as e:
        return e.error, 502
    return redirect(url_for('todos.show'))
