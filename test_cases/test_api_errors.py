

def test_invalid_employee_api(client):

    response = client.get(
        "/employees/9999"
    )

    assert response.status_code == 404

    data = response.get_json()

    assert "error" in data


def test_invalid_leave_api(client):

    response = client.put(
        "/leaves/9999/approve"
    )

    assert response.status_code in [
        403,
        404
    ]