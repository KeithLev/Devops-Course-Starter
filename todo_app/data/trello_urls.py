import os

class trello_urls:
    base_url = 'https://api.trello.com/1/'  
    auth =  {'key': os.getenv('APP_KEY'), 'token' : os.getenv('APP_TOKEN')}
    not_started_list_id = os.getenv('NOT_STARTED_LIST_ID')
    started_list_id = os.getenv('STARTED_LIST_ID')
    done_list_id = os.getenv('DONE_LIST_ID')
    cards = 'cards/'
    lists = 'lists/'