# WhatsApp Chat Statistics

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
- PostgreSQL database

## Installation

1. Clone the repository.

2. Install the required dependencies:

```pip install -r requirements.txt```

3. Set up a PostgreSQL database with the appropriate tables for storing chat data.

## Usage

1. Download your ```_chat.txt``` file and place it in to the root directory

2. Modify the configuration file `config.yaml` with your PostgreSQL database credentials and other settings.

3. Run the Python script to analyze the chat data:

```python3 main.py```

4. Access the web interface by navigating to `http://localhost:8050` in your web browser.
