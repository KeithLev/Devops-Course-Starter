from datetime import datetime
from todo_app.data.updateCard import UpdateCard
import requests
class Card:
    def __init__(self,id, name, status, TrelloUrls, lastActivity = datetime.today()):
        self.trello_urls = TrelloUrls
        self.id = id
        self._name = name
        self._status = status
        self._lastActivity = lastActivity
        self.updateCard = UpdateCard(TrelloUrls)
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def  name(self, value):
        self._name = value
        self.updateCard.updateName(self.id, self._name)
    
    @property
    def lastActivity(self):
        return self._lastActivity
    
    @lastActivity.setter
    def lastActivity(self, value):
        self._lastActivity = value
        
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value
        self.updateCard.updateStatus(self.id, self._status)
        


        