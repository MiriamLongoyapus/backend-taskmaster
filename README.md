
Before setting up the project, ensure you have the following installed:
Python 3.x
pip (Python package installer)
virtualenv (Optional but recommended)
PostgreSQL or SQLite (SQLite is used by default)

Installation
Follow these steps to get the project up and running:

Clone this repository to your local machine:
Copy this code to your terminal
git clone https://github.com/yourusername/task-manager-backend.git
cd task-manager-backend
Create and Activate a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:
python3 -m venv myenv
source myenv/bin/activate
Install Dependencies

Set Up the Database
If you're using SQLite (default), the database file will be created automatically. For PostgreSQL, you'll need to set up the database first:


Create an admin user to access the Django admin interface:
python manage.py createsuperuser
Run the Development Server

Start the development server:
python manage.py runserver
The API will be available at http://localhost:8000.

CHALLENGES
The challenge I faced on the backend was that my model changes were not reflected in the admin interface because the migrations had not been applied. 
I resolved this issue by deleting the previous migrations, allowing the system to apply the correct migrations.
