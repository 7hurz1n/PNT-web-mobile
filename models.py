from db import db

class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ocorrencia = db.Column(db.String(100), nullable=False)
    detalhes = db.Column(db.String(200), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f'<Ocorrencia {self.ocorrencia}>'