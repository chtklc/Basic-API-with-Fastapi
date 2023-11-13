# Basic-API-with-Fastapi
The goal of this project is to build a RESTful API system using FastAPI, with Uvicorn
serving as the server, and Python as the backend programming language. This system
allows for the efficient processing of HTTP requests from various clients, such as web
browsers and API testing tools
Components
![image](https://github.com/chtklc/Basic-API-with-Fastapi/assets/149814348/25b6aaf3-2117-43e5-96f4-8dcceb5604dc)

Clients: Chrome browser and Postman are clients in this context. Chrome can be
used to make GET requests directly from the browser's address bar, while Postman
allows you to make GET, POST, PUT, and DELETE requests and provides a more
comprehensive interface for API testing
FastAPI: Our chosen web framework, FastAPI, will handle endpoint routing, request
processing, and response generation. It provides a robust and efficient platform for
building RESTful APIs
Uvicorn: Uvicorn is employed as the ASGI server to run our FastAPI application. It
listens for incoming HTTP requests, forwards them to the FastAPI application, and
sends back the responses
Python Backend: Python serves as the backend programming language. It contains
the application logic, data models, and endpoint handlers, ensuring seamless
integration with FastAPI
Database: In this project, a simple dictionary is used which acts as a placeholder for
a database. It simulates the storage of car data within your API. While it's not a fullfledged database system, it serves the purpose of illustrating API fuctionality.
Swagger/OpenAPI: We use Swagger/OpenAPI to automatically generate interactive
API documentation at endpoints like "/docs". This documentation allows users to
explore, test, and understand the APIs
![image](https://github.com/chtklc/Basic-API-with-Fastapi/assets/149814348/b4c782fe-f88f-4f90-a14c-f351c440577a)


Theoretical Concepts
What is FastAPI?
modern, high-performance, and easy-to-use web framework for building APIs with
Python
designed to make it simple to create web APIs quickly and efficiently while also
providing automatic interactive documentation
Interactive API Documentation: FastAPI generates interactive API documentation
automatically using the OpenAPI and Swagger standards. This documentation is
accessible through a web interface and helps to understand and test the API.
FastAPI is built with asynchronous programming in mind, allowing you to write
asynchronous code when needed for I/O-bound tasks
It supports various authentication and authorization mechanisms, making it suitable
for building secure APIs.
What is Pydantic?
Python library for data validation and parsing
provides a convenient and declarative way to define data schemas and validate
input data
Automatic Parsing: It can automatically parse and convert data from various sources
(e.g., JSON, dictionaries) into Python objects based on your data class definitions.
Data Modeling: It is often used for modeling and validating data structures,
especially when working with APIs, databases, or external data sources.
What is Swagger/OpenAPI?
provides a clear and standardized way to document APIs, making it easier to
understand how to use the API, what endpoints are available, and what data formats
to expect
enable automatic validation of API requests and responses against the defined
schema, helping to ensure data consistency and correctness
integrated in FastAPI
What is Uvicorn?
ASGI (Asynchronous Server Gateway Interface) server that is commonly used to run
Python web applications, including frameworks like FastAPI
designed for serving web applications asynchronously, making it well-suited for
high-performance, real-time, and asynchronous web applications
includes a convenient "--reload" option that automatically detects code changes in
your application and restarts the server, making it suitable for development and
debugging.
![image](https://github.com/chtklc/Basic-API-with-Fastapi/assets/149814348/bf64e847-b6ac-4cc7-a00c-f767d5d4b073)

