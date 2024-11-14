# CGA Manager

CGA Manager is a Django-based web application for managing various aspects of factory operations, including **production**, **warehouse inventory**, **employee roles and assignments**, and **machine tracking**. The application is designed to help streamline processes and improve productivity in a factory setting.

## Project Structure

The project is organized into modular Django apps to separate different functional areas:

- **core**: Contains common resources and the homepage view.
- **human_resources**: Manages employees, roles, and authentication.
- **production**: Handles production details, machine assignments, and productivity tracking.
- **warehouse**: Manages inventory, including product types, brands, and specific product details.
- **maintenance**: (future implementation) Will handle machine maintenance schedules and logs.
- **sales**: (future implementation) Will manage sales records and client orders.

## Key Features

- **Role-Based Access**: Different views and data access based on roles (Admin, Supervisor, Worker).
- **Database Seeding**: Automated setup for sample data (e.g., machines, products, employees) using Django management commands.
- **PostgreSQL Integration**: Configured to use PostgreSQL as the database backend.
- **Modular Design**: Each functionality is organized in separate Django apps for better scalability and maintainability.

## Prerequisites

1. **Python**: Make sure Python (version 3.8 or later) is installed.
2. **PostgreSQL**: Ensure PostgreSQL is installed and running.
3. **Python Virtual Environment**: It is recommended to set up a virtual environment.

## Initial Setup

1. **Install dependencies**:
    ```bash
    pip install -r requirements. txt
    ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the project root with the following variables to configure the PostgreSQL database:
   ```plaintext
   DB_NAME=cga_data
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost  # or your database server's IP
   DB_PORT=5432       # default port
