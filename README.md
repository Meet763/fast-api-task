# FlasApi Backend

 This project implements a user authentication system using **JWT** (JSON Web Tokens) with **FastAPI** and **MongoDB**. It includes a user CRUD system with secured endpoints and implements role-based access control (RBAC) for fine-grained authorization. This project also covers logging support, predefined Pydantic models, and is structured for scalability. The system is designed for deployment on cloud platforms like **MongoDB Atlas** and **Render** (or any other free serverless service).

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

The FastApi backend has been deployed on Render . You can access the live version of the backend at the following URL:

https://fast-api-task-cpfq.onrender.com


