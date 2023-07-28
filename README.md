# newpro

create Virtual environment:
- python -m venv vagar.


To activate and run your Django virtual environment called "vagar", you can follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the root directory of your Django project where the virtual environment is located.
3. Activate the virtual environment by running the appropriate activation command depending on your operating system:

For Windows:
vagar\Scripts\activate
For macOS and Linux:
source vager/bin/activate

Once the virtual environment is activated, you will see its name (in this case, "vagar") in your terminal prompt.

Install requirements.txt using "pip install -r requirements.txt".

Run the Django development server by executing the following command in the terminal:
"python3 manage.py runserver"


Django will start the development server, and you will see the server address (usually http://127.0.0.1:8000/) in the terminal output.
Open your web browser and navigate to the server address shown in the terminal to access your Django application.
By following these steps, you will activate and run your Django virtual environment called "vagar" and start the development server to run your Django application.


migration commands
--------------------------------
# migrating the app and database changes
$ python manage.py makemigrations

# final migrations
$ python manage.py migrate


Creating superAdmin
----------------------------
python manage.py createsuperuser 

available superUser
-------------------
name: theo
email:unekwutheophilus@gmail.com
pwd:Otusegwa360@

Visiting the admin url
------------------------
http://localhost:8000/admin/


