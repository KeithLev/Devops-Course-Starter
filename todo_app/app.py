from flask import Flask, render_template,request, redirect
from flask_login import LoginManager, login_required, login_user, current_user
from werkzeug.utils import redirect
from todo_app.data.to_do_list import to_do_list
from todo_app.data.mongoDB import MongoDB
from todo_app.flask_config import Config
from todo_app.data.item_view_model import ViewModel
import os
import requests
from todo_app.data.user import User
from todo_app.data.roleChecker import ReadWriteNeeded


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    mongoDB = MongoDB()
    to_do_list_local = to_do_list(mongoDB)

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        url = f'https://github.com/login/oauth/authorize?client_id={os.getenv("GIT_HUB_CLIENT_ID")}'
        return redirect(url)

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)

    @app.route('/login/callback')
    def login_callback():
        url = 'https://github.com/login/oauth/access_token'
        code = request.args['code']
        params = {'client_id':os.getenv('GIT_HUB_CLIENT_ID'), 'client_secret':os.getenv('GIT_HUB_SECRET'), 'code':code }
        header = {'Accept': 'application/json'}
        oauth_token = requests.post(url, params=params, headers=header).json()['access_token']
        
        api_url = 'https://api.github.com/user'
        api_header = {'Accept':'application/vnd.github+json', 'Authorization': f'Bearer {oauth_token}'}
        user_id = requests.get(api_url, headers=api_header).json()['id']
        user = User(user_id)
        login_user(user)

        return redirect('/')

    @app.route('/')
    @login_required
    def index():
        list = ViewModel(to_do_list_local.return_list())
        if os.getenv('LOGIN_DISABLED') == 'Ture':
            role = 'Read/Write'
        else: role = current_user.role
        return render_template('index.html', lists = list, role = role)

    @app.route('/add_item', methods=['POST'])
    @login_required
    @ReadWriteNeeded
    def add_item(): 
        to_do_list_local.add_card(request.form.get('title'))
        return redirect('/')

    @app.route('/to_do/<id>')
    @login_required
    @ReadWriteNeeded
    def view_item(id):
        to_do = to_do_list_local.return_card(id)
        return render_template('item.html', to_do = to_do)

    @app.route('/update_item/<id>', methods=['PUT','POST'])
    @login_required
    @ReadWriteNeeded
    def update_item(id):
        to_do_list_local.update_card(id,request.form.get('title'),request.form.get('status'))
        return redirect('/')

    @app.route('/delete_item/<id>', methods=['POST'])
    @login_required
    @ReadWriteNeeded
    def delete_item(id):
        to_do_list_local.delete_item(id)
        return redirect('/')

    return app








    
