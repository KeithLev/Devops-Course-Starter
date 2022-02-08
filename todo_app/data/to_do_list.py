import requests
import os
from todo_app.data.Card import Card
from todo_app.data.trello_urls import trello_urls


class to_do_list():

    def __init__(self):
        payload = trello_urls.auth
        payload.update({'fields':['id','name']})
        self.not_started = requests.get(trello_urls.base_url+trello_urls.lists+trello_urls.not_started_list_id+'/'+trello_urls.cards,payload).json()
        self.started = requests.get(trello_urls.base_url+trello_urls.lists+trello_urls.started_list_id+'/'+trello_urls.cards,payload).json()
        self.done = requests.get(trello_urls.base_url+trello_urls.lists+trello_urls.done_list_id+'/'+trello_urls.cards,payload).json()

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
        return self.cards

    def add_card(self, title):
        payload = trello_urls.auth
        payload.update({'idList':trello_urls.not_started_list_id,'name':title})
        item = requests.post(trello_urls.base_url+trello_urls.cards,payload).json()
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
        payload = trello_urls.auth
        payload.update({'id':id})
        requests.delete(trello_urls.base_url+trello_urls.cards+id, params=payload)