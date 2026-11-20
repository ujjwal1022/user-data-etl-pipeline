User Data ETL Pipeline
A beginner Python ETL project that extracts user data from an API, transforms nested JSON fields, and loads the data into a CSV file.

Features
API Pagination
Environment Variable Configuration
Retry Logic for API Failures
CSV Export
Error Handling
Technologies
Python
Requests
Dotenv
CSV Module
Folder Structure
MiniApiProject/
│
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
└── .env
Setup
Install dependencies:

pip install -r requirements.txt
Create a .env file:

API_URL=https://jsonplaceholder.typicode.com/users
Run:

python main.py
Output:

users.csv
ETL Flow
Extract user records from API
Transform nested address data
Load transformed data into CSV