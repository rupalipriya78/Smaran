from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'smaran-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    from .routes import main
    app.register_blueprint(main)
    
    return app