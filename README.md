# Django-REST-API
## Introduction to REST and CRUD
Have you ever wondered how the websites you use the most operate? Yes, they are gorgeous, but a tiny component known as a REST API is what really powers them. So what is a REST API? Application programming interfaces are known as APIs. It is a collection of guidelines that permits communication between programs. The API is created by the developer on the server and made accessible to the client. 

REST controls how the API appears. "Representational State Transfer" is what it stands for. It is a set of guidelines that programmers adhere to when building an API. One of these rules stipulates that when you link to a particular URL, you should be able to access a specific piece of information (referred to as a resource). Through HTTP Requests made to the provided urls, a REST API interfaces with the stunning front-end you are currently viewing, enabling you to carry out actions such as CREATE, READ, UPDATE and DELETE.

To be deemed REST, an API must follow four simple rules: Create, Read, Update, and Delete. Typically, to create a resource, we would use a POST request to a URL in our API, GET to read, PUT to update, and DELETE to delete.

## Set Up
First things first, make sure you have python installed on your PC or Mac. 
Create a folder for your project.
```console
mkdir  REST API
```

Open the folder with your favorite code editor and create a _requirements.txt_ file in the root folder of REST API.

It is best practice to create a virtual environment so that all the packages you use are specific to your application. Before we do any installing, let's create an isolated environment for our project. It could be confusing to distinguish between the packages you use in your global Python environment and the ones you require in your application. How did we accomplish that?

Make sure you are in the application folder and run the command you have below:
```console
python -m venv ./venv
```
You should have a _./venv_ folder in your application folder.


Next let's bootstrap the django application:
```console
django-admin startproject RestAPI
```
Next lets create an app for our _RestAPI_ project, make sure you _cd ResAPI_ before running the command below:
```console
django-admin startapp person
```
Install Django REST framework by running command;
```console
pip install djangorestframework
```

Now activate the isolated environment, so all our packages will be installed there, a virtual environment is activated differently for Mac OSX and Windows.

_Mac OSX_
```console
source venv/bin/activate
```

_Windows_
```console
.\venv\Scripts\activate.bat
```
After activating, you should see _(venv)_ in your terminal. Install the packages in the _requirements.txt_ by using the command below:

```console
pip install -r requirements.txt
```

In your _requirements.txt_ file you should have this;
```console
asgiref==3.7.2
Django==4.2.5
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3
```


## Time to code
You should have a new directory _person_ created and it should have the following files and folder.

```console
 ./person
        ./migrations
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```

Create two additional files **serializers.py** and **urls.py** in the directory _./person_.
Don't worry; you will soon understand why those two files exist.

First, in the ./RestAPI/RestAPI folder, go to the settings.py and add to INSTALLED_APPS, _person_ app and _rest_framework_.

```console
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework', # add this
        'person' # add this too
    ]
```

First let's define the model for our _person_, Go to the **models.py** file in the _./RestAPI/person_ and you should have this below:

```console
from django.db import models

    class person(models.Model):
        name = models.CharField(max_length=255)
```

We won't focus on the database we'll use in this lesson, so we'll just use the default Django sqlite db (isn't Django awesome?). A model simply describes how our database tables will be arranged.
