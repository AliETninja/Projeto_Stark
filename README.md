# Projeto_Stark

Documentação do Código Flask para Integração com Stark Bank

Este repositório contém um exemplo de código em Flask para integração com a API do Stark Bank, incluindo a criação de faturas e transferências e a configuração de um webhook para receber notificações de crédito. O código é projetado para ser executado localmente.

# Pré-requisitos
Antes de executar este código, você precisará das seguintes ferramentas:

° Python 3.x

° Flask

° APScheduler

° Stark Bank SDK

# Instalação

Para instalar as dependências do projeto, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```
# Configuração

Acesse a pasta

`settings`

Você precisará criar uma conta no [Stark Bank](https://starkbank.com/), obter um projeto ID e gerar a chave publica e privada fornecida em seu computador.

Para fazer isso basta rodar o comando 

```bash
python create_keys.py
```

Esse comando irá criar um par de chaves "private-key.perm" e "public-key.perm", com essas chaves em mãos voce ja consegue configuar e interagir com o seu projeto criado no site da Starkbank

Antes de executar o código, você precisará configurar algumas informações no arquivo `project_config.py`. Insira ID do seu projeto da Stark Bank na variável `PROJECT_ID`.

# Configuração do Webhook
Para receber notificações de crédito, é necessário que o webhook esteja configurado para um endpoint externo acessível na Internet. No entanto, executar o servidor Flask localmente não permitirá que o webhook receba notificações.

Para criar um endpoint externo, você pode usar a ferramenta Ngrok, que permite criar um túnel seguro para expor um servidor local para a Internet.

# Instalação do Ngrok
Para instalar o Ngrok, acesse o [site oficial](https://ngrok.com/) e siga as instruções de instalação para a sua plataforma.

# Configuração do Ngrok
Após a instalação, execute o comando `ngrok http 80` no terminal para criar um túnel na porta 80, que é a porta padrão para o servidor Flask. Isso criará um endpoint externo, que pode ser usado para configurar o webhook.

Copie o URL fornecido pelo Ngrok e adicione-o à configuração do webhook no painel do Stark Bank.
Lembre-se de colocar o endpoint que direciona ao Webhook escrito no codigo.

Exemplo:

```bash
<sua-URL-Ngrok>/starkbank/webhook
```

Agora, o webhook estará configurado para receber notificações de crédito no endpoint externo fornecido pelo Ngrok.


# Execução
Para executar o código, execute o seguinte comando no terminal:

```bash
python app.py
```
Este comando iniciará o servidor Flask e agendará a criação de faturas a cada 3 horas. O webhook será configurado para receber notificações de crédito, e disparar
a transação, como instruido no desafio

# Funcionalidades
O código tem as seguintes funcionalidades:

° Criação de 8 a 12 faturas usando o método starkbank.invoice.create()

° Criação de transferências com o paramentro "amount" usando o método starkbank.transfer.create()

° Configuração de um webhook para receber notificações de crédito

° Agendamento de criação de faturas usando o APScheduler


O arquivo `generator.py` contém as definições das classes para gerar as faturas, transferências e dados dos clientes.
