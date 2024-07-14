# Services Warranty Invoice Checker

## Overview

This is a Python Flask web application designed to check SKOPE Services invoices for jobs that are very expensive or stand out from the others for some reason. This project was created to help streamline the review process for warranty claims and highlight potential issues.

## Features

- **Feature 1**: Parses the .csv export of the job list for the invoice and removes unwanted data.
- **Feature 2**: Produces an Excel spreadsheet with the top selected jobs for review with only the required information.
- **Future Features**: Will include AI analysis of the notes to identify irregular jobs and highlight jobs that should not be covered under warranty, such as installations.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tlskope/services_warranty_invoice_checker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd services_warranty_invoice_checker
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory of the project and add the necessary configuration variables:
    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

### Running the Application

To start the Flask application, run the following command:
```sh
flask run
