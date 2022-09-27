def test_feedback(client):
    response = client.get('/feedback')
    assert b"<title>Feedback</title>" in response.data
    assert response.status_code == 200