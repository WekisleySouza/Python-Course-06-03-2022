from string import Template
from datetime import datetime
from this import d

with open('Template/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().date().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Wekisley', data=data_atual)

print(corpo_msg)