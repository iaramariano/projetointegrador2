# 1. Imagem base com Python
FROM python:3.11-slim


# 2. Instalar dependências do sistema, incluindo netcat
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 3. Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Criar e definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# 5. Copiar o arquivo de dependências e instalar
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Copiar o restante do código do projeto para o diretório de trabalho
COPY . /app/

# 7. Expor a porta que a aplicação vai rodar (opcional, boa prática)
EXPOSE 8000

# 8. Comando para rodar a aplicação (usando Gunicorn para produção)
CMD ["/app/start.sh"]
