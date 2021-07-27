# back-end-challenge-viajar-faz-bem.
Avaliação para vaga de Backend Pleno Python


# Projeto já está no servidor rodando.

Realizado o deploy da aplicação nos servidores da Hostagador.
* Acesso da aplicação: http://162.240.3.106:37777/ ou http://162.240.3.106:37777/admin  ( Para realizar os devidos testes manuais da aplicação ).
* Usuário: thiago 
* Senha: 1234

# Informações.

Obs: todos as imagens dos links das urls estão armazenadas nos servidores, dentro de (storage) containers da Azure.
* APP desenvolvido dentro das normas da PEP8.
* Python==3.9.6
* djangorestframework==3.12.4


# Diferenciais implementados
* Deploy no servidore da Hostgator.
* Alterado banco de dados de sqlite para <i>POSTGRESQL.</i>
* Criado storage na plataforma Azure para armazenar as imagens.
* Implementando atributo "observacao":  dentro do ITEM.

# Link's úteis.
banco de dados PostreSQL v.13 Link para donwload (https://www.postgresql.org/).

# Configurando o projeto

1 Baixe o projeto:

git clone https://github.com/thiagocarvalhorodrigues/back-end-challenge-viajar-faz-bem.git


2 Após baixar o projeto, acesse a pasta do mesmo e execute os comandos abaixo:
* pip install -r requirements.txt

<i>Banco de dados Postgres.
O banco de dados consta em núvem, não sendo necessário baixar o Postgres Server,</i>
basta pular para p item 3.

2.1 Caso desejar instalar o banco localmente: 
Instalar o banco de dados Postgres Server:
* acesse acima os ==> Link's úteis < == 
* Acesse o <i>settings.py</i>  e altere os dados  em <i>'DATABASES'</i> e insira os dados do banco..

2.2 Crie um usuário e senha para logar no Django Admin: 
* python manage.py createsuperuser

3 Rode esse comando para subir o servidor:
* python manage.py runserver 8000 (Pode inserir a porta que desejar).

* Acesse no navegador a url: http://localhost:8000

* usuário: thiago 
* senha: 1234

<i>Depois tente acessar e logar no Django Admin com o usuário e senha criado acima: http://localhost:8000/admin/ </i>

# Agradecimentos
 
 Venho agradecer por esse desafio, pois foi muito bacana entar desenvolvendo, espero que tenham gostado 
 e que possamos a vir a trabalhar juntos em breve.
 MUITO OBRIGADO.





