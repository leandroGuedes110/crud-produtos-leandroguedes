# API de Produtos

## Integrantes

* leandro guedes da silva

## Como executar o projeto

1. Instalar as dependências:

```bash
python -m pip install fastapi uvicorn sqlalchemy
```

2. Executar a aplicação:

```bash
python -m uvicorn main:app --reload
```

3. Acessar no navegador:

```
http://127.0.0.1:8000/docs
```

## Banco de dados

O projeto utiliza SQLite, que é um banco de dados leve que funciona através de um arquivo local (`produtos.db`), não sendo necessário instalar um servidor.

## Decisões do projeto

* Os campos do produto (nome, preço, categoria e quantidade) são obrigatórios.
* O método **PUT** atualiza todos os dados do produto.
* O método **PATCH** atualiza apenas os campos enviados.
* Quando um produto não é encontrado, a API retorna erro 404.

## Organização do projeto

O código foi dividido em arquivos separados:

* `main.py`: rotas da API
* `models.py`: estrutura do banco
* `schemas.py`: validação de dados
* `crud.py`: operações no banco
* `database.py`: conexão com o banco
