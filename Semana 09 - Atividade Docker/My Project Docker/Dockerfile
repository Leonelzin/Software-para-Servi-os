# Use a imagem oficial do Python como base
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo Python para o diretório de trabalho
COPY app.py .

# Exponha a porta 8080
EXPOSE 8080

# Comando para iniciar o servidor web
CMD ["python", "app.py"]
