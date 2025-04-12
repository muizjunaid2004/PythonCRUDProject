import pytest

from rest_framework.test import APIClient

    
#Testing Creation and Lisitng
@pytest.mark.django_db
def test_CreateTask():
    
    client = APIClient()

    payload_1 = {
        'id': 1,
        'title' : 'Walk the Dog',
        'completed' : False
    }
    
    payload_2 = {
        'id': 2,
        'title' : 'Go somewhere',
        'completed' : False
    }
    
    payload_list = [payload_1, payload_2]
    
    
    api_call_1 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_1, format='json')
    api_call_2 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_2, format='json')

    
    assert api_call_1.status_code == 200
    assert api_call_2.status_code == 200
    
    api_call_3 = client.get("http://127.0.0.1:8000/api/task-list/")
    
    api_call_3.status_code = 200
    
    assert api_call_3.data == payload_list
    

#Testing deletion
@pytest.mark.django_db
def test_CreateTask():
    
    client = APIClient()

    payload_1 = {
        'id': 1,
        'title' : 'Walk the Dog',
        'completed' : False
    }
    
    payload_2 = {
        'id': 2,
        'title' : 'Go somewhere',
        'completed' : False
    }
    
    payload_list = [payload_1, payload_2]
    
    
    api_call_1 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_1, format='json')
    api_call_2 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_2, format='json')

    
    assert api_call_1.status_code == 200
    assert api_call_2.status_code == 200
    
    api_call_3 = client.get("http://127.0.0.1:8000/api/task-list/")
    
    api_call_3.status_code = 200
    
    assert api_call_3.data == payload_list
        
    api_call_4 = client.delete('http://127.0.0.1:8000/api/task-delete/2/')
    
    api_call_4.status_code = 200
    
    payload_list = [payload_1]

    api_call_5 = client.get("http://127.0.0.1:8000/api/task-list/")
    
    api_call_5.status_code = 200
    
    assert api_call_5.data == payload_list
    
    
#Testing TaskDetail
@pytest.mark.django_db
def test_CreateTask():
    
    client = APIClient()

    payload_1 = {
        'id': 1,
        'title' : 'Walk the Dog',
        'completed' : False
    }
    
    payload_2 = {
        'id': 2,
        'title' : 'Go somewhere',
        'completed' : False
    }
    
    payload_list = [payload_1, payload_2]
    
    
    api_call_1 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_1, format='json')
    api_call_2 = client.post('http://127.0.0.1:8000/api/task-create/',data=payload_2, format='json')

    
    assert api_call_1.status_code == 200
    assert api_call_2.status_code == 200
    
    api_call_3 = client.get("http://127.0.0.1:8000/api/task-list/")
    
    api_call_3.status_code = 200
    
    assert api_call_3.data == payload_list
    
    api_call_4 = client.get('http://127.0.0.1:8000/api/task-detail/1/')
    api_call_5 = client.get('http://127.0.0.1:8000/api/task-detail/2/')
    
    assert api_call_4.status_code == 200
    assert api_call_5.status_code == 200
    
    assert api_call_4.data == payload_1
    
    assert api_call_5.data == payload_2
    
    


    
    
        
    
    