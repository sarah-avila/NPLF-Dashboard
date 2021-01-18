import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as plot
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from plotly.subplots import make_subplots
import plotly
import dash_auth
from dash.dependencies import Input, Output
import numpy as np

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Twitter graph ------------------------------------------------

df = pd.read_excel('NPLF Twitter 2022.xlsx')

fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['impressions'], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['engagement rate'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(
    data=plot.Scatter(x=df['Date'], y=df['detail expands'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['likes'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media views'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media engagements'], mode='lines+markers', line_color="#1cd3f3"))
fig7 = go.Figure()
fig7.update_layout(title="Twitter", width=995, height= 500)

trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]
trace4 = fig4['data'][0]
trace5 = fig5['data'][0]
trace6 = fig6['data'][0]

fig7.add_trace(go.Scatter(trace1,
                            mode='lines+markers',
                            name='Impressions'))
fig7.add_trace(go.Scatter(trace2,
                            mode='lines+markers', name='Engagement rate'))
fig7.add_trace(go.Scatter(trace3,
                            mode='lines+markers', name='Detail expands'))
fig7.add_trace(go.Scatter(trace4,
                            mode='lines+markers', name='Likes'))
fig7.add_trace(go.Scatter(trace5,
                            mode='lines+markers', name='Media Views'))
fig7.add_trace(go.Scatter(trace6,
                            mode='lines+markers', name='Media Engagements'))

# Facebook graph ------------------------------------------------

df1 = pd.read_excel('FacebookPosts2022.xlsx')

fig1 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Reach'], mode='lines+markers', ))
fig2 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Impressions'], mode='lines+markers', line_color="#ef5a41"))
fig3 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Engaged Users'], mode='lines+markers',line_color="#00cc96" ))
fig4 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'], mode='lines+markers',line_color="#9467bd" ))
fig5 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'], mode='lines+markers', line_color="#ffa15a"))
fig6 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Impressions by people who have liked your Page'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post reach by people who like your Page'], mode='lines+markers',line_color="#1cd3f3" ))
fig9 = go.Figure()
fig9.update_layout(title="Facebook", width=995, height= 500)
fig9.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Reach'],
                            mode='lines+markers',
                            name='Lifetime Post Total Reach'))
fig9.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Impressions'],
                            mode='lines+markers',
                            name='Lifetime Post Total Impressions'))
fig9.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Engaged Users'],
                            mode='lines+markers',
                            name='Lifetime Engaged Users'))
fig9.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumers on Post'))
fig9.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumptions on Post'))

# LinkedIn graph ------------------------------------------------

df2 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = [0,1,2,3,4])
df3 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = 'Company size')
df4 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = 'Update metrics (aggregated)')
df5 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = 'Industry')
df6 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = 'Seniority')

fig1 = plot.Figure(data=plot.Scatter(y=df4["Date"], x=df4["Impressions (organic)"], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Impressions (sponsored)'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Unique impressions (organic)'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (organic)'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (sponsored)'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Reactions (organic)'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (organic)'], mode='lines+markers', line_color="#F5A10E"))
fig11 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (sponsored)'], mode='lines+markers', line_color="#0EF596"))
fig10 = go.Figure()
fig10.update_layout(title="LinkedIn", width=995, height= 500)

#Quarter 1 (april to june)

fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (organic)'],
                            mode='lines+markers',
                            name= 'Impressions (organic)'))#row = 3, col = 1)
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (sponsored)'],
                            mode='lines+markers', name='Impressions (sponsored)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Unique impressions (organic)'],
                            mode='lines+markers', name='Unique impressions (organic)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (organic)'],
                            mode='lines+markers', name='Clicks (organic)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (sponsored)'],
                            mode='lines+markers', name='Clicks (sponsored)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Reactions (organic)'],
                            mode='lines+markers', name='Reactions (organic)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (organic)'],
                            mode='lines+markers', name='Engagement rate (organic)'))
fig10.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (sponsored)'],
                            mode='lines+markers', name='Engagement rate (sponsored)'))


# default rangeslider/graph values
min_value = '2022-01-01'
max_value = '2022-12-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
date_mark = {i: dates[i] for i in range(0, 12)}


# app and layout definition
app.layout = html.Div([
    html.Div([
         html.Div([
            html.H2('Summary of January - December 2022'),
        ], style={"marginTop" : "50px"}),
        # first graph -- Twitter
        html.Div([
            dcc.Graph(
                id='g7',
                figure=fig7,
            )], className="heading"),

        # first range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='slider',
                marks=date_mark,
                min=0,
                max=11,
                value=[0, 11],
                allowCross=False
            ),
        ], className="rangeSlider"),

        # second graph -- Facebook
         html.Div([
            dcc.Graph(
                id='g9',
                figure=fig9,
            )], className="heading"),

        # second range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='slider',
                marks=date_mark,
                min=0,
                max=11,
                value=[0, 11],
                allowCross=False
            ),
        ], className="rangeSlider"),

        # third graph -- LinkedIn
        html.Div([
            dcc.Graph(
                id='g10',
                figure=fig10,
            )], className="heading"),
        # third range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='slider',
                marks=date_mark,
                min=0,
                max=11,
                value=[0, 11],
                allowCross=False
            ),
        ], className="rangeSlider"),

        html.Div([
            html.H5('Source: Nashville Public Library Foundation Official Records')
        ], className="source")
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)