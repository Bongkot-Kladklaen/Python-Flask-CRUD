# Python-Flask-CRUD
>Flask python framework using to create basic CRUD

## Table of Contents
  - [Demo](#demo)
  - [Screenshots](#screenshots)
  - [Technologies](#technologies)
  - [Setup](#setup)
  - [Config project](#config-project)
  - [License](#license)

## Demo
Here is a working live demo: [Basic flask CRUD](https://flask-basiccrud.herokuapp.com)
## Screenshots
Example web application page
### Home page
![](screenshots/home.png)
### Insert page
![](screenshots/insert.png)
### Update page
![](screenshots/update.png)
### Delete page
![](screenshots/delete.png)

## Technologies
Project is created with:
- [python3](https://www.python.org/)
- [flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Bootstrap 3](https://getbootstrap.com/docs/3.4/)

## Setup
To clone this project, you need [Git](https://git-scm.com) to install on your computer. command line below:

```zsh
# Clone this repository
$ git clone https://github.com/Bongkot-Kladklaen/Python-Flask-CRUD.git

# Go into the repository
$ cd Python-Flask-CRUD
```
## Config project
1. Create database and table :

    Open project `PHP-VueJS_CRUD` find folder: `database>database.sql` and Import file sql to database server for you
2. Config connect database server : 

    Open project `PHP-VueJS_CRUD` find file: `app.py` to config: hostname, username, password, database
 
    ```python
        # Config database connect
        hostname = 'localhost
        username = 'root'
        password = 'root'
        database = 'flask_db'
    ```

## License
[MIT](LICENSE)

