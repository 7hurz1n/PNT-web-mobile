from db import db

class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Ocorrencia {self.email}>'