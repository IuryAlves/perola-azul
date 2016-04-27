from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy

# cria o  app
app = Flask(__name__)

# configura o app a partir do settings
app.config.from_object('settings')

# configura cors
enable_cors = app.config.get("ENABLE_CORS", False)
if enable_cors:
    CORS(app, resources={
        r"/*": {"origins": "*"},
    })

# configura login manager
login_manager = LoginManager()
login_manager.init_app(app)


# configura o banco

db = SQLAlchemy(app)

from user.resources import user_blueprint

app.register_blueprint(user_blueprint)


@login_manager.user_loader
def load_user(user_id):
    pass
