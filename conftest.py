import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def session():
    """Shared requests session for all tests"""
    s = requests.Session()
    s.headers.update({"Context-Type": "application/json"})
    yield s
    s.close()

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL