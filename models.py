from db import db


class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ocorrencia = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Ocorrencia {self.ocorrencia}>'
