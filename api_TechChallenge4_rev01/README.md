# Projeto de Previsão com LSTM

## Objetivo
Este projeto utiliza um modelo LSTM para previsão de preços com base em dados históricos. 
A API Flask serve o modelo e permite que os usuários forneçam dados históricos e recebam previsões futuras.

## Requisitos
- Python 3.x
- TensorFlow
- Flask
- tensorflow
- numpy
- scikit-learn
- flask_monitoringdashboard


## Contêineres Docker para deploy da API.
1. Com o arquivo Dockerfile e requirements.txt prontos, você pode criar a imagem Docker e rodá-la
2. para construir a imagem Docker, use umterminal e insira o comando no rojeto | docker build -t api-lstm .
3. apos baixar use o camando para executer container Docker | docker run -p 5000:5000 api-lstm
4. Usando Docker Desktop para gerenciamento, Com isso, a API Flask será executada dentro de um contêiner Docker e estará acessível na URL http://127.0.0.1:5000/
5. Ao iniciar o Docoker é necessario indicar nas configuraçoes "port:5000"


## Como executar
1. use o arquivo app.py para subir localmente a aplicação de previsao ou com o Docker ative o serviço e ative(run) a imagem api-lstm 
2. pode verificar o status com o endereço http://127.0.0.1:5000 em um navegador e verá {
  "message": "API de Previs\u00e3o LSTM est\u00e1 ativa!"
}
3. use um programa plataforma para API por exemplo o Postman
4. use o endpoint (link) http://127.0.0.1:5000/predict e o metoto Post, enviar no body um tipo json ex:{
    "historical_data": [
        [150.23], 
        [152.35], 
        [151.78], 
        [153.50], 
        [152.70], 
        [154.10]
    ]
}
  o retorno previsões dos valores de preços futuros será nesse formato {
    "prediction": [
        152.67
    ]
}
