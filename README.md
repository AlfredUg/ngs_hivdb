# HIV Drug Resistance Database

This is the the HIV drug resistance database at Uganda Virus Research Virus (UVRI). It harbours sequence data, demographics and clinical data of study participants.


## Quick setup

create virtual environment

`virtualenv -p python3 uhivdb`

activate the new virtual environment (source uhivdb/bin/activate)

clone the repository from GitHub

`git clone https://github.com/AlfredUg/ngs_hivdb.git`

Make migrations 

`python manage.py makemigrations hivdb`

Commit the migrations

`python manage.py migrate`

Launch the application

`python manage.py runserver`

Project will now be running on the server.
