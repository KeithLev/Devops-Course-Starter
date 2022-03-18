from todo_app.data.trello_urls import trello_urls
import requests
class Card:
    def __init__(self,id, name, status):
        self.id = id
        self._name = name
        self._status = status
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def  name(self, name):
        self._name = name
        payload = trello_urls.auth.copy()
        payload.update({'name':name})
        requests.post(trello_urls.base_url+trello_urls.cards+self.id,payload)
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
        if (status == 'Not Started'):
            list_id = trello_urls.not_started_list_id
        if (status == 'Started'):
            list_id = trello_urls.started_list_id
        if (status == 'Done'):
            list_id = trello_urls.done_list_id
        payload = trello_urls.auth.copy()
        payload.update({'idList':list_id})
        requests.put(trello_urls.base_url+trello_urls.cards+self.id,payload)
        


        