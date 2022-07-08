from app.agendamento.model import agendamento_api
from app.agendamento.controller import AgendamentoCreate, AgendamentoDetails

agendamento_api.add_url_rule("/registro", view_func= AgendamentoCreate.as_view("cria_agendamento"), methods = ["POST","GET"])
agendamento_api.add_url_rule("/modificar/<int:id>", view_func= AgendamentoDetails.as_view("modifica_agendamento"), methods = ["GET","PUT","PATCH","DELETE"])