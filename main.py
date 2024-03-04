import pandas as pd
import yaml
from collections import Counter
from database import connect_to_db, insert_chat_data_to_db, insert_emoji_counts_to_db, retrieve_user_message_counts, retrieve_messages_time_of_day, retrieve_common_words
from data_processing import analyze_chat_data, count_emojis, read_valid_users_from_yaml
from dash_app import create_dash_app


def main():
    chat_file_path = '_chat.txt'
    valid_users_path = 'config.yaml'

    valid_users = read_valid_users_from_yaml(valid_users_path)
    df = analyze_chat_data(chat_file_path, valid_users)

    total_emoji_counts = Counter()
    for message in df['message']:
        total_emoji_counts.update(count_emojis(message))

    conn = connect_to_db()

    print("Multi-line chat data analyzed and stored in the database! UwU")

    insert_emoji_counts_to_db(total_emoji_counts, conn)
    insert_chat_data_to_db(df, conn)

    print("Retrieving analyzed data from the database! OwO")

    user_message_counts = retrieve_user_message_counts(conn)
    messages_time_of_day = retrieve_messages_time_of_day(conn)
    common_words = retrieve_common_words(conn)

    print("Starting statistics dashboard! ^^")

    app = create_dash_app(total_emoji_counts, user_message_counts, messages_time_of_day, common_words)
    app.run_server(host='0.0.0.0')


if __name__ == "__main__":
    main()
