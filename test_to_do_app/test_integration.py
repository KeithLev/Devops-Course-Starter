from todo_app.data.mongoDB import MongoDB
import pymongo
import pytest
from dotenv import load_dotenv,find_dotenv
from todo_app import app
import mongomock
from todo_app.data.to_do_list import to_do_list


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        to_do_items = to_do_list(MongoDB())
        to_do_items.add_card('Card 1')
        test_app = app.create_app() 
        with test_app.test_client() as client:
            yield client


def test_index_page(client): 
    response = client.get('/')
    assert response.status_code == 200
    assert 'Card 1' in response.data.decode()
    





