# Project Medallion Architecture

Uma implementação da **Medallion Architecture** para organizar e transformar dados em um fluxo de camadas (Bronze → Silver → Gold).  
Este projeto demonstra como estruturar um pipeline de dados incremental com foco em qualidade, organização e reutilização.

---

## 🧠 Visão Geral

**Medallion Architecture** é um padrão de arquitetura de dados que organiza dados de forma progressiva através de camadas, com o objetivo de melhorar a qualidade e facilitar análises e integrações. Cada camada tem um propósito definido:

- 🟫 **Bronze (Raw)** — Dados brutos ingeridos sem transformações.
- ⚪ **Silver (Validated)** — Dados validados e estruturados.
- 🟨 **Gold (Enriched / Curated)** — Dados otimizados para consumo analítico ou relatórios.

Este projeto implementa essas camadas com scripts Python para ingestão, transformação e normalização dos dados, criando um pipeline simples e fácil de entender.

---

## 🗂 Estrutura do Projeto

```
📦 project_medallion_architecture
├── 01-bronze-raw/              # Camada Bronze (dados brutos)
├── 02-silver-validated/        # Camada Silver (dados tratados)
├── app.py # Arquivo principal de execução
├── db.py # Configuração de conexão / DB
├── get_data.py # Scripts para ingestão de dados
├── normalize_data.py # Transformações de dados
└── .gitignore
```

---

## 🚀 Como Rodar o Projeto

Siga estes passos para executar o pipeline localmente:

### 1. Clone o repositório
```bash
git clone https://github.com/mariagrasi/project_medallion_architecture.git
cd project_medallion_architecture
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
### 3. Instale dependências
```bash
pip install -r requirements.txt
```
### 4. Execute o pipeline
```bash
python app.py
```
## 📌 Pré-requisitos

Antes de executar o projeto você precisa:

- Python 3.8+
- Dependências listadas em requirements.txt

## 📈 Resultado Esperado

Ao executar o pipeline:

- Os dados brutos são carregados na camada Bronze.
- Dados passam por validações e transformações para a camada Silver.
- Versões finalizadas e otimizadas para análise são colocadas na camada Gold.

## 💡 Tecnologias Utilizadas

- Python
- Bibliotecas de manipulação de dados (ex: pandas)
- Integração API ViaCEP
- Integração com a base de dados PostgreSQL

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql&logoColor=white)
![Architecture](https://img.shields.io/badge/Data%20Architecture-Medallion-orange)
