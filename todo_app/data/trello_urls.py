import os

class TrelloUrls:

    def __init__(self):
        self.base_url = 'https://api.trello.com/1/'  
        self.auth =  {'key': os.getenv('APP_KEY'), 'token' : os.getenv('APP_TOKEN')}
        self.not_started_list_id = os.getenv('NOT_STARTED_LIST_ID')
        self.started_list_id = os.getenv('STARTED_LIST_ID')
        self.done_list_id = os.getenv('DONE_LIST_ID')
        self.cards = 'cards/'
        self.lists = 'lists/'
    