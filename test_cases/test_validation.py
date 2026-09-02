

def test_missing_employee_name(client):

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "hr"
        session["employee_id"] = 1

    response = client.post(
        "/employees/add",
        data={
            "email": "new@gmail.com"
        }
    )

    assert response.status_code == 200


def test_missing_leave_type(client):

    response = client.post(
        "/leaves",
        json={
            "employee_id": 1,
            "start_date": "2026-08-20",
            "end_date": "2026-08-21"
        }
    )

    assert response.status_code == 400