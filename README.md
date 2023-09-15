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
You should have a _./venv_ folder in your application folder. Now activate the isolated environment, so all our packages will be installed there, a virtual environment is activated differently for Mac OSX and Windows.

_Mac OSX_
```console
source venv/bin/activate
```

_Windows_
```console
.\venv\Scripts\activate.bat
```
Next let's bootstrap the django application:
```console
django-admin startproject person
```
Next lets create an app for our _person_ project, make sure you _cd person_ before running the command below:
```console
django-admin startapp RestAPI
```

After activating, you should see _(venv)_ in your terminal, install the packages in the _requirements.txt_ by using the command below:

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
You should have a new directory _RestAPI_ created and it should have the following files and folder.

```console
 ./RestAPI
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```

Create two additional files <mark>serializers.py</mark> and <mark>urls.py</mark> in the directory ./RestAPI.

