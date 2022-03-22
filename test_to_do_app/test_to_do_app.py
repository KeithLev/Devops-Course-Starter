from itertools import count
import pytest
from todo_app.data.Card import Card
from todo_app.data.item_view_model import ViewModel

@pytest.fixture
def setup():
    item1 = Card("1","item1","Not Started")
    item2 = Card("2","item2","Started")
    item3 = Card("3","item3", "Done")
    return [item1,item2,item3]
        

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

