from lib2to3.pgen2 import token
from turtle import done
import requests
import os

class to_do_list():

    def __init__(self):
        self.trello_url = 'https://api.trello.com/1/'  
        self.auth =  {'key': os.getenv('APP_KEY'), 'token' : os.getenv('APP_TOKEN')}
        self.todo_list_id = '6200e316e238394a0c305e27'
        self.doing_list_id = '6200e316e238394a0c305e28'
        self.done_list_id = '6200e316e238394a0c305e29'
        self.trello_cards = 'cards/'

    def return_list(self):
        
        trello_list = 'lists/'
        payload = self.auth
        payload.update({'fields':['id','name']})
        self.to_do = requests.get(self.trello_url+trello_list+self.todo_list_id+'/'+self.trello_cards,payload)
        self.doing = requests.get(self.trello_url+trello_list+self.doing_list_id+'/'+self.trello_cards,payload)
        self.done = requests.get(self.trello_url+trello_list+self.done_list_id+'/'+self.trello_cards,payload)
        self.lists = [self.to_do, self.doing, self.done]
        return self.lists

    def add_card(self, title):
        payload = self.auth
        payload.update({'idList':self.todo_list_id,'name':title})
        requests.post(self.trello_url+self.trello_cards,payload)



    def return_card(self, id):
        payload = self.auth
        payload.update({'fields':['name','idList']})
        card = requests.get(self.trello_url+self.trello_cards+id,payload)
        return card.json()

    def update_card(self, id, name, status):
        if (status == 'Not Started'):
            list_id = self.todo_list_id
        if (status == 'Started'):
            list_id = self.doing_list_id
        if (status == 'Done'):
            list_id = self.done_list_id
        payload = self.auth
        payload.update({'name': name, 'idList': list_id})
        requests.put(self.trello_url+self.trello_cards+id,payload)

    def delete_item(self, id):
        payload = self.auth
        payload.update({'id':id})
        requests.delete(self.trello_url+self.trello_cards+id, params=payload)