# FastApi Backend

 This project implements a user authentication system using **JWT** (JSON Web Tokens) with **FastAPI** and **MongoDB**. It includes a user CRUD system with secured endpoints and implements role-based access control (RBAC)  for fine-grained authorization. This project also covers logging support, predefined Pydantic models, and is structured for scalability. The system is designed for deployment on cloud platforms like **MongoDB Atlas** and **Render** (or any other free serverless service).

## Features

- **User Signup**: Create new user accounts.
- **User Login & JWT Authentication**: Mock authentication using JWT tokens.
- **User Profile**: user can see own profile.
- **Role Based Access**: only Admin role can see all users detail

## Available API Endpoints

### 1. User Signup

- **Endpoint**: `POST /auth/signup`
- **Description**: Registers a new user account.

### 2. User Login

- **Endpoint**: `POST /auth/login`
- **Description**: Authenticates a user and returns a JWT.

### 3. Create Quiz

- **Endpoint**: `POST /users/profile`
- **Description**: user can see own profile.

### 4. Submit Quiz

- **Endpoint**: `POST /users/`
- **Description**: all users list but admin have only access

## Deployment

  The FastApi backend has been deployed on Render . You can access the live version of the backend at  the following URL:

  https://fast-api-task-cpfq.onrender.com

## Running Locally

Follow the steps below to run this project on your local machine:

### 1. Clone the Repository
First, clone the GitHub repository to your local machine: 

    git clone https://github.com/Meet763/fast-api-task
    cd fast-api-task

### 2. Clone the Repository
Create and activate a virtual environment to isolate your project dependencies:

    python -m venv venv
    .\venv\Scripts\activate

### 3. Install Dependencies
Once the virtual environment is activated, install the necessary dependencies:

    pip install -r requirements.txt

### Run the FastAPI Application
To run the FastAPI application, execute the following command:

    fastapi run main.py

The server will start, and you can access the backend at http://127.0.0.1:8000.

### 5. Testing the API

You can test the API by navigating to the /docs endpoint on your browser (http://127.0.0.1:8000/docs) to explore and interact with the API using Swagger UI.





   
 




