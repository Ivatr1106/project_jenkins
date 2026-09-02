

def test_login_page(client):

    response = client.get("/login")

    assert response.status_code == 200


def test_valid_login(client):

    response = client.post(
        "/login",
        data={
            "email": "test@gmail.com",
            "password": "password123"
        },
        follow_redirects=False
    )

    assert response.status_code == 302


def test_invalid_login(client):

    response = client.post(
        "/login",
        data={
            "email": "wrong@gmail.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data


def test_unauthorized_hr_dashboard(client):

    response = client.get(
        "/hr/dashboard"
    )

    assert response.status_code in [
        302,
        403
    ]