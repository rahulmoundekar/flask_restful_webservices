from flask import Flask, request
from EmployeeService import get_employees, create_employee, update_employee, delete_employee, get_employee
from db.db import db
from models.app_model import Employee

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'
app.config.from_object('settings.Config')

# initialization
db.init_app(app)


@app.route('/employee', methods=['GET', 'POST'])
def employeeFunction():
    if request.method == 'GET':
        return get_employees()
    elif request.method == 'POST':
        data = request.get_json()
        return create_employee(name=data['name'], email=data['email'], contact=data['contact'])


@app.route('/employee', methods=['PUT'])
@app.route('/employee/<int:employee_id>', methods=['GET', 'DELETE'])
def employees(employee_id=None):
    if request.method == 'GET':
        return get_employee(employee_id)

    elif request.method == 'PUT':
        data = request.get_json()
        return update_employee(employee_id=data['id'], name=data['name'], email=data['email'], contact=data['contact'])

    elif request.method == 'DELETE':
        return delete_employee(employee_id)


# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')

# manager.run()
