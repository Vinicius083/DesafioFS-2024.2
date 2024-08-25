# DesafioFS-2024.2

## Índice
- [Introdução](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias-utilizadas)
- [Contato](#contato)

## Introdução
Este projeto foi criado para o desafio proposto pelo workshop da Fábrica de Software. Desenvolvido para fornecer uma maneira simples de buscar e armazenar piadas aleatórias usando a Geek-Joke-API. Ele é ideal para quem está aprendendo Django e quer entender como consumir APIs externas e criar APIs RESTful, sendo ideal para testar os conhecimentos adquiridos na primeira semana do workshop.

## Instalação
Siga as instruções abaixo para instalar o projeto localmente.

1. Clone o repositório:
```bash```
git clone https://github.com/Vinicius083/DesafioFS-2024.2

2. Acesse o diretório do projeto:
cd nome-do-projeto

3. Crie um ambiente virtual e ative-o:
python -m venv venv
.\venv\Scripts\activate  # Para Windows
source venv/bin/activate  # Para Linux/MacOS

4. Instale as dependências:
pip install -r requirements.txt

5. Execute as migrações:
python manage.py migrate

6. Inicie o servidor de desenvolvimento:
python manage.py runserver

## Uso
Para utilizar o projeto, siga os passos abaixo:

1. Acesse a aplicação em `http://127.0.0.1:8000/`.
2. Utilize as rotas disponíveis, como `/apps/piadas/procurar_piada/` para buscar uma piada aleatória.

## Funcionalidades
# Geek-Joke-Api
- Buscar piadas aleatórias usando a Geek-Joke-API. # /apps/piadas/procurar_piada/
- Salvar piadas no banco de dados. 
- Expor uma API RESTful para acessar as piadas salvas.

# Cadastro
- Realizar um cadastro simpes de pessoas. # /apps/cadastro
- Salvar os cadastros no banco de dados. 
- Expor uma API RESTful para acessar os cadastros salvos. 

## Tecnologias Utilizadas
- [Django](https://www.djangoproject.com/) - Framework Web
- [Django REST Framework](https://www.django-rest-framework.org/) - Para construção de APIs RESTful
- [Requests](https://docs.python-requests.org/en/master/) - Para fazer requisições HTTP

## Contato
Vinícius Almeida - [e-mail](jvinicius7337@gmail.com)
Link do Projeto: https://github.com/Vinicius083/DesafioFS-2024.2
