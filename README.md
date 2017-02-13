Development Installation Instructions
=====================================

##### creates initial database.  Make sure to edit *settings.dev* for your database user/pass

    mysql -e "create database alr"

##### OPTIONAL: creates a new isolated python environment for all dependencies in application

    mkvirtualenv alr

##### installs all the python libraries necessary for the application


    pip install -r requirements.txt

##### sets an environment variable specifying which settings we want to use. In our case, it's "dev"


    export DJANGO_SETTINGS_MODULE=settings.dev

##### initial script to create db tables and also asks for a new admin user/password, so create it now


    python manage.py syncdb

##### migrates database from evolving schemas (uses South)


    python manage.py migrate

##### loads a fully populated survey


    python manage.py loaddata abbreviated.json

##### runs the server in development mode on http://0.0.0.0:9004 & http://0.0.0.0:9004/admin

    python manage.py runserver 0.0.0.0:9004



Production Installation Instructions (expands on above)
=====================================

### sets an environment variable specifying which settings we want to use. In our case, it's "prod"


    export DJANGO_SETTINGS_MODULE=settings.prod

### copy all the static files to the right spot so your web server can serve them without the actual application having to do the work

    python manage collectstatic
