import requests # Faz a requisição/ Baixa o html
from bs4 import BeautifulSoup # Manipular o html

url = "https://stackoverflow.com/questions/tagged/python"

response = requests.get(url) # Pega os dados html.

html = BeautifulSoup(response.text, 'html.parser') # Instancía para edição.

for pergunta in html.select('.s-post-summary--content'): # Selecionando elemento html.
    titulo = pergunta.select_one('.s-link') # pegando títulos da página.
    foi_postado_tempo = pergunta.select_one('.relativetime')

    print(f'"{titulo.text}" foi perguntado a {foi_postado_tempo.text}.\n')


