from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/meu_banco'
db = SQLAlchemy(app)

from route import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)