# API Test Suite

An automated API testing suite built with **Python** and **pytest** to validate the REST endpoints of the [JSONPlaceholder](https://jsonplaceholder.typicode.com) mock API.

## Features
- **Structured Framework:** Uses pytest object-oriented test patterns (`TestPostsApi`).
- **Session Management:** Utilizes shared `requests.Session` fixtures for optimized HTTP connections.
- **Robust Assertions:** Validates HTTP status codes, data types, and accurate payload schemas.
- **Reporting:** Automatic generation of HTML test reports.

---

## Directory Structure
```text
api-test-suite/
│
├── tests/
│   ├── __init__.py
│   └── test_posts.py       # Test cases for the /posts endpoints
│
├── .gitignore
├── README.md
└── requirements.txt