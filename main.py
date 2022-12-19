import os
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Resource, Api
import logging
from application.config import LocalDevelopmentConfig, TestingConfig
from application.database import db
from application.models import User, Role

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = api = None
print("Importing dependant libraries.")

def create_app():
  app = Flask(__name__, template_folder="templates")
  if os.getenv('ENV') == "production":
    app.logger.info("Currently no production config. is setup.")
    raise Exception("Currently no production config. is setup.")
  elif os.getenv('ENV') == "testing":
    app.logger.info("Starting testing.")
    print("Starting testing.")
    app.config.from_object(TestingConfig)
  else:
    app.logger.info("Starting local development.")
    print("Starting local development.")
    app.config.from_object(LocalDevelopmentConfig)
  db.init_app(app)
  migrate = Migrate(app, db)
  api = Api(app)
  app.logger.info("App setup completed.")
  print("App setup completed.")
  # Setup Flask-Security
  user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
  security = Security(app, user_datastore)
  app.app_context().push()
  return app, api

app, api = create_app()
# Import and load all the controllers.
print("Importing all the controllers.")
from application.controllers import *

@app.errorhandler(404)
def page_not_found(e):
  # Set 404 status explicitly.
  return render_template('404.html'), 404

@app.errorhandler(403)
def not_authorized(e):
  # Set 403 status explicitly.
  return render_template('403.html'), 403

if __name__ == '__main__':
  # Run the Flask app.
  app.run(host='0.0.0.0', port=8080)
