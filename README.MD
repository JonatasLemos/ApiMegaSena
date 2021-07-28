# Teste Python Backend
## MegaSena API

### Sobre o projeto

#### Projeto usando Django e Django REST framework para criar uma API em que o usuário faz um sorteio de dezenas e compara com o último resultado da megasena.

O usuário pode consultar os seguintes dados nos Endpoints:
- Ultimo sorteio da megasena (obtido através de web scraping) 
- Lista de jogos criados pelo usuário 
- Quantas dezenas do jogo do usuário são iguais ao do último sorteio da megasena

O usuário pode fazer as seguintes ações:
- Se cadastrar
- Login usando autenticação JWT
- Deletar sua conta
- Editar os dados da sua conta
- Fazer logout 

Todas as requisições (excetuando cadastro) só são feitas com usuário autenticado com Token JWT no formato Bearer.

### Frameworks e bibliotecas

* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [cfscrape](https://pypi.org/project/cfscrape/)
* Database: Postgres
* Para mais detalhes: Veja requirements.txt

### Execução

#### Passos para executar o projeto:
0 - Clonar repositorio
```
git clone git@bitbucket.org:JonatasLemos93/teste-python-backend.git
```
1 - Instalar requerimentos num ambiente virtual
```
pip install -r requirements.txt
```
2 - Criar SECRET_KEY http://www.miniwebtool.com/django-secret-key-generator/
```
export SECRET_KEY='<secret_key>'
```
3 - Fazer migrações para database Postgres
```
python manage.py makemigrations
python manage.py migrate
```
4 - Subir servidor de desenvolvimento
```
python manage.py runserver
```
5 - Importar o arquivo  "MegasenaAPI.postman_collection.json" deste repositório no POSTMAN, para realizar as requisições e testar os endpoints.

obs: O token gerado no login deve ser inserido manualmente no cabeçalho da requisição

### Autor: Jônatas Oliveira Lemos


