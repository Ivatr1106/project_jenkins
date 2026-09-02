

import pytest

from app import app
from config.database import db

from models.department import Department
from models.designation import Designation
from models.employee import Employee
from models.user import User
from models.leave_type import LeaveType


@pytest.fixture
def client():

    app.config["TESTING"] = True

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "sqlite:///:memory:"

    with app.app_context():

        db.drop_all()
        db.create_all()

        department = Department(
            name="IT"
        )

        designation = Designation(
            name="Developer"
        )

        db.session.add(
            department
        )

        db.session.add(
            designation
        )

        db.session.add(
            LeaveType(
                name="Casual Leave",
                days=12
            )
        )

        db.session.commit()

        employee = Employee(
            name="Test Employee",
            email="test@gmail.com",
            phone="1234567890",
            department_id=department.id,
            designation_id=designation.id
        )

        db.session.add(employee)
        db.session.commit()

        user = User(
            email="test@gmail.com",
            password=(
                "$pbkdf2-sha256$29000$"
            ),
            role="employee",
            employee_id=employee.id
        )

        from werkzeug.security import generate_password_hash

        user.password = generate_password_hash(
            "password123"
        )

        db.session.add(user)
        db.session.commit()

        with app.test_client() as test_client:

            yield test_client

        db.session.remove()
        db.drop_all()