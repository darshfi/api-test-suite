class TestUsersAPI:
    def test_get_all_users(self, session, base_url):
        response = session.get(f"{base_url}/users")
        assert response.status_code == 200
        assert len(response.json()) == 10

    def test_user_schema_complete(self, session, base_url):
        """Every user should have all required top-level fields"""
        response = session.get(f"{base_url}/users/1")
        user = response.json()
        required_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
        for field in required_fields:
            assert field in user, f"Missing field: {field}"

    def test_user_email_contains_at_symbol(self, session, base_url):
        """Basic format validation - all user emails should contain @"""
        response = session.get(f"{base_url}/users")
        users = response.json()
        for user in users:
            assert "@" in user["email"], f"Invalid email: {user['id']}: {user['email']}"

    def test_user_address_has_geo(self, session, base_url):
        """Nested field validation - address should contain geo coordinates"""
        response = session.get(f"{base_url}/users/1")
        user = response.json()
        assert "geo" in user["address"]
        assert "lat" in user["address"]["geo"]
        assert "lng" in user["address"]["geo"]
