import dash
from dash import html, dcc
from visualization import create_bar_chart, create_user_messages_count_chart, create_common_words_chart, create_message_time_of_day_chart


def create_dash_app(total_emoji_counts, user_message_counts, messages_time_of_day, common_words):

    fig_emoji = create_bar_chart(total_emoji_counts)
    fig_user_message_counts = create_user_messages_count_chart(user_message_counts)
    fig_common_words = create_common_words_chart(common_words)
    fig_message_time_of_day = create_message_time_of_day_chart(messages_time_of_day)

    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.Div(
            className="app-header",
            children=[
                html.Div('WhatsApp Chat Statistics', className="app-header--title"),
            ]
        ),
        html.Div(
            className="app-container",
            children=[
                html.Div([
                    dcc.Graph(
                        id='top-left-graph',
                        figure=fig_user_message_counts,
                        className='graph'
                    )
                ], className='graph-container'),
                html.Div([
                    dcc.Graph(
                        id='top-right-graph',
                        figure=fig_common_words,
                        className='graph'
                    )
                ], className='graph-container'),
                html.Div([
                    dcc.Graph(
                        id='bottom-left-graph',
                        figure=fig_emoji,
                        className='graph'
                    )
                ], className='graph-container'),
                html.Div([
                    dcc.Graph(
                        id='bottom-right-graph',
                        figure=fig_message_time_of_day,
                        className='graph'
                    )
                ], className='graph-container'),
            ]
        )
    ], className='row')
    return app
