from datetime import datetime


class Card:
    def __init__(self,id, name, status, lastActivity = datetime.today()):
        self.id = id
        self._name = name
        self._status = status
        self._lastActivity = lastActivity
    
    def updateCard(self):
        today = datetime.today()
        self.lastActivity = today

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def  name(self, value):
        self._name = value
        self.updateCard()
        
    
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
        self.updateCard()
        


        