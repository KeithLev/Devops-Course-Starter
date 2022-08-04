import requests

class UpdateCard:
    
    def __init__(self, trello_url):
        self.trello_url = trello_url

    def updateName(self, id, name):
        payload = self.trello_url.auth.copy()
        payload.update({'name':name})
        requests.put(self.trello_url.base_url+self.trello_url.cards+id,payload)

    def updateStatus(self, id, status):
        if (status == 'Not Started'):
            list_id = self.trello_url.not_started_list_id
        if (status == 'Started'):
            list_id = self.trello_url.started_list_id
        if (status == 'Done'):
            list_id = self.trello_url.done_list_id
        payload = self.trello_url.auth.copy()
        payload.update({'idList':list_id})
        requests.put(self.trello_url.base_url+self.trello_url.cards+id,payload)