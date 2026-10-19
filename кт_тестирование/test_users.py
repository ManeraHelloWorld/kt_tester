
import json
from pathlib import Path

import pytest
import requests

URL = "https://jsonplaceholder.typicode.com/users"

@pytest.fixture(scope="module")
def response():
    return requests.get(URL, timeout=15)

def test_status_code(response):
    assert response.status_code == 200

def test_users_count(response):
    users = response.json()
    assert len(users) == 10


def test_save_users(response):
    users = response.json()
    file_path = Path("users_data.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    assert file_path.exists()

    with open(file_path, "r", encoding="utf-8") as file:
        saved_users = json.load(file)

    assert saved_users == users


def test_first_user(response):
    users = response.json()
    first_user = users[0]

    assert first_user["id"] == 1
    assert first_user["name"].strip() != ""
