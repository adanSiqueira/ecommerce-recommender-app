# Sistema de Recomendação para E-commerce com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?logo=scikit-learn&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Templating-orange?logo=jinja)
![HTML](https://img.shields.io/badge/HTML5-Markup-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Responsive_UI-7952B3?logo=bootstrap&logoColor=white)

Este projeto demonstra a construção de um sistema de recomendação inteligente aplicado a uma **aplicação web de e-commerce**, com foco em personalização da experiência do usuário. A solução combina **Machine Learning**, processamento de dados e desenvolvimento web para sugerir produtos com base em interações reais (visualizações e adições ao carrinho), simulando o funcionamento de uma loja online moderna.

> ⚠️ **Nota**: o foco principal deste projeto não é criar a aplicação web mais sofisticada. O objetivo é **demonstrar, de forma prática, interativa e visível, o funcionamento de um sistema de recomendação baseado em comportamento real do usuário**. A interface da loja funciona como suporte para evidenciar como o **modelo de machine learning** responde a diferentes interações e gera recomendações em tempo real.

---

## 🎯 Objetivo

Desenvolver um sistema de recomendação que indique produtos relevantes ao usuário com base em seus comportamentos de navegação, utilizando **filtragem baseada em conteúdo**, **co-ocorrência de itens** e princípios de **sistemas de recomendação colaborativos**.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia         | Descrição |
|--------------------|----------|
| **Python**         | Linguagem principal usada para desenvolvimento da lógica, processamento de dados, integração com a aplicação web e desenvolvimento do Sistema de Recomendação. |
| **Pandas / NumPy** | Manipulação de dados tabulares, vetorização, criação de matrizes e suporte ao modelo de recomendação. |
| **Scikit-learn**   | Utilizado para funções auxiliares, como vetorização de textos e cálculo de similaridade. |
| **Flask**          | Framework web leve utilizado para criar rotas, exibir páginas e conectar o backend ao frontend. |
| **HTML/CSS + Jinja2** | Criação das páginas da loja e exibição dinâmica das recomendações usando templates. |
| **Bootstrap** | Para responsividade e estilização visual dos cards e páginas do e-commerce. |

---
## Demonstração 

![Demonstration](projectDemo.gif)

---
## 🚀 Deploy na Nuvem com Google Cloud Run + Docker
Este projeto foi empacotado e implantado utilizando o Google Cloud Run, permitindo que o sistema de recomendação funcione como um serviço web escalável, sem necessidade de servidores dedicados.

🔗 Acesse a aplicação online:
https://recommendation-system-ecommerce-276412923171.europe-west1.run.app/

### ✅ Por que usar o Cloud Run?

-  Escala automaticamente de 0 para N requisições.
-  Totalmente serverless — sem precisar configurar infraestrutura.
-  Aceita deploy direto do GitHub com Docker.
-  Ideal para projetos de Machine Learning leves que precisam de uma API ou interface interativa

---

## Notebook Explicativo: Desenvolvimento do Modelo

Além da aplicação funcional, este projeto inclui um **notebook interativo** que documenta o processo completo de desenvolvimento do sistema de recomendação, com foco na abordagem baseada em conteúdo.

O notebook pode ser acessado no arquivo [`Desenvolvimento-do-Modelo.ipynb`](./Desenvolvimento-do-Modelo.ipynb) dentro do repositório.

O notebook também explora:

- Vetorização textual com TF-IDF
- Cálculo de similaridade com Cosine Similarity
- Geração de recomendações personalizadas com base no comportamento simulado
- Estratégia de avaliação qualitativa usando perfis fictícios

---

## 🧠 Abordagem de Machine Learning

O modelo de recomendação foi desenvolvido em Python com foco em **filtragem baseada em conteúdo**, com suporte para recomendações simples por **co-ocorrência**. As principais etapas foram:

### 🔹 1. Pré-processamento dos Dados
- Leitura dos dados de produtos e simulação de interações (ex: produtos visualizados ou adicionados ao carrinho).
- Padronização e enriquecimento de campos como nome, categoria e descrição.
- Transformação das interações em uma matriz de usuário × item, ou registro de logs de ações.

### 🔹 2. Vetorização de Produtos
- Aplicação de `TfidfVectorizer` nos campos textuais dos produtos (nome, categoria, descrição).
- Geração de um espaço vetorial onde cada produto é representado por uma combinação ponderada de suas palavras-chave.

### 🔹 3. Cálculo de Similaridade
- Uso de **cosine similarity** para medir a distância entre produtos no espaço vetorial.
- Para cada produto visualizado/adicionado ao carrinho, o sistema retorna os produtos mais similares (com maior similaridade).

### 🔹 4. Recomendações por Co-ocorrência
- Implementação de uma lógica simples baseada em frequência de combinação: "usuários que visualizaram/compraram isto também visualizaram...".
- Essa técnica reforça as sugestões baseadas em comportamentos agregados.

---

## 💻 Funcionalidades

- 🛒 Página de produto individual com recomendação automática de itens relacionados.
- 🧠 Recomendações personalizadas com base nas interações do usuário (visitas e carrinho).
- 🔄 Renderização dinâmica dos produtos recomendados usando **cards visuais com imagem, nome e preço**.
- 📦 Dados simulados com categorias como **esportes**, **infantil**, **nerd/geek**, **moda** e outros.

---

## 📌 Estrutura do Projeto
```
ecommerce-recommender/
│
├── app.py # Lógica principal da aplicação Flask
├── model/ # Modelos e vetorizadores de recomendação
├── data/ # Arquivos CSV com produtos e interações
├── templates/ # HTML com Jinja2 para renderização das páginas
├── static/ # CSS, imagens e recursos estáticos
└── README.md # Este arquivo
```

---

## 📈 Trabalhando nas segunites melhorias:

- Implementar **LightFM** para recomendações híbridas (colaborativo + conteúdo).
- Incorporar **descrições geradas com LLMs** para enriquecer os produtos automaticamente.
- Treinar modelos com embeddings semânticos como **Word2Vec**, **FastText** ou **SBERT**.
- Salvar histórico do usuário e gerar recomendações persistentes.
- Adicionar filtros por categoria, preço e tags nas recomendações.

---

## 🧪 Executando o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/ecommerce-recommender.git
   cd ecommerce-recommender
   ```
2. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:
   ```bash
   python app.py
