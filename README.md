# RentSystem
Rent System FastAPI Template

The template of the Rent System is about one or more “things” property of the one natural person “owner” that is rented for a period of time to another natural person “renter”. The target of the project is to implement an API Rest with a few endpoints to manage the basic rent operations., as an example, the structure of the project and use of the framework FastAPI.

Python and the Framework FastAPI are the technologies used in its project. Its template is based on the Udemy Complete FastAPI REST course + AWS + Emails + Payments, Instructor Ines Ivanova-Kenova, Software engineer.

Process

Data Model

Tables
Users - primary data of persons
Owners -they have some things that to want to rent
Renters - they want to rent some things
Objects_to_rent - some things to rent
Bids - offer for some things to rent
Renting - bids accepted by the owner and the renter will use it and pay the rate confirmed for the time defined bids accepted by the owner and renter will use and pay for it
Relations
Owners and renters are users
The objects are managed by the owners
The bids are created by renters and include a objects
Rentings are bid accepted by owners


Requeriments.txt

Configurations

.env (definitions for config module)
DB_NAME=postgresql
DB_USER=xxx
DB_PASSWORD=xxx
DB_SERVER=localhost
DB_PORT=5432
DB_NAME_DATABASE=renting
JWT_SECRET=xxx
Create database “renting” and use Alembic to create tables.
alembic revision --autogenerate -m "Initial"
alembic upgrade head






Template Implementation Characteristics

Folder Structure:
Models: class to define tables
Managers: class to manage endpoints
Resources: endpoints and routers
Schemas: Pydantic class to define a class for validating data
The user and pass are in the .env file, using the python-decouple library. If you are working with Git, update your .gitignore adding the .env file so you don’t commit any sensitive data to your remote repository.
The project is using Alembic to manage tables in the database. Alembic is a lightweight database migration tool with the SQLAlchemy Database Toolkit for Python (https://alembic.sqlalchemy.org/en/latest/).
Registration and authentication
Security using JWT tokens and secure password hashing.
Token with an expiration time of 120 minutes.
Email must be unique
We have two endpoints: register and login
Schemas are used to validate data in the request
Register and Login
Register: users by default are users (other is admin), and status is enabled.
Login: if login is a success, it returns a JWT for authentication of the following requests. The user must have a state "enable".

Authorization
The role of the user (admin, owner, or renter) is used by authorization for consuming the endpoint.
It is implemented as dependency (is_enable)(is_admin) of the endpoint 
Users Endpoints


