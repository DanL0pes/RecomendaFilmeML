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