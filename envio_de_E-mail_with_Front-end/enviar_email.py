import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def enviar_email(remetente, senha, destinatario, assunto, mensagem, arquivo=None):
    # Criação do corpo e do cabeçalho do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # corpo do e-mail
    msg.attach(MIMEText(mensagem, 'plain'))

    # Anexar arquivo
    if arquivo:
        with open(arquivo, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(arquivo)}')
        msg.attach(part)

    # Enviar o e-mail utilizando o servidor SMTP do Gmail
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Inicia a comunicação com criptografia TLS
            server.login(remetente, senha)  # Faz login no servidor SMTP
            server.send_message(msg)  # Envia o e-mail
    except Exception as e:
        raise e
    finally:
        # Remove o arquivo após o envio
        if arquivo and os.path.exists(arquivo):
            os.remove(arquivo)
