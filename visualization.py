import plotly.express as px
import pandas as pd


def create_user_messages_count_chart(user_messages_count):
    fig = px.pie(values=list(user_messages_count.values()),
                 names=list(user_messages_count.keys()),
                 title='Message count by User',
                 hole=0.3,
                 labels={'names': 'User', 'values': 'Messages'})

    return fig


def create_bar_chart(emoji_counts):
    emoji_df = pd.DataFrame(sorted(emoji_counts.items(), key=lambda x: -x[1]), columns=['Emoji', 'Count'])
    fig = px.bar(emoji_df.head(10),
                 x='Emoji',
                 y='Count',
                 title='Top 10 Emojis',
                 color='Emoji',
                 labels={'Emoji': 'Emoji', 'Count': 'Count'})

    # Add text annotations to the bars
    for i in range(len(emoji_df.head(10))):
        fig.add_annotation(x=emoji_df['Emoji'][i], y=emoji_df['Count'][i],
                           text=str(emoji_df['Count'][i]),
                           font=dict(color='black', size=12),
                           showarrow=False,
                           xanchor='center', yanchor='bottom')

    # Remove legend
    fig.update_layout(showlegend=False)

    return fig


def create_common_words_chart(common_words):
    common_words_df = pd.DataFrame(common_words.items(), columns=['Word', 'Count'])

    # Create a bar chart using Plotly Express
    fig = px.bar(common_words_df.head(10),  # Select the top 10 common words
                 x='Word',
                 y='Count',
                 orientation='v',  # Horizontal bar chart
                 title='Top 10 Common Words',
                 labels={'Count': 'Frequency', 'Word': 'Word'})

    # Remove legend
    fig.update_layout(showlegend=False)

    return fig


def create_message_time_of_day_chart(message_time_of_day):
    message_time_of_day_df = pd.DataFrame(message_time_of_day.items(), columns=['Time of Day', 'Count'])

    fig = px.bar(message_time_of_day_df,
                 x='Count',
                 y='Time of Day',
                 orientation='h',
                 title='Messages sent at each Time of Day')

    # Remove legend
    fig.update_layout(showlegend=False)

    return fig
