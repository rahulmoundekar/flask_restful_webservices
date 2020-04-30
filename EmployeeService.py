from flask import jsonify

from db.db import db
from models.app_model import Employee


def get_employees():
    employees = Employee.query.all()
    return jsonify(employees=[e.serialize() for e in employees])


def get_employee(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return jsonify(employee=employee.serialize())


def create_employee(name, email, contact):
    employee = Employee(name=name, email=email, contact=contact)
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee=employee.serialize())


def update_employee(employee_id, name, email, contact):
    employee = Employee.query.filter_by(id=employee_id).first()
    employee.name = name
    employee.email = email
    employee.contact = contact
    db.session.commit()

    return 'Updated a Employee with id %s' % employee_id


def delete_employee(employee_id):
    employee = Employee.query.filter_by(id=employee_id).one()
    db.session.delete(employee)
    db.session.commit()
    return 'Removed Employee with id %s' % employee_id
