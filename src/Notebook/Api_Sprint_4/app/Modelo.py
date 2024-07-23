import re
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import xgboost as xgb

# Função para converter emojis em palavras
def convert_emojis(text):
    """
    Converte emojis em texto legível.

    Esta função utiliza a biblioteca `emoji` para transformar emojis em seus 
    respectivos códigos de texto. Por exemplo, 🙂 se tornará :slightly_smiling_face:.

    Args:
        text (str): Texto contendo emojis a serem convertidos.

    Returns:
        str: Texto com emojis convertidos em palavras.
    """
    return emoji.demojize(text)

# Função para limpar o texto
def clean_text(text):
    """
    Limpa o texto removendo URLs, tags HTML, caracteres especiais e números.

    Esta função remove URLs, tags HTML e caracteres não alfabéticos e
    corrige espaços extras para normalizar o texto.

    Args:
        text (str): Texto a ser limpo.

    Returns:
        str: Texto limpo.
    """
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'<[^>]+>', '', text)  # Remove tags HTML
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove caracteres especiais e números
    text = re.sub(r'\s+', ' ', text).strip()  # Corrige espaços extras
    return text

# Função para tokenizar o texto
def tokenize(text):
    """
    Tokeniza o texto em palavras individuais.

    Esta função converte o texto em minúsculas e o divide em tokens
    (palavras) usando o tokenizador da biblioteca `nltk`.

    Args:
        text (str): Texto a ser tokenizado.

    Returns:
        list: Lista de tokens.
    """
    tokens = word_tokenize(text.lower())  # Converte para minúsculas e tokeniza
    return tokens

# Função para remover stopwords
def remove_stopwords(tokens):
    """
    Remove stopwords dos tokens fornecidos.

    Esta função remove palavras comuns que não contribuem significativamente para 
    o significado do texto, conhecidas como stopwords.

    Args:
        tokens (list): Lista de tokens.

    Returns:
        list: Lista de tokens sem as stopwords.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Lista de palavras a serem mantidas
words_to_keep = ['uber']

# Função para corrigir a ortografia
def correct_spelling(text):
    """
    Corrige a ortografia do texto.

    Esta função utiliza a biblioteca `TextBlob` para corrigir a ortografia do 
    texto, preservando palavras específicas que devem ser mantidas sem alterações.

    Args:
        text (str): Texto a ser corrigido.

    Returns:
        str: Texto com a ortografia corrigida.
    """
    # Substituir palavras a serem mantidas por placeholders temporários
    for i, word in enumerate(words_to_keep):
        text = text.replace(word, f'PLACEHOLDER_{i}')
    
    # Corrigir o texto
    corrected_text = str(TextBlob(text).correct())
    
    # Restaurar as palavras mantidas
    for i, word in enumerate(words_to_keep):
        corrected_text = corrected_text.replace(f'PLACEHOLDER_{i}', word)
    
    return corrected_text

# Função principal de pré-processamento para uma única frase
def preprocess_text(text):
    """
    Executa o pré-processamento completo do texto.

    Esta função aplica uma série de etapas de pré-processamento no texto,
    incluindo a conversão de emojis, limpeza, correção de ortografia, tokenização
    e remoção de stopwords.

    Args:
        text (str): Texto a ser pré-processado.

    Returns:
        str: Texto pré-processado.
    """
    text = convert_emojis(text)
    text = clean_text(text)
    text = correct_spelling(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    return ' '.join(tokens)

# Função para vetorização de palavras usando Word2Vec
def prepare_word2vec_vectors(text, embedding_file):
    """
    Prepara vetores de Word2Vec para o texto fornecido.

    Esta função carrega vetores de Word2Vec pré-treinados e os utiliza para gerar 
    uma representação vetorial para o texto fornecido.

    Args:
        text (str): Texto para o qual os vetores serão gerados.
        embedding_file (str): Caminho para o arquivo de vetores Word2Vec pré-treinados.

    Returns:
        pd.DataFrame: DataFrame contendo o vetor de Word2Vec do texto.
    """
    word_vectors = KeyedVectors.load_word2vec_format(embedding_file, binary=True)
    vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
    vectorizer.fit([text])
    word_embedding = np.zeros((word_vectors.vector_size,))
    tokens = vectorizer.build_tokenizer()(text)
    word_vecs = [word_vectors[word] for word in tokens if word in word_vectors.key_to_index]
    if word_vecs:
        word_embedding = np.sum(word_vecs, axis=0)
    return pd.DataFrame([word_embedding])

# Função para prever usando modelo XGBoost
def predict_xgboost(vectorized_text, model):
    """
    Realiza previsões usando um modelo XGBoost treinado.

    Esta função converte o texto vetorizado em um formato adequado para o XGBoost
    e utiliza um modelo treinado para fazer previsões.

    Args:
        vectorized_text (np.array): Texto vetorizado para previsão.
        model (xgb.Booster): Modelo XGBoost treinado.

    Returns:
        np.array: Previsão feita pelo modelo.
    """
    vectorized_text = np.array(vectorized_text).reshape(1, -1)
    # Criar um DMatrix a partir do texto vetorizado
    feature_names = [str(i) for i in range(vectorized_text.shape[1])]
    dmatrix = xgb.DMatrix(vectorized_text, feature_names=feature_names)
    return model.predict(dmatrix)