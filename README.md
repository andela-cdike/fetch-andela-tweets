# TwitterAPI

This is a simple project to test the use of twitter api using just python and Django. So every refresh requires a refresh of the page.  
The app displays three panes each displaying the most recent tweets from Andela, Andela Nigeria and Andela Kenya. Each pane has a button at the bottom to refresh its tweets. There is also a central button for refreshing all the panes simultaneously.

## Installation

### Pre-requisites
+ Virtual Environment
+ Django 1.8  or greater
+ Python

### Steps
1. Clone this repo:  
```git clone <name of repo>```
2. Enter the directory and activate virtual environment (command used depends on if you are using virtualenv with virtualenvwrapper or not):  
e.g.
```makevirtualenv <name of virtual environment>``` or  
```virtualenv venv```
3. Install requirements with:  
``` pip install -r requirements.txt```
4. Ensure you are in the django project directory where the file manage.py is located. Then run:  
```python manage.py runserver```
5. Visit the page on your browser at `http://127.0.0.1:8000`

## Tests
I didn't observe TDD for this one. Needed to test it quickly. Hoping I can come back to write tests.
