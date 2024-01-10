# Documentação do Projeto

## Conversão Monetária

Este projeto é uma aplicação web simples desenvolvida em Django para realizar a conversão monetária entre diferentes moedas. Ele consiste em uma interface de usuário para inserir as informações de moeda de origem, moeda de destino e quantia a ser convertida.

## Organização do Código

O código do projeto está organizado da seguinte forma:

- **conversao_monetaria**: Diretório principal do projeto Django.
  - **conversao**: Aplicação Django que contém os modelos, views e URLs.
    - **migrations**: Diretório contendo as migrações do banco de dados.
    - **templates**: Diretório contendo os templates HTML para renderizar as páginas.
    - **static**: Diretório contendo arquivos estáticos como CSS, JavaScript, etc.
    - **views.py**: Arquivo contendo as views da aplicação.
    - **models.py**: Arquivo contendo os modelos de dados.
    - **urls.py**: Arquivo contendo as configurações de URL da aplicação.
  - **conversao_monetaria**: Configurações principais do projeto Django.
  - **manage.py**: Script de gerenciamento do Django.

## Como Rodar a Aplicação

### Sem Docker
Navegue até o diretório do projeto:
cd conversao_monetaria

Execute as migrações do banco de dados:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

Abra um navegador e acesse:
http://127.0.0.1:8000/converter/


### Com Docker
Certifique-se de ter o Docker instalado em sua máquina.

Clone este repositório:
git clone https://github.com/seu-usuario/conversao_monetaria.git

Navegue até o diretório do projeto:
cd conversao_monetaria

Construa o contêiner Docker:
docker build -t conversao_monetaria .

Execute o contêiner:
docker run -p 8000:8000 conversao_monetaria

Abra um navegador e acesse:
http://127.0.0.1:8000/converter/

## Funcionalidades
Insira a moeda de origem, a moeda de destino e a quantia desejada para obter o valor convertido.

## Legibilidade do Código
O código foi escrito de forma a seguir as boas práticas de programação em Python e Django. 

Foram adicionados comentários onde necessário para explicar partes específicas do código.

## Segurança
Foram adotadas práticas de segurança recomendadas pelo Django para evitar vulnerabilidades conhecidas. 

Além disso, o projeto utiliza o framework Django, que é amplamente utilizado e mantido.

## Cobertura de Testes
Embora não haja uma cobertura completa de testes, foram criados testes unitários para as principais funcionalidades da aplicação. 


## Escolhas Técnicas
Django: Escolhido devido à sua robustez, facilidade de uso e recursos integrados para desenvolvimento web.

SQLite: Banco de dados leve e integrado ao Django para facilitar o desenvolvimento e testes.

HTML/CSS/JavaScript: Utilizados para criar uma interface de usuário simples e interativa.

Este é um projeto de exemplo e pode ser adaptado e expandido conforme necessário. 

Gif utilizando o programa:

![2024-01-10 11-29-08](https://github.com/GleisonAmorim/ConversorDeMoeda/assets/54336609/89a58b71-af63-400b-84ad-e7d08590b8a2)

