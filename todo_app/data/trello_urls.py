import os
from todo_app.data.getListsFromBoard import GetListsFromBoard

class TrelloUrls:

    def __init__(self, boardID):
        self.cards = 'cards/'
        self.lists = 'lists/'
        self.auth = {'key': os.getenv('APP_KEY'), 'token' : os.getenv('APP_TOKEN')}
        self.base_url = 'https://api.trello.com/1/'
        self.getListsFromBoards = GetListsFromBoard(self, boardID)

    @property
    def not_started_list_id(self):
        return self.getListsFromBoards.GetToDoListId()
    
    @property
    def started_list_id(self):
        return self.getListsFromBoards.GetDoingListId()
    
    @property
    def done_list_id(self):
        return self.getListsFromBoards.GetDoneListId()


        

    
    

        
