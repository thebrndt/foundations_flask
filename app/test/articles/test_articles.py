def test_articles_success(client):
    response = client.get("/blog/")
    assert response.status_code == 200
