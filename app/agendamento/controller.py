from app.agendamento.model import Agendamento
from flask import render_template, request, jsonify
from flask.views import MethodView

from flask_mail import Message
from app.extensions import mail

class AgendamentoCreate(MethodView): # rota = /registro

    def post (self):

        body = request.json

        id = body.get("id")
        nomeResponsavel = body.get("nomeResponsavel")
        nomeCrianca = body.get("nomeCrianca")
        nascimento = body.get("nascimento")
        telefone = body.get("telefone")
        email = body.get("email")
        data = body.get("data")
        horario = body.get("horario")

        if isinstance(nomeResponsavel, str) and\
            isinstance(nomeCrianca, str) and\
                isinstance(nascimento, str) and\
                    isinstance(telefone, str) and\
                        isinstance(email, str) and\
                            isinstance(data, str) and\
                                isinstance(horario, str):
            
            agendamento = Agendamento.query.filter_by(nomeCrianca = nomeCrianca).first()

            dataMarcada = Agendamento.query.filter_by(data = data).first()

            horarioMarcado = Agendamento.query.filter_by(horario = horario).first()
            
            if dataMarcada and horarioMarcado:
                return {"code_status": "Dados inválidos, horário já cadastrado"}, 400

            agendamento = Agendamento(nomeResponsavel=nomeResponsavel,
                                      nomeCrianca=nomeCrianca,
                                      telefone=telefone,
                                      email=email,
                                      data=data,
                                      horario=horario)

            agendamento.save()

            # Por conta da exposição da chave ao github mesmo dentro do .gitignore, minha conta no sendgrid foi temporariamente suspensa, logo a funcionadlidade de enviar emails pode nao estar disponivel
            
            msg = Message(sender='pedrobolzan@poli.ufrj.br', recipients=[email], subject='Agendamento Feito', html=render_template('email.html', nome=nomeResponsavel))
            mail.send(msg)

            return agendamento.json(), 200

    def get (self):

        agendamentos = Agendamento.query.all()

        return jsonify([agendamento.json() for agendamento in agendamentos]), 200

class AgendamentoDetails (MethodView): # rota = /modificar/<id>

    def get (self, id):

        agendamento = Agendamento.query.get_or_404(id)

        return agendamento.json()

    def put (self, id):

        body = request.json
        agendamento = Agendamento.query.get_or_404(id)

        id = body.get("id")
        nomeResponsavel = body.get("nomeResponsavel")
        nomeCrianca = body.get("nomeCrianca")
        nascimento = body.get("nascimento")
        telefone = body.get("telefone")
        email = body.get("email")
        data = body.get("data")
        horario = body.get("horario")

        if isinstance(nomeResponsavel, str) and\
            isinstance(nomeCrianca, str) and\
                isinstance(nascimento, str) and\
                    isinstance(telefone, str) and\
                        isinstance(email, str) and\
                            isinstance(data, str) and\
                                isinstance(horario, str):

            agendamento.nomeResponsavel = nomeResponsavel
            agendamento.nomeCrianca = nomeCrianca
            agendamento.nascimento = nascimento
            agendamento.telefone = telefone
            agendamento.email = email
            agendamento.data = data
            agendamento.horario = horario

            agendamento.update()

            return agendamento.json(), 200
        else:
            return {"code_status": "dados inválidos"}, 400
    
    def patch (self, id):

        body = request.json
        agendamento = Agendamento.query.get_or_404(id)

        id = body.get("id")
        nomeResponsavel = body.get("nomeResponsavel", agendamento.nomeResponsavel)
        nomeCrianca = body.get("nomeCrianca", agendamento.nomeCrianca)
        nascimento = body.get("nascimento", agendamento.nascimento)
        telefone = body.get("telefone", agendamento.telefone)
        email = body.get("email", agendamento.email)
        data = body.get("data", agendamento.data)
        horario = body.get("horario", agendamento.horario)

        # Como, com o PATCH somente alguns atributos sao recebidos, foi utilizado o or para verificar os isinstance
        
        if isinstance(nomeResponsavel, str) or\
            isinstance(nomeCrianca, str) or\
                isinstance(nascimento, str) or\
                    isinstance(telefone, str) or\
                        isinstance(email, str) or\
                            isinstance(data, str) or\
                                isinstance(horario, str):

            agendamento.nomeResponsavel = nomeResponsavel
            agendamento.nomeCrianca = nomeCrianca
            agendamento.nascimento = nascimento
            agendamento.telefone = telefone
            agendamento.email = email
            agendamento.data = data
            agendamento.horario = horario

            agendamento.update()

            return agendamento.json(), 200
    
    def delete (self, id):

        agendamento = Agendamento.query.get_or_404(id)
        agendamento.delete(agendamento)

        return agendamento.json()
