from re import M
from app.checklist.model import Checklist
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity
from flask import request, jsonify, render_template
from flask.views import MethodView
import bcrypt

class ChecklistCreate(MethodView): # rota = /registroChecklist

    def post (self):

        body = request.json

        id = body.get("id")
        
        email = body.get("email")
        senha = body.get("senha")
        
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        
        agendamento = body.get("agendamento")
        cadastro = body.get("cadastro")
        checkin = body.get("checkin")
        triagem = body.get("triagem")
        consulta = body.get("consulta")
        checkout = body.get("checkout")
        limpeza = body.get("limpeza")

        if isinstance(email, str) and\
            isinstance(senha, str) and\
                isinstance(agendamento, str) and\
                    isinstance(cadastro, str) and\
                        isinstance(checkin, str) and\
                            isinstance(triagem, str) and\
                                isinstance(consulta, str) and\
                                    isinstance(checkout, str) and\
                                        isinstance(limpeza, str):
            
            checklist1 = Checklist.query.filter_by(agendamento = agendamento).first()
            
            if checklist1:
                return {"code_status": "Dados inválidos, etapa já cadastrada"}, 400

            checklist1 = Checklist(email=email,
                                      senha=senha,
                                      agendamento=agendamento,
                                      cadastro=cadastro,
                                      checkin=checkin,
                                      triagem=triagem,
                                      consulta=consulta,
                                      checkout=checkout,
                                      limpeza=limpeza)

            checklist1.save()

            return checklist1.json(), 200

    def get (self):

        checklists = Checklist.query.all()

        return jsonify([checklist.json() for checklist in checklists]), 200

class Login(MethodView): # rota = /login
    def post (self):
        
        body = request.json

        email = body.get("email")
        senha = body.get("senha")

        user = Checklist.query.filter_by(email=email).first()

        if user and bcrypt.checkpw(senha.encode(),user.senha.encode()):
            return {"token":create_access_token(user.id, additional_claims={"usuario":"logado"})}, 200
        return {"msg":"email ou senha errado"}, 400

class UserSpecific(MethodView):

    def get(self, id):
        verify_jwt_in_request()
        if id == get_jwt_identity():
            user = Checklist.query.get(id)
            return user.json()
        return {"msg":"token invalido"}, 400


class ChecklistDetails (MethodView): #rota = /modificarChecklist/<id>

    def get (self, id):

        checklist = Checklist.query.get_or_404(id)

        return checklist.json()

    def put (self, id):

        body = request.json
        checklist = Checklist.query.get_or_404(id)

        id = body.get("id")
        email = body.get("email")
        senha = body.get("senha")
        agendamento = body.get("agendamento")
        cadastro = body.get("cadastro")
        checkin = body.get("checkin")
        triagem = body.get("triagem")
        consulta = body.get("consulta")
        checkout = body.get("checkout")
        limpeza = body.get("limpeza")

        if isinstance(email, str) and\
            isinstance(senha, str) and\
                isinstance(agendamento, str) and\
                    isinstance(cadastro, str) and\
                        isinstance(checkin, str) and\
                            isinstance(triagem, str) and\
                                isinstance(consulta, str) and\
                                    isinstance(checkout, str) and\
                                        isinstance(limpeza, str):

            checklist.email = email
            checklist.senha = senha
            checklist.agendamento = agendamento
            checklist.cadastro = cadastro
            checklist.checkin = checkin
            checklist.triagem = triagem
            checklist.consulta = consulta
            checklist.checkout = checkout
            checklist.limpeza = limpeza

            checklist.update()

            return checklist.json(), 200
        else:
            return {"code_status": "dados inválidos"}, 400
    
    def patch (self, id):

        body = request.json
        checklist = Checklist.query.get_or_404(id)

        id = body.get("id")
        email = body.get("email", checklist.email)
        senha = body.get("senha", checklist.senha)
        agendamento = body.get("agendamento", checklist.agendamento)
        cadastro = body.get("cadastro", checklist.cadastro)
        checkin = body.get("checkin", checklist.checkin)
        triagem = body.get("triagem", checklist.triagem)
        consulta = body.get("consulta", checklist.consulta)
        checkout = body.get("checkout", checklist.checkout)
        limpeza = body.get("limpeza", checklist.limpeza)

        # Como, com o PATCH somente alguns atributos sao recebidos, foi utilizado o or para verificar os isinstance

        if isinstance(email, str) and\
            isinstance(senha, str) and\
                isinstance(agendamento, str) and\
                    isinstance(cadastro, str) and\
                        isinstance(checkin, str) and\
                            isinstance(triagem, str) and\
                                isinstance(consulta, str) and\
                                    isinstance(checkout, str) and\
                                        isinstance(limpeza, str):

            checklist.email = email
            checklist.senha = senha
            checklist.agendamento = agendamento
            checklist.cadastro = cadastro
            checklist.checkin = checkin
            checklist.triagem = triagem
            checklist.consulta = consulta
            checklist.checkout = checkout
            checklist.limpeza = limpeza

            checklist.update()

            return checklist.json(), 200
    
    def delete (self, id):

        checklist = Checklist.query.get_or_404(id)
        checklist.delete(checklist)

        return checklist.json()