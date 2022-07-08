from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

agendamento_api = Blueprint("agendamento_api", __name__)

class Agendamento(BaseModel):
    __tablename__ = "agendamento"
    
    id = db.Column(db.Integer, primary_key = True)
    nomeResponsavel = db.Column(db.String(100))
    nomeCrianca = db.Column(db.String(100), unique = True)
    nascimento = db.Column(db.String(100))
    telefone = db.Column(db.String(11))
    email = db.Column(db.String(100))
    data = db.Column(db.String(100))
    horario = db.Column(db.String(100))

    def json(self):
        return {
            "id": self.id,
            "nomeResponsavel": self.nomeResponsavel,
            "nomeCrianca": self.nomeCrianca,
            "nascimento": self.nascimento,
            "telefone": self.telefone,
            "email": self.email,
            "data": self.data,
            "horario": self.horario
        }