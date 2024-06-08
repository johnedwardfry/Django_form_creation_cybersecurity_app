# This script will initialize a new project by migrating the database, collecting static files, and creating a superuser.
# This script should be run after the project has been cloned and the virtual environment has been activated.

# Migrate the database
python manage.py migrate
# Collect static files
python manage.py collectstatic --noinput
# Create a superuser
python manage.py createsuperuser --noinput
# Start the server
python manage.py runserver 0.0.0.0:800