from app.checklist.model import checklist_api
from app.checklist.controller import ChecklistCreate, ChecklistDetails, Login, UserSpecific

checklist_api.add_url_rule("/registroChecklist", view_func= ChecklistCreate.as_view("cria_checklist"), methods = ["POST","GET"])
checklist_api.add_url_rule("/modificarChecklist/<int:id>", view_func= ChecklistDetails.as_view("modifica_checklist"), methods = ["GET","PUT","PATCH","DELETE"])
checklist_api.add_url_rule("/login", view_func= Login.as_view("login"), methods = ["POST"])
checklist_api.add_url_rule("/user/<int:id>", view_func= UserSpecific.as_view("getdata"), methods = ["GET"])