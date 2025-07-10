# 🛒 Sistema de Recomendação para E-commerce com Machine Learning

Este projeto demonstra a construção de um sistema de recomendação inteligente aplicado a uma **aplicação web de e-commerce**, com foco em personalização da experiência do usuário. A solução combina **Machine Learning**, processamento de dados e desenvolvimento web para sugerir produtos com base em interações reais (visualizações e adições ao carrinho), simulando o funcionamento de uma loja online moderna.

---

## 🎯 Objetivo

Desenvolver um sistema de recomendação que indique produtos relevantes ao usuário com base em seus comportamentos de navegação, utilizando **filtragem baseada em conteúdo**, **co-ocorrência de itens** e princípios de **sistemas de recomendação colaborativos**.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia         | Descrição |
|--------------------|----------|
| **Python**         | Linguagem principal usada para desenvolvimento da lógica, processamento de dados e integração com a aplicação web. |
| **Pandas / NumPy** | Manipulação de dados tabulares, vetorização, criação de matrizes e suporte ao modelo de recomendação. |
| **Scikit-learn**   | Utilizado para funções auxiliares, como vetorização de textos e cálculo de similaridade. |
| **Flask**          | Framework web leve utilizado para criar rotas, exibir páginas e conectar o backend ao frontend. |
| **HTML/CSS + Jinja2** | Criação das páginas da loja e exibição dinâmica das recomendações usando templates. |
| **Bootstrap** | Para responsividade e estilização visual dos cards e páginas do e-commerce. |

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
ecommerce-recommender/
│
├── app.py # Lógica principal da aplicação Flask
├── model/ # Modelos e vetorizadores de recomendação
├── data/ # Arquivos CSV com produtos e interações
├── templates/ # HTML com Jinja2 para renderização das páginas
├── static/ # CSS, imagens e recursos estáticos
└── README.md # Este arquivo


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
