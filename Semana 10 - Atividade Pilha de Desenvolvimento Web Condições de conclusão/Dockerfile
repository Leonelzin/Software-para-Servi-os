# Imagem PHP Apache
FROM php:7.4-apache

# Atualizando o sistema e instalando dependências
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libzip-dev \
    git \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Instalando extensões PHP necessárias
RUN docker-php-ext-install pdo pdo_mysql mysqli intl zip

# Configurando o PHP
RUN echo "date.timezone = 'America/Sao_Paulo'" >> /usr/local/etc/php/php.ini

# Habilitando o módulo Apache de reescrita
RUN a2enmod rewrite

# Copiando os arquivos do aplicativo para o diretório de trabalho no contêiner
COPY ./app /var/www/html

# Expondo a porta 80 para o servidor web
EXPOSE 80

# Definindo um ponto de entrada para o contêiner
CMD ["apache2-foreground"]
