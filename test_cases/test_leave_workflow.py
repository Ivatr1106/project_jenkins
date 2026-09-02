

def test_approve_leave(client):

    create_response = client.post(
        "/leaves",
        json={
            "employee_id": 1,
            "leave_type_id": 1,
            "start_date": "2026-08-20",
            "end_date": "2026-08-21",
            "reason": "Personal"
        }
    )

    assert create_response.status_code == 201

    leave_id = (
        create_response
        .get_json()["leave"]["id"]
    )

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "hr"
        session["employee_id"] = 1

    response = client.put(
        f"/leaves/{leave_id}/approve"
    )

    assert response.status_code == 200

    assert (
        response
        .get_json()["leave"]["status"]
        == "approved"
    )


def test_reject_leave(client):

    create_response = client.post(
        "/leaves",
        json={
            "employee_id": 1,
            "leave_type_id": 1,
            "start_date": "2026-08-22",
            "end_date": "2026-08-23",
            "reason": "Personal"
        }
    )

    leave_id = (
        create_response
        .get_json()["leave"]["id"]
    )

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "hr"
        session["employee_id"] = 1

    response = client.put(
        f"/leaves/{leave_id}/reject"
    )

    assert response.status_code == 200

    assert (
        response
        .get_json()["leave"]["status"]
        == "rejected"
    )