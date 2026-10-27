# 🤖 Automação de Dados e Registo de Produtos com Python

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Solução de automação de processos de negócio (RPA) desenvolvida em Python para automatizar a leitura de dados de produtos e efetuar o respetivo registo num sistema web/desktop através da emulação de teclado e rato.

---

## 📌 Visão Geral

A introdução manual de catálogos e inventários acarreta morosidade e risco de erros de digitação. Este projeto automatiza o fluxo ponta a ponta:
1. Leitura estruturada da tabela de dados (`produtos.csv`).
2. Acesso e autenticação automática no sistema de destino.
3. Iteração linha a linha com preenchimento programático de cada campo do produto.
4. Envio de formulário e confirmação de registo em ciclo contínuo.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para estruturação do fluxo lógico.
- **Pandas**: Leitura e manipulação eficiente do ficheiro de dados tabulares.
- **PyAutoGUI**: Controlo programático de eventos de cursor de rato e digitação de teclado.
- **Time**: Gestão de intervalos e esperas ativas entre ações da interface.

---

## 📂 Estrutura do Repositório

```text
├── Projeto_Automacao_de_dados_com_python/
│   ├── auxiliar.py      # Utilitário para captura de coordenadas (X, Y) no ecrã
│   ├── codigo.py        # Fluxo principal de automação e inserção de dados
│   └── produtos.csv     # Base de dados com o catálogo de produtos a processar
├── .gitignore
├── requirements.txt     # Dependências externas do projeto
└── README.md
