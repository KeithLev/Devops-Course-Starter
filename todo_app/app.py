from flask import Flask, render_template,request
from werkzeug.utils import redirect
from todo_app.data.session_items import get_items, add_item, get_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()

    items = sorted(items, key=lambda items : items['status'], reverse=True)

    return render_template('index.html', to_dos = items)

@app.route('/add_item', methods=['POST'])
def submit():
    add_item(request.form.get('title'))
    return redirect('/')

@app.route('/to_do/<id>')
def view_item(id):
    item = get_item(id)
    not_started = False
    started = False
    done = False

    not_started = item['status'] == "Not Started"
    started = item['status'] == "Started"
    done = item['status'] == "Done" 
    return render_template('item.html', to_do = get_item(id), not_started  = not_started, started = started, done = done)

@app.route('/update_item/<id>', methods=['POST', 'GET'])
def submit_item(id):
    item = get_item(id)
    item['title'] = request.form.get('title')
    item['status'] = request.form.get('status')
    save_item(item)
    return redirect('/')

    
