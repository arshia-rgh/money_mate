# Money Mate

![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)

## Description

This project is an Expense Tracker API built with FastAPI. It allows users to manage their expenses, budgets, incomes
user accounts using Firebase Authentication and Firestore.

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
    - Add your Firebase API key and other configurations to the `.env` file:
        ```dotenv
        FIREBASE_API_KEY=your_firebase_api_key
        databaseURL=https://your-database-url

        MAIL_USERNAME=your_email
        MAIL_PASSWORD=your_email_password
        MAIL_FROM=your_email
        MAIL_PORT=587
        MAIL_SERVER=smtp.gmail.com
        MAIL_FROM_NAME=New Notifications
        ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

### Endpoints

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.