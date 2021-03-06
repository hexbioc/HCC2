from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message
from flask_login import LoginManager
from config import config
from flaskext.mysql import MySQL 

mysql = MySQL()
bootstrap = Bootstrap()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



 

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

   
    mysql.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint,url_prefix='/student')

    from .doctor import doctor as doctor_blueprint
    app.register_blueprint(doctor_blueprint,url_prefix='/doctor')

    return app




