# Data Pusher Documentation

## Overview
Data Pusher is a Django web application designed to receive JSON data and push it across different platforms (destinations) based on account configurations using webhook URLs. It provides APIs for creating, retrieving, updating, and deleting accounts and their associated destinations. The application ensures data integrity and security by validating incoming data and authenticating requests using secret tokens.

## Getting Started

To get started with the project, follow these instructions:

1. Clone the repository to your local machine:
      git clone https://github.com/prudhvikollanapK/Assessment.git

2. Navigate to the project directory:
      cd Assessment

3. Install project dependencies using pip:
      pip install -r requirements.txt

4. Run migrations to create the database schema:
       python manage.py makemigrations
       python manage.py migrate

5. Start the development server:
       python manage.py runserver

6. Database administration(optional):
       python manage.py createsuperuser

7. Access the application in your web browser at http://localhost:8000.


## API Endpoints

The project provides the following API endpoints:

## Accounts API Endpoints
- `GET /accounts/`:
Retrieve a list of all accounts.
- `POST /accounts/`:
Create a new account.
- `GET /accounts/{account_id}/`:
Retrieve details of a specific account.
- `PUT /accounts/{account_id}/`:
Update details of a specific account.
- `DELETE /accounts/{account_id}/`:
Delete a specific account.
Destinations API Endpoints
- `POST /accounts/{account_id}/destinations/`:
Create a new destination for the specified account.
- `GET /accounts/{account_id}/destinations/`:
Retrieve a list of all destinations for the specified account.
Data Pushing Endpoint
- `POST /receive_data/`:
Receive JSON data and push it to destinations configured for the associated account.

## Postman APIs

For easier interaction with the APIs, you can use the provided Postman collection. Import the collection into Postman to access the following APIs:

- Data Pusher System APIs: [Data Pusher.postman_collection.json]

## Authentication
Authentication for API endpoints is handled using secret tokens associated with each account. Tokens are generated automatically during account creation.

## Additional Notes
Ensure that appropriate HTTP methods and headers are configured for each destination to facilitate proper data delivery.
Implement additional security measures such as SSL/TLS encryption for enhanced data protection during transmission.

## Contributing

Contributions to the project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.
