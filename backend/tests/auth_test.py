def test_login(client):
    response = client.post("/users/login", json={"username": "root", "password": "toor"})
    cookies = response.headers.getlist('Set-Cookie')
    access_token_flag = False
    for cookie in cookies:
        if cookie.startswith('access_token='):
            access_token_flag = True
    refresh_token_flag = False
    for cookie in cookies:
        if cookie.startswith('refresh_token='):
            refresh_token_flag = True
    assert access_token_flag and refresh_token_flag


def test_is_auth(client):
    response = client.post("/users/login", json={"username": "root", "password": "toor"}, follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if not cookies:
        assert False
    response = client.post("/users/is-auth")
    response = response.get_json()
    assert response["auth"] == True


def test_logout(client):
    response = client.post("/users/login", json={"username": "root", "password": "toor"}, follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if not cookies:
        assert False
    response = client.get("/users/logout", follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if cookies:
        assert False
    assert True


def test_refresh(client):
    response = client.post("/users/login", json={"username": "root", "password": "toor"}, follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if not cookies:
        assert False
    cookies_str = '; '.join(cookies)
    start_index = cookies_str.find("access_token=")
    if start_index != -1:
        end_index = cookies_str.find(";", start_index)
        if end_index == -1:
            end_index = len(cookies_str)
        cookies_str = cookies_str[:start_index] + cookies_str[end_index:]
    response = client.get("/users", headers={'Cookie': cookies_str})
    users = [{"id": 1, "username": "root"}]
    if list(response.json) != users:
        assert False
    response = client.post("/users/refresh", follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if not cookies:
        assert False
    response = client.get("/users")
    users = [{"id": 1, "username": "root"}]
    assert list(response.json) == users





def test_get_all_users(client):
    response = client.post("/users/login", json={"username": "root", "password": "toor"}, follow_redirects=True)
    cookies = response.headers.getlist('Set-Cookie')
    if not cookies:
        assert False
    response = client.get("/users")
    users = [{"id": 1, "username": "root"}]
    assert list(response.json) == users