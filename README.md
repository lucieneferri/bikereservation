# Bike Reservation :bike:

O projeto consiste em uma sistema que faz reserva de bicicletas para uma aula de spinning em uma academia.
O aluno só consegue fazer uma reserva se tiver cadastrado e logado

## Dependecias 

- Python 3

## Rodando a aplicação localmente

- Crie uma virtual env [Docs](https://docs.python.org/pt-br/3/library/venv.html)
- Rode o comando `pip install -r requirements.txt`
- Rode o comando `python3 manage.py migrate` para criar o banco local (SQLite)
- Rode o comando `python3 manage.py createsuperuser` para criar o cadastro do aluno no banco
- Esolha um usuário e uma senha, eles serão usados para fazer o login na aplicação
- Para subir o projeto rode `python3 manage.py runserver` 
- Acesse `localhost:8000` para ver a aplicação rodar
- Use o usuário e senha cadastrados previamente para conseguir acessar o sistema

Projeto em construção...
