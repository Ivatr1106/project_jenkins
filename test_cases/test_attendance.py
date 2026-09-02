

def test_mark_attendance(client):

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "employee"
        session["employee_id"] = 1

    response = client.post(
        "/attendance",
        json={
            "employee_id": 1,
            "status": "present",
            "date": "2026-08-20"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["attendance"]["status"] == "present"


def test_invalid_attendance(client):

    response = client.post(
        "/attendance",
        json={
            "employee_id": 1,
            "status": "invalid"
        }
    )

    assert response.status_code == 400