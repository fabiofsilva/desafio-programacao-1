# Desafio de programação 1
Solução para o desafio de importação de arquivo.

## Instruções de instalação
1. Antes de instalar o projeto, tenha certeza de ter instalado o git, [pyenv](https://github.com/pyenv/pyenv) e 
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
1. Baixe a versão do python 3.6.5 e crie um ambiente virtual com o nome que desejar.


    $ pyenv install 3.6.5
    
    $ pyenv virtualenv 3.6.5 nome-do-virtual-env
    
1. Clone este repositório.


    $ git clone https://github.com/fabiofsilva/desafio-programacao-1.git && cd desafio-programacao-1
       
1. Instale as dependências do projeto.


    $ pip install -r requirements.txt
    
1. Crie o arquivo .env e configure as variáveis do arquivo settings.py. Você pode dar uma olhada no arquivo de exemplo .env.example, 
que possui algumas variáveis configuradas.
1. Crie a base de dados, rodando as migrações.


    $ python manage.py migrate
    
1. Inicie o servidor.


    $ python manage.py runserver
    
1. Acesse a página de importação em http://127.0.0.1:8000/importar-arquivo-de-vendas/          


## Rodando testes

Caso queira executar os testes do projeto, instale as dependências utilizando o arquivo requirements-dev.txt.

    $ pip install -r requirements-dev.txt
    
Para executar os testes digite o comando:

    $ python manage.py test import_data