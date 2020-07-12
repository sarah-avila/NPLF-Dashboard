import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as plot

df = pd.read_excel('Temporary Dataset -- VandyHacks Summer 2020.xlsx')

fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Advertising']))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Reach']))
fig3 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Google Analytics']))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['TwitterReach']))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['LinkedIn Reach']))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Email Marketing']))
fig7 = plot.Figure()
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Advertising'],
                    mode='lines+markers',
                    name='Facebook Advertising'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Reach'],
                    mode='lines+markers', name='Facebook Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Google Analytics'],
                    mode='lines+markers', name='Google Analytics'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['TwitterReach'],
                    mode='lines', name='TwitterReach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['LinkedIn Reach'],
                    mode='lines', name='LinkedIn Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Email Marketing'],
                    mode='lines', name='Email Marketing'))

app = dash.Dash()
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Facebook Advertising'),
            dcc.Graph(
        id='g1',
        figure=fig1,
    )],className="six columns"),

        html.Div([
            html.H3('Facebook Reach'),
            dcc.Graph(id='g2', figure=fig2)
        ], className="six columns"),
    ], className="row"),
    html.Div([
        html.Div([
            html.H3('Google Analytics'),
            dcc.Graph(
        id='g3',
        figure=fig3,
    )],className="six columns"),

        html.Div([
            html.H3('Twitter Reach'),
            dcc.Graph(id='g4', figure=fig4)
        ], className="six columns"),
    ], className="row"),
    html.Div([
        html.Div([
            html.H3('LinkedIn Reach'),
            dcc.Graph(
        id='g5',
        figure=fig5,
    )],className="six columns"),

        html.Div([
            html.H3('Email Marketing'),
            dcc.Graph(id='g6', figure=fig6)
        ], className="six columns"),
    ], className="row"),
    html.Div([
            html.H3('Summary'),
            dcc.Graph(
        id='g7',
        figure=fig7,
    )],className="six columns")

])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
