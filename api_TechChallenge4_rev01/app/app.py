from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import flask_monitoringdashboard as dashboard  # Importar o Dashboard

# Inicializar a aplicação Flask
app = Flask(__name__)

# Configurar o Flask Monitoring Dashboard
dashboard.bind(app)

# Carregar o modelo LSTM salvo
model = tf.keras.models.load_model('modelo_lstm_previsao.h5')

# Configurar o MinMaxScaler com os mesmos parâmetros usados no treinamento
scaler = MinMaxScaler(feature_range=(0, 1))

# Rota para testar a API
@app.route('/')
def home():
    return jsonify({'message': 'API de Previsão LSTM está ativa!'})

# Rota para previsão
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receber os dados no formato JSON
        data = request.get_json()

        # Verificar se os dados estão no formato correto
        if 'historical_data' not in data:
            return jsonify({'error': 'Dados históricos não fornecidos!'}), 400

        # Extrair os dados históricos
        historical_data = data['historical_data']  # Espera-se uma lista de listas

        # Converter os dados para um array NumPy
        input_data = np.array(historical_data)

        # Aplicar o mesmo escalonamento usado no treinamento
        scaled_data = scaler.fit_transform(input_data)

        # Ajustar o formato para (1, timesteps, features) para o modelo LSTM
        input_data_scaled = scaled_data.reshape(1, scaled_data.shape[0], scaled_data.shape[1])

        # Fazer a previsão
        scaled_prediction = model.predict(input_data_scaled)

        # Reverter a previsão para a escala original
        prediction = scaler.inverse_transform(scaled_prediction)

        # Formatar a previsão para 2 casas decimais e garantir que seja serializável
        formatted_prediction = [round(float(value), 2) for value in prediction[0]]

        # Retornar a previsão como resposta
        return jsonify({'prediction': formatted_prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Rodar a API localmente
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    app.run(host='0.0.0.0', port=5000, debug=True)

