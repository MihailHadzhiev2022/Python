import pytest

@pytest.fixture
def sample_data():
    return {'name': 'mihail', 'age': 30}

def test_name(sample_data):
    assert sample_data['name'] == 'mihail'

def test_age(sample_data):
    assert sample_data['age'] == 30