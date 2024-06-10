# This script will initialize a new project by migrating the database, collecting static files, and creating a superuser.
# This script should be run after the project has been cloned and the virtual environment has been activated.

# Migrate the database
python Cybersecurity_forms/manage.py makemigrations
python Cybersecurity_forms/manage.py migrate
# Collect static files
python Cybersecurity_forms/manage.py collectstatic --noinput
# Create a superuser
python Cybersecurity_forms/manage.py createsuperuser --noinput
# Start the server
python Cybersecurity_forms/manage.py runserver 0.0.0.0:8000