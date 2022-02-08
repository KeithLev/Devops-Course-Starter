from flask import Flask, render_template,request
from werkzeug.utils import redirect
from todo_app import to_do_lists
from todo_app.to_do_lists import to_do_list
from todo_app.data.session_items import get_items, add_item, get_item, save_item
from todo_app.flask_config import Config
app = Flask(__name__)
app.config.from_object(Config())


to_do_list = to_do_lists.to_do_list()

@app.route('/')
def index():   
    lists = to_do_list.return_list()

    return render_template('index.html', lists = to_do_list.return_list())

@app.route('/add_item', methods=['POST'])
def add_item():
    to_do_list.add_card(request.form.get('title'))
    return redirect('/')

@app.route('/to_do/<id>')
def view_item(id):
    to_do = to_do_list.return_card(id)
    return render_template('item.html', to_do = to_do)

@app.route('/update_item/<id>', methods=['PUT','POST'])
def update_item(id):
    to_do_list.update_card(id,request.form.get('title'),request.form.get('status'))
    return redirect('/')

    
