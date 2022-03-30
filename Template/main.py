from email.mime.nonmultipart import MIMENonMultipart
from mimetypes import MimeTypes
from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart # Permite que coloque quem envia msg, para quem, etc...
from email.mime.text import MIMEText # Recebe o corpo do email.
from email.mime.image import MIMEImage # Recebe imagem para anexar no email. 
import smtplib # É o que envia a mensagem em si.

meu_email = "wekisleysouzapro@gmail.com"
senha = "naosei"

email_receptor = "wekisleysouza015@gmail.com"

with open('Template/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().date().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Wekisley', data=data_atual)

msg = MIMEMultipart()
msg['from'] = "Wekisley Souza"
msg['to'] = email_receptor
msg['subject'] = 'Teste do programa que envia emails.'

corpo = MIMEText(corpo_msg, 'html') # Se fosse texto simples, bastava colocar o texto entre os parenteses.

msg.attach(corpo) # Enviar corpo para msg.

with open('Template/img/rato.jpg', 'rb') as img:
    img = MIMEImage(img.read()) # Ler imagem.
    #msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # Mensagem de hellow pro servidor.
    smtp.starttls() # Um tipo de inicio com conexão específica. Gmail aceita tls.

    try:
        smtp.login(meu_email, senha) # Faz o login.
    except smtplib.SMTPAuthenticationError as error:
        print("Senha ou email incorretos!")

    smtp.send_message(msg) # Envia mensagem.
    print("E-mail enviado com sucesso!")