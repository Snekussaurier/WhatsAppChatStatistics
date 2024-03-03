import psycopg2
from psycopg2.extras import execute_batch


def connect_to_db():
    return psycopg2.connect(
        dbname="whatsapp_groupchat_data", user="postgres", password="postgres", host="localhost"
    )


def insert_chat_data_to_db(df, conn):
    cursor = conn.cursor()
    delete_query = "DELETE FROM whatsapp_messages;"
    insert_query = """
    INSERT INTO whatsapp_messages (sender, message, timestamp) 
    VALUES (%s, %s, %s);
    """
    data_tuples = [(row['sender'], row['message'], row['timestamp'].to_pydatetime()) for _, row in df.iterrows()]
    try:
        print("Deleting existing data! :3")
        cursor.execute(delete_query)
        execute_batch(cursor, insert_query, data_tuples)
        conn.commit()
        print("Data inserted successfully! :3")
    except Exception as e:
        print("An error occurred while inserting the data: ", e)
        conn.rollback()
    finally:
        cursor.close()


def insert_emoji_counts_to_db(emoji_counts, conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emoji_counts;")
    for emoji, count in emoji_counts.items():
        cursor.execute('INSERT INTO emoji_counts (emoji, count) VALUES (%s, %s);', (emoji, count))
    conn.commit()
    cursor.close()


def retrieve_user_message_counts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_message_counts;")
    return dict(cursor.fetchall())


def retrieve_messages_time_of_day(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages_time_of_day;")
    return dict(cursor.fetchall())


def retrieve_common_words(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM common_words;")
    return dict(cursor.fetchall())
