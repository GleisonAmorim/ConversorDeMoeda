# Usa a imagem base do Python 3.8
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto para o contêiner
COPY . .

# Especifica o comando a ser executado ao iniciar o contêiner
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
