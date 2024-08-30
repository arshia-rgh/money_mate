# Money Mate

![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)
## Description
This project is an Expense Tracker API built with FastAPI. It allows users to manage their expenses, budgets, incomes user accounts using Firebase Authentication and Firestore.
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/arshia-rgh/money_mate
    cd money_mate
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add your Firebase API key to the `.env` file:
        ```
        FIREBASE_API_KEY=your_firebase_api_key
        ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### User Endpoints

- **POST /signup**: Create a new user.
    - Request Body: `UserCreate`
    - Response: `{"message": "User created successfully", "uid": "user_uid"}`

- **POST /login**: Log in a user.
    - Request Body: `UserLogin`
    - Response: `{"message": "Login successful", "token": "id_token"}`

- **DELETE /delete**: Delete a user account.
    - Query Parameter: `user_id`
    - Response: `{"message": "Your user deleted successfully"}`

- **PATCH /update**: Update a user account.
    - Query Parameter: `user_id`
    - Request Body: `UserCreate`
    - Response: `{"message": "Your account has been updated successfully"}`

- **GET /profile**: Retrieve a user account.
    - Query Parameter: `user_id`
    - Response: User data

### Expense Endpoints

- **POST /add**: Add a new expense.
    - Request Body: `Expense`
    - Response: `{"message": "Expense added successfully"}`

- **DELETE /delete**: Delete an expense.
    - Query Parameter: `expense_id`
    - Response: `{"message": "Expense deleted successfully"}`

- **PATCH /update**: Update an expense.
    - Query Parameter: `expense_id`
    - Request Body: `Expense`
    - Response: `{"message": "Expense updated successfully"}`

- **GET /retrieve**: Retrieve an expense.
    - Query Parameter: `expense_id`
    - Response: Expense data

this list will be updated soon

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.