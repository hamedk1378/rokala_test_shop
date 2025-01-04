## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x

## Step-by-Step Setup

### 1. Create a Virtual Environment

First, create a virtual environment to isolate your project’s dependencies. In your terminal, run:

#### On Windows:
```bash
python -m venv venv
```

#### On macOS/Linux:
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment to ensure you're working within it.

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Requirements

Install the required Python packages using `pip` by running:

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in `requirements.txt`.

### 4. Make Migrations

Now, create the necessary database migrations for your project. Run the following command to generate migration files:

```bash
python manage.py makemigrations
```

### 5. Apply Migrations

Apply the migrations to your database by running:

```bash
python manage.py migrate
```

### 6. Create a Superuser

To access the Django admin interface, you need to create a superuser account. Run the following command and follow the prompts to create a superuser:

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

Now you can start the Django development server with the following command:

```bash
python manage.py runserver
```

### 8. Access the Project

Once the server is running, you can access the project in your browser at:

```
http://127.0.0.1:8000/
```

To access the Django admin panel, visit:

```
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials you created earlier.

---

## Database Design

For a better understanding of the database structure, refer to the **database diagram** located in the root of the project:  
`database_diagram.png`

---
