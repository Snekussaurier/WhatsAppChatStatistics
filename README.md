# WhatsApp Chat Statistics

[![Made with Python](https://img.shields.io/badge/Python->=3.11-purple?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![Made with PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-purple?logo=postgresql&logoColor=white)](https://www.postgresql.org/ "Go to PostgresSQL homepage")
[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-purple?logo=github-actions&logoColor=white)](https://github.com/features/actions "Go to GitHub Actions homepage")

<img width="100%" alt="Screenshot 2024-03-04 at 19 54 16" style="border-radius: 15px;" src="https://github.com/Snekussaurier/WhatsAppChatStatistics/assets/68194327/08437255-2e4f-4707-bb12-e2467aa53d55">

## Overview

This Python application is designed to analyze WhatsApp group chat data and provide various statistics. It includes functionalities to process chat data, extract information such as message counts, common words, emojis, and message distribution over time, and visualize the results using a web interface built with Dash and Plotly.

## Features

- Import WhatsApp chat data from a text file.
- Analyze chat data to extract:
  - Message counts per user.
  - Commonly used words and their frequencies.
  - Emojis and their frequencies.
  - Message distribution over time.
- Visualize the extracted statistics using interactive charts and graphs.

## Requirements

- Python 3.x
- Docker
- Docker Compose

## Installation

1. Clone the repository.

2. Install Docker and Docker Compose if you haven't already.

3. Set up a PostgreSQL database with the appropriate tables for storing chat data.

## Configuration

Modify the `config.yaml` file with the following configuration:

```yaml
users:
  - Alice
  - Bob
  - Charlie
  - David
  - Emily
  - Frank
  - Grace
  - Harry

database:
  dbname: "whatsapp_groupchat_data"
  user: "postgres"
  password: "postgres"
  host: "postgres"
```

The users section should contain a list of valid users in your WhatsApp group chat, and the database section specifies the PostgreSQL database credentials and host.

## Docker Compose
Use the provided docker-compose.yml file to set up the required services:

```yaml
version: '3.8'

services:
  postgres:
    # PostgreSQL container configuration...

  pgadmin:
    # pgAdmin container configuration...

  whatsapp_chat_statistics:
    image: whatsapp-chat-statistics:latest
    container_name: whatsapp_chat_statistics_container
    volumes:
      - ./_chat.txt:/app/_chat.txt
      - ./config.yaml:/app/config.yaml
    ports:
      - "8050:8050"
    restart: always
    depends_on:
      - postgres

volumes:
  postgres_data:
  pgadmin_data:
```

The whatsapp_chat_statistics service mounts the _chat.txt file and config.yaml into the container and exposes port 8050 for accessing the web interface.

## Installation

### Manually

1. Clone the repository.

2. Install the required dependencies:

```pip install -r requirements.txt```

3. Set up a PostgreSQL database with the appropriate tables for storing chat data.

## Usage

Download your `_chat.txt` file and place it into the root directory.

Modify the `config.yaml` file with your configuration.

Run the following command to start the application using Docker Compose:

 ```sh
docker-compose up -d
```
Access the web interface by navigating to http://localhost:8050 in your web browser.

When you're done, you can stop the application with:

```sh
docker-compose down
```
