from flask import Flask, render_template,request
from flask.ctx import RequestContext
from flask.wrappers import Request
from werkzeug.utils import redirect
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', ToDos = get_items())

@app.route('/submit', methods=['POST','GET'])
def submit():
    add_item(request.form.get('title'))
    return redirect('/')

    
