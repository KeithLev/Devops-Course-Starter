import requests

class GetListsFromBoard:
    def __init__(self, TrelloUrls, BoardID):
        self._TrelloUrls = TrelloUrls
        self._BoardID = BoardID
        self.payload = self._TrelloUrls.auth
        
    
    def GetToDoListId(self):
        boards = requests.get(url=self._TrelloUrls.base_url+'boards/'+ self._BoardID +'/lists',params=self.payload).json()
        for list in boards:
            if list['name'] == 'To Do':
                return list['id']

    def GetDoingListId(self):
        boards = requests.get(url=self._TrelloUrls.base_url+'boards/'+ self._BoardID +'/lists',params=self.payload).json()
        for list in boards:
            if list['name'] == 'Doing':
                return list['id']
        
    def GetDoneListId(self):
        boards = requests.get(url=self._TrelloUrls.base_url+'boards/'+ self._BoardID +'/lists',params=self.payload).json()
        for list in boards:
            if list['name'] == 'Done':
                return list['id']

        
