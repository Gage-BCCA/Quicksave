# QuickSave
...or Quiksave... the name is to be determined.

This is a project using the Django framework. It features vanilla JavaScript and CSS using the BEM naming convention.
# Building the App
- Git Clone this repo
- Install Dependencies
    - ``` pip install django```
    - ``` pip install markdown ```
    - ``` pip install faker ```
- Navigate to the cloned directory
- Make Migrations
    - ``` python manage.py makemigrations ```
    - ``` python manage.py migrate ```
- Run the command to generate dummy data
    - ``` python manage.py generatedummydata ```
- Run the development server
    - ``` python manage.py runserver ```

### Still a Work-In-Progress
This site is still in its infancy. Lots of work is being done almost everyday. Check back in the future, or leave a suggestion if you have a feature you want to see.

## Apps and Their Purposes
There are just a few apps in QuickSave:
- Accounts
- Feed
- Core

#### Accounts
This app holds the login and register templates. It has the ExtendedUserData model, which is used to extend the built-in Django User model with additional data and functionality.

#### Feed
This is the primary part of the app. It holds the models for posts, games, and a few additional supporting models.

It holds all the templates that a logged in user sees, including the main feed page, search, game landing pages, game browsing, and individual post pages.

#### Core
The core app is for project level functionality for developers. Right now, the only thing it is used for is a command for generating dummy data to fill the site.

