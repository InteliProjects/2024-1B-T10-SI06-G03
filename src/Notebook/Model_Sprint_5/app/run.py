# Esse código está devidamente documentado na seção 11 da documentação do projeto. 
# Você pode acessa-lo nesse link: https://github.com/Inteli-College/2024-1B-T10-SI06-G03/blob/main/docs/documentacao.md#11-deploy

from flask import Flask, request, jsonify
from flasgger import Swagger
import pickle
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
import os 
from flask_sqlalchemy import SQLAlchemy  # Importa o SQLAlchemy
from threading import Thread

# OBS: Referência -> O detalhamento do código e a justificativa da utilização do arquivo "run.py" está documentado na secção "11. Deploy", em "11.3.3 Integração com o Arquivo run.py " na pasta "docs" em "documentacao.md"

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'  # Usando SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configuração do Swagger
swagger = Swagger(app)

from model import preprocess_text, prepare1_fasttext_vectors, prepare2_fasttext_vectors, predict_xgboost

# Carregar os modelos pré-treinados
with open('./models/xgboost_negative_vs_rest.pkl', 'rb') as file:
    model_neg_vs_rest = pickle.load(file)

with open('./models/xgboost_positive_vs_neutral.pkl', 'rb') as file:
    model_pos_vs_neutral = pickle.load(file)

#Load do modelo FastText
print("O modelo irá carregar agora.")
print("Isso pode demorar...")
fasttext_model_path = './data/cc.en.100.vec'
embeddings = prepare1_fasttext_vectors(fasttext_model_path)
print("Modelo carregado!")

# Definir a variável de ambiente para o token do Slack
os.environ["SLACK_BOT_TOKEN"] = 'xoxb-7304409500788-7302580002723-8sUD50F25bttK0MMMg2a6Chm'

# Inicializar o aplicativo Slack
slack_app = App(token=os.getenv("SLACK_BOT_TOKEN"))
handler = SlackRequestHandler(slack_app)

def send_slack_alert(message):
    try:
        slack_app.client.chat_postMessage(
            channel="#sentiment_tracker_inteli",
            text="----------------------------------------------------"
        )
        response = slack_app.client.chat_postMessage(
            channel="#sentiment_tracker_inteli",
            text=message
        )
        app.logger.info(f"Message sent to Slack channel: {response}")
    except Exception as e:
        app.logger.error(f"Error sending message to Slack: {e}")
        
# Definição do modelo para armazenar as frases
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    preprocessed_text = db.Column(db.String(500))
    sentiment = db.Column(db.String(50))

    def __init__(self, text, preprocessed_text, sentiment):
        self.text = text
        self.preprocessed_text = preprocessed_text
        self.sentiment = sentiment

# Criar o banco de dados e as tabelas
with app.app_context():
    db.create_all()

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
  
@app.route('/fasttext', methods=['POST'])
def fasttext():
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

    #Vetorização da frase
    vector_df = prepare2_fasttext_vectors(text, embeddings)

    word_vector = vector_df.tolist()
    return jsonify({'word_vector': word_vector})
  
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
    fasttext_model_path = './data/cc.en.100.vec'
    
    # Certifique-se de passar os modelos já carregados
    prediction = predict_xgboost(text, embeddings, model_neg_vs_rest, model_pos_vs_neutral)

    emoji = ""
    if prediction == 1: #🟢🔴🟡
        sentiment_message = "positive"
        emoji = ":large_green_circle:"
    elif prediction == -1:
        sentiment_message = "negative"
        emoji = ":red_circle:"
    else:
        sentiment_message = "neutral"
        emoji = ":large_yellow_circle:"

    new_comment = Comment(text=text, preprocessed_text=preprocessed_text, sentiment=sentiment_message)
    db.session.add(new_comment)
    db.session.commit()

    
    send_slack_alert(f"Analyzed text: {text}\nPrediction: {sentiment_message} {emoji}")
    
    return jsonify({'prediction': f"{sentiment_message}" })
  
@app.route('/test_slack_message', methods=['GET'])
def test_slack_message():
    try:
        send_slack_alert("Test message from Flask app")
        return jsonify({"message": "Test message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)

    flask_thread.start()

    flask_thread.join()
