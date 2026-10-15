# FastApiExample
Employee Management API
A simple FastAPI application to create, view, update, and delete employees.

Features
Welcome endpoint.

List all employees.

Add employees with automatically generated UUIDs.

Update and delete employees by ID.

Project Structure
text
main.py
README.md
Installation
Run in your project folder:

bash
python -m pip install fastapi "uvicorn[standard]"
Run the Application
bash
python -m uvicorn main:app --reload
Application: http://127.0.0.1:8000

Swagger documentation: http://127.0.0.1:8000/docs

API Endpoints
Method	Endpoint	Description	Query Parameters
GET	/	Display welcome message	None
GET	/getEmployee	List all employees	None
POST	/employees	Add an employee	name, position
PUT	/employees	Update an employee	id, name, position
DELETE	/employees	Delete an employee	id
Parameters are passed in the URL query string, not as a JSON request body. The id must be a valid UUID.

Example Usage
Add an employee:

bash
curl -X POST "http://127.0.0.1:8000/employees?name=Ranjani&position=Developer"
List employees:

bash
curl "http://127.0.0.1:8000/getEmployee"
Update an employee (replace <employee-id> with the returned UUID):

bash
curl -X PUT "http://127.0.0.1:8000/employees?id=<employee-id>&name=Ranjani&position=Senior%20Developer"
Delete an employee:

bash
curl -X DELETE "http://127.0.0.1:8000/employees?id=<employee-id>"
You can also test all endpoints through the Swagger documentation page.

Notes
Employee records are stored in an in-memory list, not a database. Restarting the application clears the records.

No authentication is implemented. This is a learning/demo project.

Update and delete return {"message": "Employee Not found!"} when an ID is not found, rather than an HTTP 404 error.

CORS is configured broadly in the source. Review allowed origins and credentials before deployment