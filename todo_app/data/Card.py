from datetime import datetime
from todo_app.data.trello_urls import TrelloUrls
import requests
class Card:
    def __init__(self,id, name, status):
        self.trello_urls = TrelloUrls()
        self.id = id
        self.name = name
        self.status = status
        
        
    
    @property
    def name(self):
        return self._name  
    
    @name.setter
    def  name(self, name):
        self._name = name
        payload = self.trello_urls.auth.copy()
        payload.update({'name':name})
        requests.post(self.trello_urls.base_url+self.trello_urls.cards+self.id,payload)
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
        if (status == 'Not Started'):
            list_id = self.trello_urls.not_started_list_id
        if (status == 'Started'):
            list_id = self.trello_urls.started_list_id
        if (status == 'Done'):
            list_id = self.trello_urls.done_list_id
        payload = self.trello_urls.auth.copy()
        payload.update({'idList':list_id})
        requests.put(self.trello_urls.base_url+self.trello_urls.cards+self.id,payload)
        


        