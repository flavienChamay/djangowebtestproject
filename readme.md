DJANGO WEB TEST PROJECT:
This project is based on tutorials of Corey Schafer

HOW TO LAUNCH THE PROJECT:
In a terminal at the root of the project, type:
python manage.py runserver

By default, the adress of the site should be : http://127.0.0.1:8000/

TO UPDATE MIGRATIONS:
python manage.py makemigrations
python manage.py migrate

Programs requirements:
See requirements.txt file in root directory of the source code's website.
Be sure to use a virtual env and install those packages before exporting the virtual env into the server.

WARNING:
This site is not operationnal yet, many errors where found like apache not wanting to restart properly.
The site is not live but all its functionalities to do so are implemented.
The user's email name and its associated password are not present, this is maybe why apache refuses to starts.
But, for security reasons, I didn't used my email username and password. I will see in the future how I can use the site without those informations.
Here is the apache error:
apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Wed 2021-01-27 19:35:38 UTC; 1min 43s ago
       Docs: https://httpd.apache.org/docs/2.4/
    Process: 376504 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)

