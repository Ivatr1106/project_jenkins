
def test_create_leave(client):

    response = client.post(
        "/leaves",
        json={
            "employee_id": 1,
            "leave_type_id": 1,
            "start_date": "2026-08-20",
            "end_date": "2026-08-21",
            "reason": "Personal work"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["leave"]["status"] == "pending"


def test_invalid_leave_dates(client):

    response = client.post(
        "/leaves",
        json={
            "employee_id": 1,
            "leave_type_id": 1,
            "start_date": "2026-08-25",
            "end_date": "2026-08-20",
            "reason": "Test"
        }
    )

    assert response.status_code == 400


def test_leave_without_employee(client):

    response = client.post(
        "/leaves",
        json={
            "leave_type_id": 1,
            "start_date": "2026-08-20",
            "end_date": "2026-08-21"
        }
    )

    assert response.status_code == 400