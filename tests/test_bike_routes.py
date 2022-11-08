def test_get_all_bikes_with_empty_db_returns_empty_list(client):
    response = client.get("/bike")
    response_body = response.get_json()
    
    assert response.status_code ==200
    assert response_body == []

def test_get_one_bike_with_empty_db_returns_404(client):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body

def test_getting_one_bike_in_populated_datbase_returns_bike_json(client, two_bikes):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Speedy",
        "price":1,
        "size":6,
        "type":"racing"
        }

def test_post_1_bike_creates_new_bike_in_db(client, two_bikes):
    response = client.post("/bike", json={
        "name":"Ernie",
        "price": 5,
        "size": 100,
        "type":"imaginary"
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 3
