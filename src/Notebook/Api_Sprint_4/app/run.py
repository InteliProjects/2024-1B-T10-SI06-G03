from flask import Flask, request, jsonify
from flasgger import Swagger
import pickle
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
import os

app = Flask(__name__)

# Configuração do Swagger
swagger = Swagger(app)

from Modelo import preprocess_text, prepare_word2vec_vectors, predict_xgboost

# Carregue o modelo pretreinado
model = pickle.load(open('../models/xgboost_model.pkl', 'rb'))

# Definir a variável de ambiente para o token do Slack
os.environ["SLACK_BOT_TOKEN"] = 'xoxp-7223665090662-7230184266179-7253141460016-5c83eadf05f7eb4a917af42aa7f999a6'

# Inicialize o aplicativo Slack
slack_app = App(token=os.getenv("SLACK_BOT_TOKEN"))
handler = SlackRequestHandler(slack_app)

def send_slack_alert(message):
    try:
        response = slack_app.client.chat_postMessage(
            channel="#sentiment_tracker_inteli",
            text=message
        )
        app.logger.info(f"Message sent to Slack channel: {response}")
    except Exception as e:
        app.logger.error(f"Error sending message to Slack: {e}")
        
@app.route('/preprocess', methods=['POST'])
def preprocess():
    """
    Endpoint para pré-processar um texto.
    ---
    parameters:
      - name: text
        in: body
        type: string
        required: true
        description: Texto a ser pré-processado.
    responses:
      200:
        description: Texto pré-processado com sucesso.
        schema:
          type: object
          properties:
            preprocessed_text:
              type: string
              description: Texto pré-processado.
    """
    data = request.get_json()
    text = data['text']
    preprocessed_text = preprocess_text(text)
    return jsonify({'preprocessed_text': preprocessed_text})
  
@app.route('/wordvec', methods=['POST'])
def wordvec():
    """
    Endpoint para obter o vetor de palavras de um texto.
    ---
    parameters:
      - name: text
        in: body
        type: string
        required: true
        description: Texto para o qual o vetor de palavras será calculado.
      - name: embedding_file
        in: body
        type: string
        required: true
        description: Caminho do arquivo de embedding.
    responses:
      200:
        description: Vetor de palavras calculado com sucesso.
        schema:
          type: object
          properties:
            word_vector:
              type: array
              description: Vetor de palavras.
              items:
                type: number
    """
    data = request.get_json()
    text = data['text']
    embedding_file = data['embedding_file']
    vector_df = prepare_word2vec_vectors(text, embedding_file)
    return jsonify({'word_vector': vector_df.values.tolist()})
  
@app.route('/xgboost', methods=['POST'])
def xgboost_predict():
    """
    Endpoint para obter a predição do modelo XGBoost a partir de um vetor de frase.
    ---
    parameters:
      - name: phrase_vector
        in: body
        required: true
        schema:
          type: object
          properties:
            phrase_vector:
              type: array
              items:
                type: float
              description: Vetor de frase para predição.
    responses:
      200:
        description: Predição do modelo calculada com sucesso.
        schema:
          type: object
          properties:
            prediction:
              type: array
              items:
                type: float
              description: Predição do modelo.
    """
    vectorized_text = request.json['phrase_vector']
    # Fazer a predição usando o modelo carregado
    prediction = predict_xgboost(vectorized_text, model)
    return jsonify({'prediction': prediction.tolist()})
  
@app.route("/analise_xgboost", methods=["POST"])
def analyze_sentiment():
    """
    Endpoint para análise de sentimento de um texto.
    ---
    parameters:
      - name: text
        in: body
        type: string
        required: true
        description: Texto a ser analisado.
    responses:
      200:
        description: Sentimento analisado com sucesso.
        schema:
          type: object
          properties:
            sentiment:
              type: string
              description: Sentimento do texto.
    """
    data = request.get_json()
    text = data['text']
    preprocessed_text = preprocess_text(text)
    vector_df = prepare_word2vec_vectors(preprocessed_text, '../models/GoogleNews-vectors-negative300.bin')
    # Ensure the prediction is converted to a list
    prediction = predict_xgboost(vector_df.values[0], model).tolist()
    
    if prediction == [2.0]:
        sentiment_message = "positive"
    elif prediction == [0.0]:
        sentiment_message = "negative"
    else:
        sentiment_message = "neutral"
    
    send_slack_alert(f"Analyzed text: {text}\nPrediction: {sentiment_message} {prediction}")
    
    return jsonify({'prediction': prediction})
  
@app.route('/test_slack_message', methods=['GET'])
def test_slack_message():
    try:
        send_slack_alert("Test message from Flask app")
        return jsonify({"message": "Test message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
if __name__ == '__main__':
    app.run(debug=True)