from datetime import datetime,timedelta
import pytest
from todo_app.data.Card import Card
from todo_app.data.item_view_model import ViewModel
from todo_app.data.trello_urls import TrelloUrls

@pytest.fixture
def setup():
    trelloUrls = TrelloUrls('1')
    item1 = Card("1","item1","Not Started",trelloUrls)
    item2 = Card("2","item2","Started",trelloUrls)
    item3 = Card("3","item3", "Done",trelloUrls)
    return [item1,item2,item3]

@pytest.fixture
def setup_recently_done(): 
    trelloUrls = TrelloUrls('')
    item4 = Card("4","item4", "Done", trelloUrls)
    item5 = Card("5","item5", "Done",trelloUrls)
    item6 = Card("6","item6", "Done",trelloUrls)
    item7 = Card("7","item7", "Done", trelloUrls, lastActivity=(datetime.today()- timedelta(days=1)))
    item8 = Card("8","item8", "Done", trelloUrls, lastActivity=(datetime.today()- timedelta(days=1)))
    return [item4, item5, item6, item7, item8]

        

def test_doing_items(setup):
    #arrange
    view_model = ViewModel(setup)
    #act 
    doing_items = view_model.doing_items
    #assert
    assert len(doing_items) == 1
    assert doing_items[0].status == "Started"

        
def test_to_do_items(setup):
    #arrange
    view_model = ViewModel(setup)
    #act
    to_do_items = view_model.to_do_items
    #assert
    assert len(to_do_items) == 1
    assert to_do_items[0].status == "Not Started"

def test_done_items(setup):
    #arrange
    view_model = ViewModel(setup)
    #act
    done_items = view_model.done_items
    #assert
    assert len(done_items) == 1
    assert done_items[0].status == "Done"

def test_recently_done_items(setup_recently_done):
     #arrange
    view_model = ViewModel(setup_recently_done)
    #act
    done_items = view_model.recently_done_items
    #assert
    assert len(done_items) == 3
    assert done_items[0].status == "Done"                                                                                                                                                                       
