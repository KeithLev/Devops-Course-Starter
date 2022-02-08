import os

class trello_urls:
    base_url = 'https://api.trello.com/1/'  
    auth =  {'key': os.getenv('APP_KEY'), 'token' : os.getenv('APP_TOKEN')}
    not_started_list_id = '6200e316e238394a0c305e27'
    started_list_id = '6200e316e238394a0c305e28'
    done_list_id = '6200e316e238394a0c305e29'
    cards = 'cards/'
    lists = 'lists/'