# Use uma imagem base do Python leve
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia a pasta `app` para o diretório de trabalho do contêiner
COPY app/ /app/

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que será usada pela API Flask
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
