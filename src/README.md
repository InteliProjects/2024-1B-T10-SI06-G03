# 💻 Configuração para desenvolvimento e execução do código

&emsp;Este projeto tem como objetivo realizar a análise de dados relacionados à Uber utilizando técnicas de processamento de linguagem natural (PLN) e aprendizagem de máquina, rodando uma aplicação em Flask e utilizando a biblioteca Gradio do Python para uma visualização mais clara da interface. Para executar o projeto corretamente, siga as instruções detalhadas abaixo.

&emsp;*Vale citar que a versão final entregue como MVP está localizada na pasta Model_Sprint_5*

## 1. Clonar o Repositório

&emsp;Primeiro, é necessário clonar o repositório do projeto para o seu computador local. Abra um terminal e execute o seguinte comando:

```bash
git clone https://github.com/Inteli-College/2024-1B-T10-SI06-G03.git
cd 2024-1B-T10-SI06-G03
```

## 2. Preparar o Ambiente e Baixar os Datasets

1. **Baixar os Datasets**: Para rodar o notebook corretamente, você precisa baixar os datasets disponíveis no link a seguir: [Datasets](https://drive.google.com/drive/folders/1bm6iQenyZ63gbw_s7j0md8UaHP84O0Vn?usp=sharing). Os datasets necessários são:

    - **cc.en.300.bin**: [Download](https://drive.google.com/file/d/1eM6TfyZIUt6YlCOus5C8nCU1UkmqRu2V/view?usp=sharing) - Este é um arquivo binário contendo palavras pré-treinadas para o FastText, uma biblioteca de vetorização de texto.
    - **tweets_uber.csv**: [Baixar Arquivo](https://drive.google.com/file/d/1cot0O9YoNDQa6bPpVgboRhMIOOsoh2rI/view?usp=sharing) - Este arquivo contém uma coleção de tweets relacionados à Uber. Note que este dataset foi modificado para fins de análise e não é o original fornecido pela Uber.

2. **Salvar os Datasets**: Após baixar os arquivos, você deve colocá-los na pasta `data`, que está localizada em `src/Notebook/Model_Sprint5/data`. Para encontrar essa pasta, navegue pela estrutura de pastas do projeto até `src/Notebook/Model_Sprint5/data` e mova os arquivos baixados para lá.

## 3. Preparar o Ambiente de Desenvolvimento

1. **Instalar Dependências Necessárias para Rodar o Notebook**: O projeto usa várias bibliotecas Python, listadas no arquivo `requirements.txt`. Para instalar todas elas de uma vez, abra um terminal, navegue até a pasta do projeto e execute o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

    Este comando instalará todas as bibliotecas necessárias para rodar o notebook.


    Alternativamente, você pode rodar a célula de "Instalação e Importação das Bibliotecas" no notebook para instalar as bibliotecas necessárias quando for rodar tudo.

2. **Instalar Dependências Necessárias para Rodar a Aplicação**: Além das bibliotecas do notebook, a aplicação web requer algumas bibliotecas adicionais. Para instalá-las, execute o seguinte comando no terminal:
    ```bash
    pip install gradio requests pandas matplotlib numpy flask flasgger slack_bolt sqlalchemy
    ```
    Este comando instalará as bibliotecas necessárias para rodar a interface Gradio e o servidor Flask.

## 4. Executar o Notebook

1. **Abrir o Jupyter Notebook**: Para abrir o notebook, navegue até a pasta `src/Notebook/Model_Sprint_5/` e abra o arquivo `Model.ipynb`. 

2. **Executar o Notebook**: Dentro do Jupyter Notebook, execute todas as células clicando em `Executar tudo` ou `Run All` no menu. Este processo executará todo o código passo a passo. No final, este arquivo deve gerar dois arquivos na pasta ***models: xgboost_negative_vs_rest.pkl e xgboost_positive_vs_neutral.pkl***. Além disso, deve gerar mais três arquivos na pasta ***data: cc.en.300.vec, tweets_uber_vectorized.csv e tweets_uber.csv***. Esses arquivos são necessários para as etapas seguintes.

## 5. Executar a Interface Gradio

1. **Abrir um Terminal**: Abra um terminal e navegue até a pasta onde o script `gradio_inteface.py` está localizado:
    ```bash
    cd 2024-1B-T10-SI06-G03/src/Notebook/Model_Sprint_5/app
    ```

2. **Executar o Script**: Execute o script `gradio_inteface.py` digitando o seguinte comando no terminal:
    ```bash
    python gradio_inteface.py
    ```
    Isso iniciará a aplicação localmente em `http://127.0.0.1:7860/`. Abra um navegador e vá até esse endereço para ver a interface Gradio do projeto.

## 6. Executar o Servidor Flask

1. **Abrir Outro Terminal**: Abra outro terminal (ou uma nova aba no terminal atual) e navegue até a mesma pasta onde o script `run.py` está localizado:
    ```bash
    cd 2024-1B-T10-SI06-G03/src/Notebook/Model_Sprint_5/app
    ```

2. **Executar o Script**: Execute o script `run.py` digitando o seguinte comando no terminal:
    ```bash
    python run.py
    ```

&emsp;Após executar os passos acima, ao clicar no link `http://127.0.0.1:7860/` no navegador, você deve ver a aplicação do projeto em funcionamento.


# 📝 Etapas de Divisão do Projeto

Para que o projeto se torne viável, foi estipulado um prazo de 10 semanas, distribuído em 5 Sprints, onde cada sprint tem a duração de 15 dias. Além disso, o grupo *Thunder* utilizou a metodologia ágil *Scrum* para estipular a divisão de tarefas e conseguir realizar os entregáveis de cada sprint. 

Para ver em detalhes *como* e *o que* foi elaborado em cada sprint, basta acessar nossa pasta `docs` e procurar por `documentacao.md`. Logo abaixo, em "Histórico de lançamentos" podemos ver em tópicos os entregáveis de cada sprint. 

**OBS:**
 - A entrega final do *MVP* do código está dentro pasta `Model_Sprint_5` dentro da pasta `Notebook` em `src`. 

## 🗃 Histórico de lançamentos

* 0.1.0 - 27/04/2024
    - Entendimento do Negócio
        - Matriz de avaliação de valor Oceano Azul
        - Matriz de Risco       
        - Canvas Proposta de Valor
        - Análise financeira do projeto
        - Regras de negócio 
    - Entendimento do Usuário    
        - User Stories
        - Personas
* 0.2.0 - 11/05/2024
    - Modelo de Bag of Words - arquivo IPYNB
        - Análise Descritiva
        - Pré-processamento
        - Método Bag of Words
    - Documentação do Modelo de Bag of Words - Markdown
        - Análise Descritiva
        - Pré-processamento
        - Método Bag of Words
* 0.3.0 - 26/05/2024
    - Modelo Word 2 Vec - arquivo IPYNB
        - Introdução e Carregamento de Vetorização Pré-treinada
        - Desenvolvimento e Análise do modelo Word 2 Vec
        -   Treinamento com Modelos de Classificação - Naive Bayes, Random Forest, SVM, XGBoost
    - Documentação do Modelo Word 2 Vec - Markdown
        - Metodologia e Vetores de Palavras Pré-treinadas
        - Análise e Resultados dos Modelos
        - Comparação de Performance dos Modelos
* 0.4.0 - 09/06/2024
    - Encapsulamento dos Procedimentos Desenvolvidos em uma API Local (Flask)
        - Organização do Notebook em Instalação, Definição de Funções e Rotas da API   
        - Suporte à Vetorização BoW e Word2Vec
        - Classificação de Sentimento usando Naive Bayes e XGBoost
        - Exportação dos Modelos usando Pickle
        - Rota para Classificação de Sentimento usando a Melhor Combinação de Modelo e Vetorização
    - Aprimoramento do Modelo com Diversas Vetorizations 
    - Integração com Slack
    - Criação de Wireframe
    - Documentação - Markdown
        - Análise e Documentação dos Resultados
        - Documentação da API e Aprimoramento do Modelo
* 0.5.0 - 21/06/2024
    - Revisão e atualizações Gerais
    - Arquitetura da solução (Diagrama de Implantação UML)
    - Modelo, API e Slack
        - Adaptação de funcções para melhoramento do modelo
    - Frontend, Backend e Integração
        - Criação da tela de frontend
        - Criação uma Rota para receber Input de frase e retornar sentimento
        - Criação de Banco de Dados para guardar o input e a análise
        - Integrar a API do Flask, Frontend e Banco de Dados
        - Documentação do Fronendt, Backend Banco de dados


