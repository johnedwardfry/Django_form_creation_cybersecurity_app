# This script will initialize a new project by migrating the database, collecting static files, and creating a superuser.
# This script should be run after the project has been cloned and the virtual environment has been activated.

# Migrate the database
python cyber_security_forms_project/manage.py makemigrations

python cyber_security_forms_project/manage.py migrate
# Collect static files
python cyber_security_forms_project/manage.py collectstatic --noinput
# Create a superuser
python cyber_security_forms_project/manage.py createsuperuser --noinput
# Start the server
python cyber_security_forms_project/manage.py runserver 0.0.0.0:8001