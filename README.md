# bit68_task
# Your Django App Name

A brief description of your Django app.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python (3.x recommended)
- Django (4.x recommended)
- Other dependencies:
    - `rest_framework`
    - `rest_framework.authtoken`
    - `rest_framework_simplejwt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/youssef-99/bit68_task.git
    cd bit68_task
    ```

2. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Migrate the database:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (optional but recommended):

    ```bash
    python manage.py createsuperuser
    ```

## Configuration

- Create a `.env` file in the project directory and set your environment variables. You can use the `.env.example` file as a template.

    ```bash
    cp .env.example bit68_task/.env
    ```

- Edit the `.env` file with your configuration.

## Usage

- Run the development server:

    ```bash
    python manage.py runserver
    ```

- Access the application in your web browser at [http://localhost:8000](http://localhost:8000)

- Access the Django admin at [http://localhost:8000/admin](http://localhost:8000/admin) (if you created a superuser)

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Please follow the [code of conduct](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
