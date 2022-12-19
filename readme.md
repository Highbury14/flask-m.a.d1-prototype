# Local Setup
- Clone the project
- Run `local_setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

# Replit run
- Go to shell.
- Run `pip install --upgrade poetry`
- Click on `main.py` and click button run
- The web app will be availabe at https://<replname>.<username>.repl.co
- Format https://<replname>.<username>.repl.co

# Folder Structure

- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- `local_setup.sh` set up the virtualenv inside a local `.env` folder. Uses `requirements.txt` and `pip` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `static` - default `static` files folder. It serves at '/static' path. More about it is [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/static/).
- `static/bootstrap` We have already added the bootstrap files. It can be used.
- `static/style.css` Custom CSS.
- `templates` - Default flask templates folder


```
├── application
│   ├── config.py
│   ├── controllers.py
│   ├── database.py
│   ├── __init__.py
│   ├── models.py
│   └── __pycache__
├── db_directory
│   └── test.db
├── local_run.sh
├── local_setup.sh
├── main.py
├── requirements.txt
├── readme.md
├── static
│   ├── bootstrap
│   │   ├── css
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap-grid.css
│   │   │   ├── bootstrap-grid.min.css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap-reboot.css
│   │   │   ├── bootstrap-reboot.css.map
│   │   │   ├── bootstrap-reboot.min.css
│   │   │   ├── bootstrap-reboot.rtl.css
│   │   │   ├── bootstrap-reboot.rtl.min.css
│   │   │   ├── bootstrap.rtl.css
│   │   │   ├── bootstrap.rtl.min.css
│   │   │   ├── bootstrap-utilities.css
│   │   │   ├── bootstrap-utilities.min.css
│   │   │   ├── bootstrap-utilities.rtl.css
│   │   │   ├── bootstrap-utilities.rtl.min.css
│   │   └── js
│   │       ├── bootstrap.bundle.js
│   │       ├── bootstrap.bundle.min.js
│   │       ├── bootstrap.js
│   │       ├── bootstrap.min.js
│   └── style.css
└── templates
    ├── articles.html
    └── 404.html
```
