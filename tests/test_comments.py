class TestCommentsAPI:
    def test_filter_comments_by_post(self, session, base_url):
        """GET /comments?postId=1 should return only comments on post 1"""
        response = session.get(f"{base_url}/comments", params={"postId": 1})
        assert response.status_code == 200
        comments = response.json()
        assert len(comments) > 0
        for comment in comments:
            assert comment["postId"] == 1, f"Comment {comment['id']} has wrong post id"

    def test_comment_email_format(self, session, base_url):
        """All comment emails should be valid format"""
        response = session.get(f"{base_url}/comments?postId=1")
        comments = response.json()
        for comment in comments:
            assert "@" in comment["email"]
            assert "." in comment["email"]

    def test_response_time_acceptable(self, session, base_url):
        """Response should come back in under 3 seconds"""
        import time
        start = time.time()
        session.get(f"{base_url}/posts")
        elapsed = time.time() - start
        assert elapsed < 3.0, f"Response time too slow: {elapsed:.2f}s"