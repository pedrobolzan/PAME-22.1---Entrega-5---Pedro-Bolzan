from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

checklist_api = Blueprint("checklist_api", __name__)

class Checklist(BaseModel):
    __tablename__ = "checklist"
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100), nullable=False)
    agendamento = db.Column(db.Boolean, unique=True, default = False)
    cadastro = db.Column(db.Boolean, unique=True, default = False)
    checkin = db.Column(db.Boolean, unique=True, default = False)
    triagem = db.Column(db.Boolean, unique=True, default = False)
    consulta = db.Column(db.Boolean, unique=True, default = False)
    checkout = db.Column(db.Boolean, unique=True, default = False)
    limpeza = db.Column(db.Boolean, unique=True, default = False)

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "agendamento": self.agendamento,
            "cadastro": self.cadastro,
            "checkin": self.checkin,
            "triagem": self.triagem,
            "consulta": self.consulta,
            "checkout": self.checkout,
            "limpeza": self.limpeza
        }