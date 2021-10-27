import dotenv
import os
from email.mime import image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

dotenv.load_dotenv(dotenv.find_dotenv())

# Poderia pegar direto da tabela os emais que não foram marcados como iniciados

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# para fazer login é preciso permitir que seu email se conecte em aplicações não seguras,
# ou gerar um token de acesso no caso dee verificação em duas etapas. https://security.google.com/settings/security/apppasswords.
server.login(email, password)

msg = MIMEMultipart('related')
# assunto do email.
msg['Subject'] = ""

# seta o corpo do e-mail baseado em um template html (obs: preferível usar table pra adicionar estilos)
with open("emailTemplate.html", "rb") as f:
    template = f.read()

body = MIMEText(template, "html", "utf-8")

# aqui ele inclue a imagem no corpo do arquivo, definindo o Content-ID(cid) conforme no template.
with open("imagem.png", 'rb') as f:
    img = MIMEImage(f.read())

img.add_header("Content-ID", "<imagem>")

msg.attach(body)
msg.attach(img)

try:
    server.sendmail(
        os.getenv("EMAIL"),
        [],  # lista de contatos de email.
        msg.as_string()
    )

    print("Email Enviado!")

except:
    print("Erro ao enviar email!")


server.close()
