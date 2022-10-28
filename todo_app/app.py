from flask import Flask, render_template,request
from werkzeug.utils import redirect
from todo_app.data.to_do_list import to_do_list
from todo_app.data.mongoDB import MongoDB
from todo_app.flask_config import Config
from todo_app.data.item_view_model import ViewModel
import os



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    mongoDB = MongoDB()
    to_do_list_local = to_do_list(mongoDB)

    @app.route('/')
    def index():
        list = ViewModel(to_do_list_local.return_list())
        return render_template('index.html', lists = list)

    @app.route('/add_item', methods=['POST'])
    def add_item(): 
        to_do_list_local.add_card(request.form.get('title'))
        return redirect('/')

    @app.route('/to_do/<id>')
    def view_item(id):
        to_do = to_do_list_local.return_card(id)
        return render_template('item.html', to_do = to_do)

    @app.route('/update_item/<id>', methods=['PUT','POST'])
    def update_item(id):
        to_do_list_local.update_card(id,request.form.get('title'),request.form.get('status'))
        return redirect('/')

    @app.route('/delete_item/<id>', methods=['POST'])
    def delete_item(id):
        to_do_list_local.delete_item(id)
        return redirect('/')

    return app








    
