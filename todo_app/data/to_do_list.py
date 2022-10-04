from datetime import datetime
from todo_app.data.Card import Card


class to_do_list():

    def __init__(self, mongoDB):
        self.mongoDB = mongoDB
        self.cards = {}
        items = self.mongoDB.return_cards()
        for item in items:
            card = Card(str(item['_id']), item['Name'], item['Status'], self.mongoDB, item['LastActivity'])
            self.cards.update({card.id:card})
        
    def return_list(self):
        return self.cards.values()

    def add_card(self, title):
        lastUpdated = datetime.today()
        result = self.mongoDB.add_card(title, "Not Started", lastUpdated)
        card = Card(result,title,'Not Started', self.mongoDB, lastUpdated)
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
        self.mongoDB.delete_card(id)