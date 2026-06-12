import pytest

class TestPostsApi:
    def test_get_all_posts_status_code(self, session, base_url):
        """GET /posts/ should return 200"""
        response = session.get(f"{base_url}/posts")
        assert response.status_code == 200

    def test_get_all_posts_return_list(self, session, base_url):
        """GET /posts/ should return a list of 100 posts"""
        response = session.get(f"{base_url}/posts")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 100

    def test_get_single_post(self, session, base_url):
        """GET /posts/1 should return a post with correct structure"""
        response = session.get(f"{base_url}/posts/1")
        assert response.status_code == 200
        post = response.json()
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert "userId" in post

    def test_get_single_post_correct_id(self, session, base_url):
        """The returned post id should match what we requested"""
        response = session.get(f"{base_url}/posts/5")
        post = response.json()
        assert post["id"] == 5

    def test_get_nonexistent_post_returns_404(self, session, base_url):
        """GET /posts/99999 should return 404"""
        response = session.get(f"{base_url}/posts/99999")
        assert response.status_code == 404

    def test_create_post(self, session, base_url):
        """POST /posts should return 201 and echo back the data"""
        payload = {"title": "Test Post", "body": "Test body", "userId": 1}
        response = session.post(f"{base_url}/posts", json=payload)
        assert response.status_code == 201
        created = response.json()
        assert created["title"] == payload["title"]
        assert created["body"] == payload["body"]
        assert "id" in created

    def test_update_post(self, session, base_url):
        """PUT /posts/1 should return 200 and echo back the updated data"""
        payload = {"title": "Updated title", "body": "Updated body", "userId": 1}
        response = session.put(f"{base_url}/posts/1", json=payload)
        assert response.status_code == 200
        updated = response.json()
        assert updated["title"] == payload["title"]
        assert updated["body"] == payload["body"]

    def test_delete_post(self, session, base_url):
        """DELETE /posts/1 should return 200"""
        response = session.delete(f"{base_url}/posts/1")
        assert response.status_code == 200

    @pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
    def test_multiple_posts_have_valid_schema(self, session, base_url, post_id):
        """Parametrized = runs this test 5 times with different IDs"""
        response = session.get(f"{base_url}/posts/{post_id}")
        assert response.status_code == 200
        post = response.json()
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)
        assert isinstance(post["userId"], int)