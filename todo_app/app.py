from flask import Flask, render_template,request
from flask.ctx import RequestContext
from flask.wrappers import Request
from werkzeug.utils import redirect
from todo_app.data.session_items import get_items, add_item, get_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()

    items = sorted(items, key=lambda items : items['status'], reverse=True)

    return render_template('index.html', ToDos = items)

@app.route('/submit', methods=['POST','GET'])
def submit():
    add_item(request.form.get('title'))
    return redirect('/')

@app.route('/todo/<id>')
def view_item(id):
    item = get_item(id)
    not_started = False
    started = False
    done = False

    if item['status'] == "Not Started":
        not_started = True
    if item['status'] == "Started":
        started = True
    if item['status'] == "Done":
        done = True     
    return render_template('item.html', ToDo = get_item(id), not_started  = not_started, started = started, done = done)

@app.route('/submit_item/<id>', methods=['POST', 'GET'])
def submit_item(id):
    item = get_item(id)
    item['title'] = request.form.get('title')
    item['status'] = request.form.get('status')
    save_item(item)
    return redirect('/')

    
