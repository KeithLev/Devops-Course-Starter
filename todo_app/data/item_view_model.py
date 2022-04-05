from datetime import datetime
from operator import truediv


class ViewModel:
    def __init__(self, items):
        self._items=items

    @property
    def items(self):
        return self._items

    @property
    def doing_items(self):
        doing_items = []
        for item in self.items:
            if item.status == "Started":
                doing_items.append(item)
        return doing_items

    @property
    def to_do_items(self):
        to_do_items = []
        for item in self.items:
            if item.status == "Not Started":
                to_do_items.append(item)
        return to_do_items

    @property
    def done_items(self):
        done_items = []
        for item in self.items:
            if item.status == "Done":
                done_items.append(item)
        return done_items

    @property
    def recently_done_items(self):
        recently_done_items = []
        today = datetime.today()
        for item in self.items:
            if item.status == "Done" and item.lastActivity.date() == today.date() :
                recently_done_items.append(item)
        return recently_done_items
    
    def five_or_more_done_items(self):
        if len(self.done_items) >=5:
            return True
        return False
