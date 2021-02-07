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

df = pd.read_excel('NPLF Twitter 2023.xlsx')

fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['impressions'], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['engagement rate'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(
    data=plot.Scatter(x=df['Date'], y=df['detail expands'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['likes'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media views'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['media engagements'], mode='lines+markers', line_color="#1cd3f3"))
twitter_2023 = go.Figure()
twitter_2023.update_layout( 
    width=995, 
    height= 500,
    title_text="Twitter",
    font_family="'Poppins', sans-serif",
    font_color="black",
    font_size= 15,
    title_font_family="'Poppins', sans-serif",
    title_font_color="black",
    title_font_size = 35,
    title = dict (
    xanchor = 'left'
    ),
    
      legend=dict(
        x=1.3,
        y=0.5,
        valign = "middle",
       xanchor = "right",
#        yanchor = "top",
#        traceorder="reversed",
        
        bgcolor="white",
        bordercolor="Black",
        borderwidth=2
    ),
    legend_title="Twitter Data",
    legend_title_font_color="brown",
    legend_title_font_size=20
)

trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]
trace4 = fig4['data'][0]
trace5 = fig5['data'][0]
trace6 = fig6['data'][0]

twitter_2023.add_trace(go.Scatter(trace1,
                            mode='lines+markers',
                            name='Impressions'))
twitter_2023.add_trace(go.Scatter(trace2,
                            mode='lines+markers', name='Engagement rate'))
twitter_2023.add_trace(go.Scatter(trace3,
                            mode='lines+markers', name='Detail expands'))
twitter_2023.add_trace(go.Scatter(trace4,
                            mode='lines+markers', name='Likes'))
twitter_2023.add_trace(go.Scatter(trace5,
                            mode='lines+markers', name='Media Views'))
twitter_2023.add_trace(go.Scatter(trace6,
                            mode='lines+markers', name='Media Engagements'))

# Facebook graph ------------------------------------------------

df1 = pd.read_excel('FacebookPosts2023.xlsx')

fig1 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Reach'], mode='lines+markers', ))
fig2 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Impressions'], mode='lines+markers', line_color="#ef5a41"))
fig3 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Engaged Users'], mode='lines+markers',line_color="#00cc96" ))
fig4 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'], mode='lines+markers',line_color="#9467bd" ))
fig5 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'], mode='lines+markers', line_color="#ffa15a"))
fig6 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post Impressions by people who have liked your Page'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = go.Figure(data=go.Scatter(x=df1['Date'], y=df1['Lifetime Post reach by people who like your Page'], mode='lines+markers',line_color="#1cd3f3" ))
facebook_2023 = go.Figure()
facebook_2023.update_layout(
    width=995, 
    height= 500,
    title_text="Facebook",
    font_family="'Poppins', sans-serif",
    font_color="black",
    font_size= 15,
    title_font_family="'Poppins', sans-serif",
    title_font_color="black",
    title_font_size = 35,
    title = dict (
    xanchor = 'left'
    ),
    
      legend=dict(
        x=1.7,
        y=0.5,
        valign = "middle",
       xanchor = "right",
#        yanchor = "top",
#        traceorder="reversed",
        
        bgcolor="white",
        bordercolor="Black",
        borderwidth=2
    ),
    legend_title="Facebook Data",
    legend_title_font_color="brown",
    legend_title_font_size=20
)

facebook_2023.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Reach'],
                            mode='lines+markers',
                            name='Lifetime Post Total Reach'))
facebook_2023.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Post Total Impressions'],
                            mode='lines+markers',
                            name='Lifetime Post Total Impressions'))
facebook_2023.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Engaged Users'],
                            mode='lines+markers',
                            name='Lifetime Engaged Users'))
facebook_2023.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumers on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumers on Post'))
facebook_2023.add_trace(go.Scatter(x=df1['Date'], y=df1['Lifetime Matched Audience Targeting Consumptions on Post'],
                            mode='lines+markers',
                            name='Lifetime Matched Audience Targeting Consumptions on Post'))

# LinkedIn graph ------------------------------------------------

df2 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = [0,1,2,3,4])
df3 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = 'Company size')
df4 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = 'Update metrics (aggregated)')
df5 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = 'Industry')
df6 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = 'Seniority')

fig1 = plot.Figure(data=plot.Scatter(y=df4["Date"], x=df4["Impressions (organic)"], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Impressions (sponsored)'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Unique impressions (organic)'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (organic)'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Clicks (sponsored)'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Reactions (organic)'], mode='lines+markers', line_color="#1cd3f3"))
fig8 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (organic)'], mode='lines+markers', line_color="#F5A10E"))
fig11 = plot.Figure(data=plot.Scatter(y=df4['Date'], x=df4['Engagement rate (sponsored)'], mode='lines+markers', line_color="#0EF596"))
linkedin_2023 = go.Figure()
linkedin_2023.update_layout(
    width=995,
    height= 500,
    title_text="LinkedIn",
    font_family="'Poppins', sans-serif",
    font_color="black",
    font_size= 15,
    title_font_family="'Poppins', sans-serif",
    title_font_color="black",
    title_font_size = 35,
    title = dict (
    xanchor = 'left'
    ),
    
      legend=dict(
        x=1.5,
        y=0.5,
        valign = "middle",
       xanchor = "right",
#        yanchor = "top",
#        traceorder="reversed",
        
        bgcolor="white",
        bordercolor="Black",
        borderwidth=2
    ),
    legend_title="Linkedin Data",
    legend_title_font_color="brown",
    legend_title_font_size=20
)

#Quarter 1 (april to june)

linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (organic)'],
                            mode='lines+markers',
                            name= 'Impressions (organic)'))#row = 3, col = 1)
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Impressions (sponsored)'],
                            mode='lines+markers', name='Impressions (sponsored)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Unique impressions (organic)'],
                            mode='lines+markers', name='Unique impressions (organic)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (organic)'],
                            mode='lines+markers', name='Clicks (organic)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Clicks (sponsored)'],
                            mode='lines+markers', name='Clicks (sponsored)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Reactions (organic)'],
                            mode='lines+markers', name='Reactions (organic)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (organic)'],
                            mode='lines+markers', name='Engagement rate (organic)'))
linkedin_2023.add_trace(plot.Scatter(x=df4['Date'], y=df4['Engagement rate (sponsored)'],
                            mode='lines+markers', name='Engagement rate (sponsored)'))


# default rangeslider/graph values
min_value = '2020-01-01'
max_value = '2021-01-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
date_mark = {i: dates[i] for i in range(0, 13)}


# app and layout definition
app.layout = html.Div([
    html.Div([
         html.Div([
            html.H2('Summary of January - December 2023'),
        ], style={"marginTop" : "50px"}),
        # first graph -- Twitter
        html.Div([
            dcc.Graph(
                id='twitter_2023',
                figure=twitter_2023,
            )], className="heading"),

        # first range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='twitter-2023',
                marks=date_mark,
                min=0,
                max=12,
                value=[0, 12],
                allowCross=False
            ),
        ], className="rangeSlider"),

        # second graph -- Facebook
         html.Div([
            dcc.Graph(
                id='facebook_2023',
                figure=facebook_2023,
            )], className="heading"),

        # second range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='facebook-2023',
                marks=date_mark,
                min=0,
                max=12,
                value=[0, 12],
                allowCross=False
            ),
        ], className="rangeSlider"),

        # third graph -- LinkedIn
        html.Div([
            dcc.Graph(
                id='linkedin_2023',
                figure=linkedin_2023,
            )], className="heading"),
        # third range slider with input boxes
        html.Div([
            html.Label("Time Period"),
        ], style={"fontSize" : "20px", "marginTop" : "30px"}),
        html.Div(
        [
            dcc.RangeSlider(
                id='linkedin-2023',
                marks=date_mark,
                min=0,
                max=12,
                value=[0, 12],
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

