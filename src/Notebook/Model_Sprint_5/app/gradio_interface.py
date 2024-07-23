# Esse código está devidamente documentado na seção 11 da documentação do projeto. 
# Você pode acessa-lo nesse link: https://github.com/Inteli-College/2024-1B-T10-SI06-G03/blob/main/docs/documentacao.md#11-deploy

import gradio as gr
import requests
import sqlite3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# OBS: Referência -> O detalhamento da implementação da Interface Gradio e a justificativa da sua utilizaçãoo está documentado na secção "11. Deploy", em "11.2 Justificativa para o Uso do Gradio" na pasta "docs" em "documentacao.md"

# Configurar o backend do Matplotlib para 'Agg' no início do script
matplotlib.use('Agg')

# Caminho para o arquivo do banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'instance/comments.db')

# Função para enviar o texto para o endpoint Flask e obter a predição
def analyze_sentiment(text):
    response = requests.post("http://127.0.0.1:5000/analise_xgboost", json={"text": text})
    print(response)
    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")
        return prediction
    else:
        return "Erro ao analisar o texto"

# Função para calcular a porcentagem de sentimentos negativos
def get_negative_sentiment_percentage():
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM Comment", conn)
        conn.close()
    except Exception as e:
        return f"Error: {str(e)}"
    
    if len(df) == 0:
        return 0.0  # No data available
    
    negative_comments = df[df['sentiment'] == 'negative']
    negative_percentage = (len(negative_comments) / len(df)) * 100

    return negative_percentage

# Função para gerar o gráfico de distribuição de sentimentos
def plot_negative_sentiment_percentage():
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM Comment", conn)
        conn.close()
    except Exception as e:
        return f"Error: {str(e)}"

    if len(df) == 0:
        return "No data available"

    sentiments = df['sentiment'].value_counts(normalize=True) * 100
    colors = {'negative': 'red', 'neutral': 'gray', 'positive': 'green'}
    plt.figure(figsize=(4, 3))
    sentiments.plot(kind='bar', color=[colors.get(sentiment, 'blue') for sentiment in sentiments.index], alpha=0.7)
    plt.title('Sentiment Distribution')
    plt.ylabel('Percentage')
    plt.xlabel('Sentiment')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    img_path = 'sentiment_distribution.png'
    plt.savefig(img_path)
    plt.close()  # Fechar a figura para liberar memória
    return img_path

# Função para gerar o gráfico estilo termômetro
def plot_gauge(negative_percentage):
    fig, ax = plt.subplots(figsize=(1.2, 0.9))  # Ajustar o tamanho da figura

    # Desenhar o termômetro
    ax.barh(1, negative_percentage, color='red', height=0.1)
    ax.barh(1, 100, color='lightgray', height=0.1, left=negative_percentage)

    # Configurações adicionais do gráfico
    ax.set_xlim(0, 100 )
    ax.set_yticks([1])
    ax.set_yticklabels(['Negativity'], fontsize=2, rotation=90, va='center')
    ax.set_xlabel('Percentage', fontsize=2)

    # Diminuir o tamanho da fonte dos eixos
    ax.tick_params(axis='both', which='both', labelsize=2)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.xaxis.set_ticks_position('none') 
    ax.yaxis.set_ticks_position('none') 

    plt.tight_layout()
    plt.title('Negative Sentiment Gauge', fontsize=2)

    
    img_path = 'gauge.png'
    plt.savefig(img_path, dpi=500)
    plt.close()  # Fechar a figura para liberar memória
    return img_path

# Interface do Gradio
css = """
    .small-button {
        padding: 5px 10px !important;
        font-size: 0.8em !important;
    }
    .gradio-container {
        font-family: 'Arial', sans-serif;
    }
    #title {
        font-size: 1.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .gr-row {
        margin-bottom: 15px;
    }
    .gr-column {
        align-items: center;
        justify-content: center;
        max-width: 600px;
        margin: auto.
    }
    .gr-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 0.8em;
        cursor: pointer.
    }
    .gr-button:hover {
        background-color: #45a049.
    }
    .center-content {
        display: flex.
        flex-direction: column.
        align-items: center.
        justify-content: center.
    }
    .gr-textbox {
        width: 100%.
    }
    .gr-image {
        width: 100%.
    }
"""

with gr.Blocks(css=css) as iface:
    with gr.Column(elem_classes="center-content"):
        gr.Markdown("# Sentiment Analysis", elem_id="title")
        text_input = gr.Textbox(
            label="Enter text to analyze sentiment:", 
            placeholder="Type your text here...",
            lines=3,
            elem_classes="gr-textbox"
        )
        sentiment_output = gr.Textbox(
            label="Sentiment Prediction", 
            interactive=False, 
            placeholder="Prediction will appear here...",
            elem_classes="gr-textbox"
        )
        analyze_button = gr.Button("Analyze", elem_classes="small-button")
        analyze_button.click(analyze_sentiment, inputs=text_input, outputs=sentiment_output)
        
        negative_sentiment_output = gr.Textbox(
            label="Negative Sentiment Percentage", 
            interactive=False, 
            placeholder="Percentage will appear here...",
            elem_classes="gr-textbox"
        )
        refresh_button = gr.Button("Refresh", elem_classes="small-button")
        refresh_button.click(lambda: get_negative_sentiment_percentage(), inputs=None, outputs=negative_sentiment_output)

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## Sentiment Distribution Chart")
                sentiment_chart = gr.Image(
                    plot_negative_sentiment_percentage, 
                    label="Sentiment Chart", 
                    interactive=False,
                    elem_classes="gr-image"
                )
                chart_refresh_button = gr.Button("Refresh Chart", elem_classes="small-button")
                chart_refresh_button.click(plot_negative_sentiment_percentage, inputs=None, outputs=sentiment_chart)

            with gr.Column(scale=1):
                gr.Markdown("## Negative Sentiment Gauge")
                gauge_chart = gr.Image(
                    lambda: plot_gauge(get_negative_sentiment_percentage()), 
                    label="Gauge Chart", 
                    interactive=False,
                    elem_classes="gr-image"
                )
                gauge_refresh_button = gr.Button("Refresh Gauge", elem_classes="small-button")
                gauge_refresh_button.click(lambda: plot_gauge(get_negative_sentiment_percentage()), inputs=None, outputs=gauge_chart)

if __name__ == "__main__":
    iface.launch(share=True)
