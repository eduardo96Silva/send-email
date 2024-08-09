import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

def send_email(authApp, emailFrom, emailTo):
    # Corpo do email em HTML
    body_email = """
        <html>
            <head>
                <style>
                    h1 {color: blue;}
                    p {font-size: 16px;}
                </style>
            </head>
            <body>
                <h1>Email Teste</h1>
                <p>Testando envio de email</p>
            </body>
        </html>
    """

    # Criar a mensagem
    msg = MIMEMultipart()
    msg['Subject'] = "Test Send Email"
    msg['From'] = emailFrom
    msg['To'] = emailTo

    # Anexar o corpo do email com codificação UTF-8
    msg.attach(MIMEText(body_email, 'html', 'utf-8'))

    # Conectar ao servidor SMTP e enviar o email
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(emailFrom, authApp)
        s.send_message(msg)

# Carregar variáveis de ambiente
load_dotenv()
authApp = os.environ.get('AUTH_APP')
emailFrom = os.environ.get('EMAIL_FROM')
emailTo = os.environ.get('EMAIL_TO')

send_email(authApp, emailFrom, emailTo)
