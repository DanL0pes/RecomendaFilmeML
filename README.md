# Sistema de Recomendação de Filmes: Do Estudo à API

> Um projeto End-to-End de Machine Learning implementando Filtragem Colaborativa com Python.

![GitHub repo size](https://img.shields.io/github/repo-size/DanL0pes/RecomendaFilmeML?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/DanL0pes/RecomendaFilmeML?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/DanL0pes/RecomendaFilmeML?style=for-the-badge)

---

## Tecnologias Utilizadas

### Linguagem & Análise de Dados
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

### Machine Learning
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

### API & Backend
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/uvicorn-%2325263B.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

---

## Sobre o Projeto

Este repositório contém o ciclo completo de desenvolvimento de um sistema de recomendação de filmes, dividido em duas etapas principais:

1.  **Análise Exploratória e Modelagem:** Um Jupyter Notebook detalhado que processa o dataset *MovieLens Small*, realiza a limpeza de dados, cria matrizes de interação usuário-filme e treina um modelo KNN (K-Nearest Neighbors).
2.  **API RESTful (Deploy):** Uma aplicação robusta usando **FastAPI** que consome o modelo treinado e expõe um endpoint para gerar recomendações em tempo real para novos usuários (resolvendo o problema de *Cold Start*).

### Funcionalidades

* **Filtragem Colaborativa:** Recomendação baseada na similaridade de gosto entre usuários (User-Based).
* **Similaridade de Cosseno:** Cálculo matemático para encontrar os vizinhos mais próximos.
* **API Robusta:** Endpoint que aceita IDs de filmes e notas, converte para o formato da matriz e retorna sugestões.
* **Métricas de Avaliação:** Implementação de Precision, Recall e F1-Score no notebook de estudo.

---

## Estrutura do Projeto

```bash
├── notebooks/
│   └── recomendar_filmes.ipynb   # Estudo, Análise e Treinamento
├── src/
│   ├── main.py                   # Código da API (FastAPI)
│   └── requirements.txt          # Dependências do projeto
├── data/
│   ├── matriz_filmes.pkl         # Modelo serializado (Matriz Pivot)
│   └── tabela_filmes.pkl         # Dicionário de IDs e Títulos
└── README.md
```

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3.9+ instalado.

1. Clone o repositório:

```Bash
git clone [https://github.com/DanL0pes/RecomendaFilmeML.git](https://github.com/DanL0pes/RecomendaFilmeML.git)
cd RecomendaFilmeML
```

2. Instale as dependências:

```Bash
pip install -r src/requirements.txt
```

### Passo 1: Gerar o Modelo (Estudo)

Abra o notebook na pasta notebooks/ e execute todas as células. Isso irá baixar o dataset, treinar o modelo e gerar os arquivos .pkl necessários na pasta raiz.

### Passo 2: Rodar a API

Execute o servidor Uvicorn apontando para o arquivo da API:

```Bash
uvicorn src.main:app --reload
```

A API estará disponível em: http://127.0.0.1:8000

---

## Documentação da API

O FastAPI gera automaticamente uma documentação interativa (Swagger UI). Acesse http://127.0.0.1:8000/docs para testar os endpoints diretamente pelo navegador.

### Exemplo de Request (JSON)
**POST**  `/recomendar_por_id`

```JSON
{
  "avaliacoes": [
    { "movie_id": 1, "rating": 5.0 },
    { "movie_id": 318, "rating": 5.0 },
    { "movie_id": 296, "rating": 4.5 }
  ]
}
```

## Próximos Passos (Roadmap)
- [ ] Implementar tratamento de Matrizes Esparsas (Sparse Matrix) para suportar o dataset MovieLens 25M.

- [ ] Criar um frontend simples em Streamlit ou React.

- [ ] Containerizar a aplicação com Docker.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um Pull Request.

---

<div align="center"> Feito com 💙 e Python </div>