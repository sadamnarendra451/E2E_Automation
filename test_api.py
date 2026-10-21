import requests


def test_get_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    # Status code 200 (Success) vachindho ledho test chesthunnam
    assert response.status_code == 200

    # Response Data ni verify chesthunnam
    data = response.json()
    assert data["id"] == 1
    print("API Test Success mawa!")