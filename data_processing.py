import re
import emoji
import string
import pandas as pd
import yaml
from collections import Counter


def read_valid_users_from_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        users_data = yaml.safe_load(file)
        return set(users_data['users'])


def analyze_chat_data(filepath, valid_users):
    pattern = re.compile(r"\[(\d{2}\.\d{2}\.\d{2}), (\d{2}:\d{2}:\d{2})] ([^:]+): (.+)")
    data = []
    current_message = None
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if pattern.match(line):
                if current_message:
                    data.append(current_message)
                date, time, sender, message = pattern.match(line).groups()
                if '\u200E' in message:
                    continue
                message = re.sub(f"[{string.punctuation}]", "", message)
                if sender in valid_users:
                    timestamp = pd.to_datetime(f'{date} {time}')
                    current_message = (sender, message, timestamp)
            else:
                if current_message:
                    if '\u200E' in line:
                        continue
                    line = re.sub(f"[{string.punctuation}]", "", line.strip())
                    current_message = current_message[:1] + (current_message[1] + '\n' + line.strip(),) + current_message[2:]
        if current_message and not '\u200E' in current_message[1]:
            data.append(current_message)
    df = pd.DataFrame(data, columns=['sender', 'message', 'timestamp'])
    return df


def count_emojis(message):
    emoji_counts = {}
    appearing_emojis = emoji.emoji_list(message)
    for emoji_icon in appearing_emojis:
        if emoji_icon['emoji'] not in emoji_counts.keys():
            emoji_counts[emoji_icon['emoji']] = 1
        else:
            emoji_counts[emoji_icon['emoji']] += 1
    return emoji_counts
