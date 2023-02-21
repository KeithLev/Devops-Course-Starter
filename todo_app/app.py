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
from loggly.handlers import HTTPSHandler
from logging import Formatter


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    mongoDB = MongoDB()
    to_do_list_local = to_do_list(mongoDB)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
        app.logger.addHandler(handler)

    login_manager = LoginManager()


    @login_manager.unauthorized_handler
    def unauthenticated():
        url = f'https://github.com/login/oauth/authorize?client_id={os.getenv("GIT_HUB_CLIENT_ID")}'
        return redirect(url)

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        app.logger.debug("User is " + user.role)
        return user


    login_manager.init_app(app)

    @app.route('/login/callback')
    def login_callback():
        try:
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
        except:
            app.logger.error('Unable to log in')
        
        

    @app.route('/')
    @login_required
    def index():
        list = ViewModel(to_do_list_local.return_list())
        if os.getenv('LOGIN_DISABLED') == 'True':
            role = 'Read/Write'
        else: role = current_user.role
        return render_template('index.html', lists = list, role = role)

    @app.route('/add_item', methods=['POST'])
    @login_required
    @ReadWriteNeeded
    def add_item(): 
        title = request.form.get('title')
        to_do_list_local.add_card(title)
        app.logger.info(f"User {get_id()} added to do item {title}")
        return redirect('/')

    @app.route('/to_do/<id>')
    @login_required
    @ReadWriteNeeded
    def view_item(id):
        to_do = to_do_list_local.return_card(id)
        app.logger.info(f"User {get_id()} viewed to do item {to_do.name}")
        return render_template('item.html', to_do = to_do)

    @app.route('/update_item/<id>', methods=['PUT','POST'])
    @login_required
    @ReadWriteNeeded
    def update_item(id):

        to_do_list_local.update_card(id,request.form.get('title'),request.form.get('status'))
        app.logger.info(f"User {get_id()} updated to do item with id {id}")
        return redirect('/')

    @app.route('/delete_item/<id>', methods=['POST'])
    @login_required
    @ReadWriteNeeded
    def delete_item(id):
        to_do_list_local.delete_item(id)
        app.logger.info(f"User {get_id()} deleted item with id {id}")
        return redirect('/')

    return app

    def get_id():
        if os.getenv('LOGIN_DISABLED') == 'True':
            return "Anonymous"
        else:
            return current_user.id







    
