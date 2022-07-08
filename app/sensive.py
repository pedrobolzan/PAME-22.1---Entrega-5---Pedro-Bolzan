from telnetlib import SE

#Por conta da exposição da chave ao github, minha conta no sendgrid foi temporariamente suspensa, logo a funcionadlidade de enviar emails pode nao estar disponivel

class Sensive:
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = "abp;ojenrioaenrujinserjkhnjiklrbnyhjkdlbnkldgvbuohbrkldbahsilujbarisulhjkabiourb"
    
    MAIL_SERVER = "smtp.sendgrid.net"
    MAIL_PORT = 587
    MAIL_USERNAME = "apikey"
    MAIL_PASSWORD = "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"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

sen = Sensive()
