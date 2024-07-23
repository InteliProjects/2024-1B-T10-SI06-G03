# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="./assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# Processamento de Linguagem Natural

## Thunder

## Integrantes: 
- <a href="https://www.linkedin.com/in/daniel-a-mendez-571217251/">Daniel Mendez</a>
- <a href="https://www.linkedin.com/in/freddy-mester-harari-375860279/">Freddy Harari</a>
- <a href="https://www.linkedin.com/in/izadoraluz-rsn/">Izadora Luz </a>
- <a href="https://www.linkedin.com/in/kaylanevasconcelos/">Kaylane Vasconcelos</a> 
- <a href="https://www.linkedin.com/in/marcelo-sitton-878248271/">Marcelo Sitton</a>
- <a href="https://www.linkedin.com/in/rafaella-bianca-cavalcante/">Rafaella Cavalcante</a> 
- <a href="https://www.linkedin.com/in/thiago-goulart-de-oliveira/">Thiago Goulart</a> 


## Professores:
### Orientador 
- Renato Penha

### Instrutores
- Ana Cristina
- Fabiana Martins de Oliveira
- Pedro Teberga
- Ricardo José Missori
- Victor Hayashi

# 📝 Descrição


O projeto de análise de sentimentos, desenvolvido pelo grupo Thunder para a Uber, visa mensurar os sentimentos dos clientes através de uma aplicação de processamento de linguagem natural. Uma vez que a Uber enfrenta o desafio de ocorrências às reclamações dos clientes. Com este projeto, a a empresa pretende identificar oportunidades de melhoria em seus produtos e serviços antes que problemas se tornem crises. O sistema processará sentimentos contidos nas avaliações e comentários dos clientes. Sentimentos positivos ajudam a identificar tendências como qualidade do serviço, preço e comodidade, resultando em envios automáticos no Slack para a equipe. Para sentimentos negativos, o sistema avaliará a gravidade, o risco de perda de clientes, riscos de imagem e necessidades de melhorias, gerando alertas no Slack para ações rápidas. O modelo de análise de sentimentos será treinado com uma base de dados rotulada contendo registros de textos e sentimentos. A criação de um MVP fornecerá funcionalidades básicas, incluindo descrição de usuários, processos de negócios, regras de negócio e casos de testes. O principal benefício para a Uber será a capacidade de antecipar problemas e melhorar a satisfação do cliente, através de uma compreensão mais profunda dos feedbacks recebidos. A implementação de um sistema automatizado para monitorar e responder aos sentimentos dos clientes permitirá à Uber agir proativamente, mitigando crises e aprimorando continuamente seus serviços. Em resumo, o projeto transformará a maneira como a Uber entende e responde aos sentimentos dos clientes, estabelecendo uma nova norma de eficiência no setor móvel.

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




# 📝 Link de demonstração

Link de demonstração: https://drive.google.com/file/d/1qL2gWc6u0AFz142zCqTETCrG-Jvr3lRs/view?usp=drivesdk

# 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **assets**: Contém elementos não-estruturados do repositório, como imagens e outros recursos visuais.

- **docs**: Contém toda a documentação do projeto na arquivo `documentacao.md`.

- **src**: Abriga todo o código fonte desenvolvido para o projeto. Dentro desta pasta, destaca-se a pasta `Notebook`, que inclui subpastas organizadas por sprint para versionamento do código:
  - **Api_Sprint_4**: Contém o código desenvolvido na quarta sprint do projeto. Esta pasta está organizada em:
    - `app`: Scripts e módulos relacionados à aplicação.
    - `data`: Conjuntos de dados utilizados no desenvolvimento e teste.
    - `models`: Modelos treinados e arquivos relacionados.
  - **BoW_Sprint_2**: Contém o trabalho realizado na segunda sprint do projeto, focado em técnicas de Bag-of-Words (BoW). Inclui:
    - `assets`: Recursos visuais e diagramas explicativos.
    - Notebooks e scripts específicos da sprint.
  - **Model_Sprint_5**: Contém o código desenvolvido na quinta sprint do projeto. Esta pasta está organizada em:
    - `app`: Scripts e módulos relacionados à aplicação.
    - `data`: Conjuntos de dados utilizados no desenvolvimento e teste.
    - `models`: Modelos treinados e arquivos relacionados.
  - **Word2Vec_Sprint_3**: Contém o trabalho realizado na terceira sprint do projeto, focado em técnicas de Word2Vec. Inclui:
    - `data`: Conjuntos de dados utilizados no desenvolvimento e teste.
    - `models`: Modelos treinados e arquivos relacionados.
    - Notebooks e scripts específicos da sprint.

- **README.md**: Arquivo que serve como guia introdutório e explicação geral sobre o projeto e a aplicação.

# 💻 Configuração para desenvolvimento e execução do código


&emsp;Este projeto tem como objetivo realizar a análise de dados relacionados à Uber utilizando técnicas de processamento de linguagem natural (PLN) e aprendizagem de máquina, rodando uma aplicação em Flask e utilizando a biblioteca Gradio do Python para uma visualização mais clara da interface. Para executar o projeto corretamente, siga as instruções detalhadas abaixo.

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


# 🌐 Tecnologias Utilizadas

&emsp;Este projeto utiliza uma variedade de tecnologias para realizar o processamento de linguagem natural e desenvolver uma *API* funcional, juntamente com uma interface. Abaixo estão listadas as principais tecnologias empregadas:

1. **Python**: Linguagem de programação principal utilizada para desenvolvimento de scripts de processamento de dados e modelos de machine learning. Aqui, utilizou-se de blicliotecas como *Pandas, Numpy, NLTK, entre outras*.

2. **Jupyter Notebook**: Ferramenta interativa usada para o desenvolvimento e execução de código Python, especialmente para análise de dados e construção de modelos.

3. **Flask**: Micro framework web em Python, utilizado para desenvolver a API.

4. **Gradio**: Biblioteca Python usada para criar interfaces de usuário interativas para modelos de *machine learning*.

6. **Slack**: Integração com a plataforma *Slack* para notificações e interação com a aplicação.

7. **TensorFlow e Keras**: Bibliotecas de *deep learning* usadas para construir e treinar redes neurais.

8. **FastText**: Biblioteca para aprendizagem de representações de palavras e frases eficientes, utilizada para capturar variações morfológicas no texto.

9. **XGBoost**: Biblioteca de otimização de gradiente de árvore de decisão, utilizada para melhorar a performance dos modelos de machine learning.
  
10. **GitHub**: Plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git, gerando um fluxo de trabalho baseado em pull requests e revisão de código.
    
11. **Visual Studio Code**: É um editor de código-fonte que inclui suporte para depuração, controle de versionamento Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código.

# 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-1B-T10-SI06-G03">THUNDER</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.inteli.edu.br/">Inteli, <a href="https://github.com/danielmendez07">Daniel Mendez</a>, <a href="https://github.com/Freddyharari">Freddy Harari</a>, <a href="https://github.com/izadoraluz">Izadora Luz </a>, <a href="https://github.com/KayVasconcelos">Kaylane Vasconcelos</a>, <a href="https://github.com/marcelositton">Marcelo Sitton</a>, <a href="https://github.com/RafaellaCavalcante">Rafaella Cavalcante</a>, <a href="https://github.com/thigoulart">Thiago Goulart</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


# 🎓 Referências

[1] PRUITT, John; ADLIN, Tamara. The Persona Lifecycle: Keeping People in Mind Throughout Product Design. San Francisco: Morgan Kaufmann Publishers, 2006.

[2] COOPER, Alan; REIMANN, Robert; CRONIN, David. About Face 3: The Essentials of Interaction Design. Indianapolis: Wiley Publishing, 2007.

[3] Cohn, M., Ford, D. Agile Software Development: The Business of Innovation. 2003.

[4] Chan Kim, W., & Mauborgne, R. (2019). A estratégia do oceano azul: Como criar novos mercados e tornar a concorrência irrelevante (A. Celso da Cunha Serra, Trad.; 2a ed.). Editora Sextante.

[5] BROWNLEE, J. How Much Training Data is Required for Machine Learning? Machine Learning Mastery. Disponível em: https://machinelearningmastery.com/much-training-data-required-machine-learning/. Acesso em: 26 abr. 2024.

[6] Napoleão, B. M. (2019, 29 de junho). Matriz de Riscos (Matriz de Probabilidade e Impacto). Ferramentas de Qualidade. https://ferramentasdaqualidade.org/matriz-de-riscos-matriz-de-probabilidade-e-impacto/. Acesso em: 15 fev. 2024.

[7] Salário de um Software Engineer na Uber. Disponível em: https://www.glassdoor.com.br/Sal%C3%A1rio/Uber-Software-Engineer-Sal%C3%A1rios-E575263_D_KO5,22.htm. Acesso em: 22 abril. 2024.

[8] Quanto cobrar pelo trabalho freelancer. Disponível em: https://www.remessaonline.com.br/blog/trabalho-freelancer-quanto-cobrar/. Acesso em: 22 abril. 2024.

[9] Preços Bid-Ask - Compra/Venda. Disponível em: https://br.investing.com/education/terms/pre%C3%A7os-bid-ask---compra-venda-200430351. Acesso em: 22 abril. 2024.

[10] Salário de um Compliance Specialist na Uber. Disponível em: https://www.glassdoor.com.br/Sal%C3%A1rio/Uber-Compliance-Specialist-Sal%C3%A1rios-E575263_D_KO5,26.htm. Acesso em: 22 abril. 2024.

[11] Como fazer o cálculo do custo do funcionário. Disponível em: https://blog.solides.com.br/como-fazer-o-calculo-do-custo-do-funcionario/#:~:text=Somando%20tudo%2C%20um%20funcion%C3%A1rio%20pode,32%25%20do%20custo%20do%20funcion%C3%A1rio. Acesso em: 22 abril. 2024.

[12] Índice de retenção de clientes. Disponível em: https://www.zendesk.com.br/blog/indice-retencao-clientes/. Acesso em: 25 abril. 2024.

[13] FARD, A. Value Proposition Canvas: The Whats, Whys & Hows. Disponível em: <https://medium.com/@adam.fard/value-proposition-canvas-the-whats-whys-hows-51eb539eb6ab>. Acesso em: 24 abr. 2024.

[14] SOLBERG, S.; LEE, J.; SILVA, C. Text Data Management and Analysis: A Practical Introduction to Information Retrieval and Text Mining. 2021.

[15] KELLEHER, J.D.; TIERNEY, B. Data Science. 2018.

[16] AssemblyAI. "How to implement Naive Bayes from scratch with Python." YouTube, publicado por AssemblyAI. Acesso em: 05 maio 2024. Disponível em: https://www.youtube.com/watch?v=TLnuAorxqE

[17] Ciência dos Dados. "COMO FAZER ANÁLISE DE SENTIMENTOS COM DADOS TEXTUAIS." YouTube, publicado por Ciência dos Dados. Acesso em: 06 maio 2024. Disponível em: https://www.youtube.com/watch?v=Wq-n7ZPce8k

[18] Google Cloud Tech. "Getting started with Natural Language Processing: Bag of words." YouTube, publicado por Google Cloud Tech. Acesso em: 07 maio 2024. Disponível em: https://www.youtube.com/watch?v=UFtxy0KRvVI

[19] Google Cloud LATAM. "Processamento de linguagem natural (PLN) | Decodificando a Nuvem | PT-BR." YouTube, publicado por Google Cloud LATAM. Acesso em: 08 maio 2024. Disponível em: https://www.youtube.com/watch?v=Dt2DRQN6uwg

[20] Mendes, Eduardo. "spaCy: Introdução a Processamento de Linguagem Natural | Live de Python #226." YouTube, publicado por Eduardo Mendes. Acesso em: 09 maio 2024. Disponível em: https://www.youtube.com/watch?v=Vr9QXpELdrs

[21] ProgrammingKnowledge. "Introduction To Natural Language Toolkit (NLTK) | NLTK Tutorial in Python." YouTube, publicado por ProgrammingKnowledge. Acesso em: 10 maio 2024. Disponível em: https://www.youtube.com/watch?v=WYgeOKZBhe0

[22] "PLN Avançado com SpaCy: Capítulo 1: Selecionando palavras, frases, nomes e alguns conceitos." Acesso em: 29 abril 2024. Disponível em: https://course.spacy.io/pt/chapter1

[23] "Dive into Deep Learning: 15.1. Análise de Sentimentos e o Dataset." Acesso em: 30 abril 2024. Disponível em: https://pt.d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-and-dataset.html

[24] "Medium: A Simple Explanation of the Bag-of-Words Model." Acesso em: 01 maio 2024. Disponível em: https://towardsdatascience.com/a-simple-explanation-of-the-bag-of-words-model-b88fc4f4971

[25] "FreeCodeCamp: An introduction to Bag of Words and how to code it in Python for NLP." Acesso em: 02 maio 2024. Disponível em: https://www.freecodecamp.org/news/an-introduction-to-bag-of-words-and-how-to-code-it-in-python-for-nlp-282e87a9da04

[26] "GitHub Docs: Licenciar um repositório." Acesso em: 03 maio 2024. Disponível em: https://docs.github.com/pt/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#disclaimer

[27] "NLTK Documentation: Sample usage for portuguese_en." Acesso em: 04 maio 2024. Disponível em: https://www.nltk.org/howto/portuguese_en.html

[28] "Medium: A Hitchhiker’s Guide to Sentiment Analysis using Naive-Bayes Classifier." Acesso em: 05 maio 2024. Disponível em: https://towardsdatascience.com/a-hitchhikers-guide-to-sentiment-analysis-using-naive-bayes-classifier-b921c0fb694

[29] "geeksforgeeks: Programming Paradigms in Python." Acesso em: 06 maio 2024. Disponível em: https://www.geeksforgeeks.org/programming-paradigms-in-python/

[30] "geeksforgeeks: Python Data Structures." Acesso em: 07 maio 2024. Disponível em: https://www.geeksforgeeks.org/python-data-structures/

[31] ChatGPT 3.5. OpenAI, utilizado em várias interações e consultas durante o desenvolvimento do projeto. 

[32] ChatGPT 4. OpenAI, utilizado em várias interações e consultas durante o desenvolvimento do projeto. 

[33] Métricas de Avaliação: Acesso em: 19 de Maio de 2024. Disponível em: https://vitorborbarodrigues.medium.com/m%C3%A9tricas-de-avalia%C3%A7%C3%A3o-acur%C3%A1cia-precis%C3%A3o-recall-quais-as-diferen%C3%A7as-c8f05e0a513c

[34] Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32. Acesso em: 21 de Maio de 2024. Disponível em: https://link.springer.com/article/10.1023/A:1010933404324.

[35] Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine Learning, 20(3), 273-297. Acesso em: 21 de Maio de 2024. Disponível em: https://link.springer.com/article/10.1007/BF00994018.

[36] Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794. Acesso em: 21 de Maio de 2024. Disponível em: https://dl.acm.org/doi/10.1145/2939672.2939785.

[37] Google Cloud Tech. "Getting started with keras". Acesso em 19 de maio de 2024. https://www.youtube.com/watch?v=J6Ok8p463C4

[38] Código Fonte TV. "Tensor flower". Acesso em: 22 de maio de 2024. Disponível em: https://www.youtube.com/watch?v=2eYLt1NA4Ss

[39] Understanding Word Vectors. Acessado em: 23 de maio de 2024. Disponível em: https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469

[40] Codebasics. "Whats is word 2 vec". Acessado em 17 de maio de 2024. Diwponível em: https://www.youtube.com/watch?v=hQwFeIupNP0

[41] Entenda como funciona o Random Foresr. Acessado em : 20 de maio de 2024. Disponível em: https://didatica.tech/o-que-e-e-como-funciona-o-algoritmo-randomforest/

[42] Word2Vec: interpretação da linguagem humana com Word embedding. Acessado em 21 de maio de 2024. Disponível em: https://www.alura.com.br/conteudo/introducao-word-embedding

[43] SVM. Acessado em 22 de maio de 2024. Disponível em: 
https://www.inf.ufpr.br/dagoncalves/IA07.pdf

[44] slackapi/bolt-python. Disponível em: <https://github.com/slackapi/bolt-python>. Acesso em: 7 jun. 2024.

[45] TF-IDF. Acessado em 07 de junho de 2024. Disponível em: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=b3bf6373ff41a115197cb5b30e57830c16130c2c

[46]GloVe. Acessado em 07 de junho de 2024. Disponível em: https://nlp.stanford.edu/pubs/glove.pdf

[47]FastText. Acessado em 07 de junho de 2024. Disponível em: https://aclanthology.org/E17-2068.pdf

[48]N-Grams. Acessado em 07 de junho de 2024. Disponível em: https://ieeexplore.ieee.org/abstract/document/6786458

[49] Part-Of-Speech Tagging. Acessado em 07 de junho de 2024. Disponível em: https://arxiv.org/pdf/cmp-lg/941001
