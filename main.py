from flask import Flask
from models import Ocorrencia
from db import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db.init_app(app)

from route import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)