

import io


def test_document_upload(client):

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "employee"
        session["employee_id"] = 1

    response = client.post(
        "/documents",
        data={
            "employee_id": "1",
            "file": (
                io.BytesIO(
                    b"test document"
                ),
                "certificate.pdf"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 201


def test_invalid_document_type(client):

    with client.session_transaction() as session:

        session["user_id"] = 1
        session["role"] = "employee"
        session["employee_id"] = 1

    response = client.post(
        "/documents",
        data={
            "employee_id": "1",
            "file": (
                io.BytesIO(
                    b"test"
                ),
                "virus.exe"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 400