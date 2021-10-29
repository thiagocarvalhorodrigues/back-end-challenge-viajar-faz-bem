#  🧑🏻‍🚀back-end-challenge-viajar-faz-bem.

# 🔥 As potenciais melhorias sugeridas foram implementadas:
* Criação da documentção  da API com  SWAGGER.
* Criação de testes unitários 
* Ajustando erro no campo ArrayField.
* Ajustado as rotas "/destinos" , "/".
* Retirado no Json o campo "Observação".
* Ajustado requirements.txt.

# 📄 Instruções da API SWAGGER:
Interno:
* Layout API SWAGGER: http://127.0.0.1:8000/docs/
* Schema API SWAGGER: http://127.0.0.1:8000/openapi/

Externo:
* http://162.240.3.106:37777/docs/
* http://162.240.3.106:37777/openapi/


# ☁️ Projeto já está no servidor rodando.
Realizado o deploy da aplicação nos servidores da Hostagador.
* Acesso da aplicação: http://162.240.3.106:37777/ ou http://162.240.3.106:37777/admin  ( Para realizar os devidos testes manuais da aplicação ).
* Usuário: thiago 
* Senha: 1234

# ℹ️  Informações.

Obs: todos as imagens dos links das urls estão armazenadas nos servidores, dentro de (storage) containers da Azure.
* APP desenvolvido dentro das normas da PEP8.
* Python==3.9.6
* djangorestframework==3.12.4

 
# 💡 Diferenciais implementados
* Deploy no servidore da Hostgator.
* Alterado banco de dados de sqlite para <i>POSTGRESQL.</i>
* Criado storage na plataforma Azure para armazenar as imagens.


# 🔗 Link's úteis.
banco de dados PostreSQL v.13 Link para donwload (https://www.postgresql.org/).

# 🚧 Configurando o projeto localmente

1 Baixe o projeto:

git clone https://github.com/thiagocarvalhorodrigues/back-end-challenge-viajar-faz-bem.git


2 Após baixar o projeto, acesse a pasta do mesmo e execute os comandos abaixo:
* pip install -r requirements.txt

<i>Banco de dados Postgres.
O banco de dados consta em núvem, não sendo necessário baixar o Postgres Server,</i>
basta pular para para o  item 3.

2.1 Caso desejar instalar o banco localmente: 
Instalar o banco de dados Postgres Server:
* acesse acima os ==> Link's úteis < == 
* Acesse o <i>settings.py</i>  e altere os dados  em <i>'DATABASES'</i> e insira os dados do banco.

2.2 Crie um usuário e senha para logar no Django Admin: 
* python manage.py createsuperuser

3 Rode esse comando para subir o servidor:
* python manage.py runserver 8000 (Pode inserir a porta que desejar).

* Acesse no navegador a url: http://localhost:8000

* usuário: thiago 
* senha: 1234

<i>Depois tente acessar e logar no Django Admin com o usuário e senha criado acima: http://localhost:8000/admin/ </i>

# ℹ️  Informações extras:

* O sistema já vem configurado com o banco de dados conforme abaixo: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "viajar_faz_bem",
        'USER': "postgres",
        'PASSWORD': "12345678",
        'HOST': "189.34.18.253",
        'PORT': "5432"

    }
 }
 
 ![image](https://user-images.githubusercontent.com/23345809/128272367-4f0c33b5-27e7-4595-ab11-6601d31bb834.png)

* Para rodar os TESTE UNITÁRIOS. 
 Digite: <i>python manage.py test</i>

# 🎉 Agradecimentos
 
 Venho agradecer por esse desafio, pois foi muito bacana entar desenvolvendo, espero que tenha gostado.

# ✈️ No aguardo!!! 🚀




