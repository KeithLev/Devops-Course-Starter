import pytest
from dotenv import load_dotenv,find_dotenv
from todo_app import app
import requests
from todo_app.data.trello_urls import TrelloUrls
import os

@pytest.fixture
def client(monkeypatch):
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    monkeypatch.setattr(requests,'get',get_lists_stub)
    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(client):  
    response = client.get('/')
    assert response.status_code == 200
    assert 'Card 1' in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_lists_stub(url, params):
    NOT_STARTED_LIST_ID = os.environ.get('NOT_STARTED_LIST_ID')
    STARTED_LIST_ID = os.environ.get('STARTED_LIST_ID')
    DONE_LIST_ID = os.environ.get('DONE_LIST_ID')
    trello_urls = TrelloUrls()
    payload = trello_urls.auth.copy()
    payload.update({'fields':['id','name','dateLastActivity']})
    fake_response_data =[
        {'id':'1','name':'Card 1'}
    ]
    return StubResponse(fake_response_data)



