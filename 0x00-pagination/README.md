# 0x00-pagination

Welcome to the 0x00-pagination project in the ALX Backend repository! This project focuses on implementing and understanding pagination techniques in backend development. Pagination is crucial for efficiently handling large datasets by breaking them into manageable chunks.

## Project Overview

In this project, you will learn how to:

- Implement pagination in a backend API.
- Handle different pagination strategies such as offset-based and cursor-based pagination.
- Optimize database queries for efficient data retrieval.
- Provide a user-friendly API for navigating through paginated data.

## Technologies Used

- **Programming Languages**: Python
- **Framework**: Flask
- **Database**: SQLite (for demonstration purposes)
- **Tools**: Postman (for testing API endpoints)

## Project Structure

The project directory is organized as follows:

```
0x00-pagination/
├── README.md
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_pagination.py
└── requirements.txt
```

- **app/**: Contains the main application code, including initialization, models, routes, and utility functions.
- **tests/**: Contains unit tests for the pagination functionality.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python (>= 3.8)
- SQLite (optional, comes pre-installed with Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alx-backend.git
   cd alx-backend/0x00-pagination
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Running the Project

1. Initialize the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

2. Run the Flask application:

   ```bash
   export FLASK_APP=app
   flask run
   ```

## Usage

### API Endpoints

- **Get Paginated Items**

  ```
  GET /items?page=<page_number>&page_size=<page_size>
  ```

  Retrieves a paginated list of items. Example:

  ```bash
  curl http://127.0.0.1:5000/items?page=1&page_size=10
  ```

### Testing

Run the tests using:

```bash
pytest tests/
```