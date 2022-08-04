import pytest
from dotenv import load_dotenv,find_dotenv
from todo_app import app
import requests

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
    if url == 'https://api.trello.com/1/boards/6/lists':
        fake_response_data = [{'id':'6','name':'To Do'},{'id':'6','name':'Doing'},{'id':'6','name':'Done'}]
    else:
        fake_response_data =[
            {'id':'1','name':'Card 1', 'dateLastActivity':'2022-02-07T11:34:48:260Z'}
        ]

    return StubResponse(fake_response_data)





