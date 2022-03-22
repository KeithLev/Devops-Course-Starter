import requests
from todo_app.data.Card import Card


class to_do_list():

    def __init__(self, trello_urls):
        self.trello_urls = trello_urls
        payload = self.trello_urls.auth
        payload.update({'fields':['id','name']})
        self.not_started = requests.get(self.trello_urls.base_url+self.trello_urls.lists+self.trello_urls.not_started_list_id+'/'+self.trello_urls.cards,payload).json()
        self.started = requests.get(url = self.trello_urls.base_url+self.trello_urls.lists+self.trello_urls.started_list_id+'/'+self.trello_urls.cards, params = payload).json()
        self.done = requests.get(url=self.trello_urls.base_url+self.trello_urls.lists+self.trello_urls.done_list_id+'/'+self.trello_urls.cards, params = payload).json()

        self.cards = {}
        for item in self.not_started:
            card = Card(item['id'],item['name'],'Not Started')
            self.cards.update({card.id:card})

        for item in self.started:
            card = Card(item['id'],item['name'],'Started')
            self.cards.update({card.id:card})
        
        for item in self.done:
            card = Card(item['id'], item['name'],'Done')
            self.cards.update({card.id:card})
        

    def return_list(self):
        return self.cards.values()

    def add_card(self, title):
        payload = self.trello_urls.auth.copy()
        payload.update({'idList':self.trello_urls.not_started_list_id,'name':title})
        item = requests.post(self.trello_urls.base_url+self.trello_urls.cards,payload).json()
        card = Card(item['id'],title,'Not Started')
        self.cards.update({card.id:card})

    def return_card(self, id):
        return self.cards[id]

    def update_card(self, id, name, status):
        card = self.cards[id]
        if card.name != name:
            card.name = name
        if card.status != status:
            card.status = status

    def delete_item(self, id):
        self.cards.pop(id)
        payload = self.trello_urls.auth.copy()
        payload.update({'id':id})
        requests.delete(self.trello_urls.base_url+self.trello_urls.cards+id, params=payload)