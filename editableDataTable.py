import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objects as plot
from pandas import ExcelWriter
from pandas import ExcelFile
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from plotly.subplots import make_subplots
import plotly
import dash_auth
from apps import year2020, year2021, year2022, year2023
from dash.dependencies import Input, Output
import numpy as np


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'NashvillePLFoundation@gmail.com': 'Foundation2018'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# Twitter Layout
twitterLayout = go.Layout(
    title="Twitter"
)
# Twitter Excel Sheet
df = pd.read_excel('NPLF Twitter Q1andQ2.xlsx')


# Facebook Layout
facebookLayout = go.Layout(
    title="Facebook"
)
# Facebook Excel Sheet
df1 = pd.read_excel('Facebook Posts Q1andQ2.xlsx')


# LinkedIn Layout
linkedinLayout = go.Layout(
    title="LinkedIn"
)
# Linkedin Excel Sheets
df2 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = [0,1,2,3,4])
df3 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Company size')
df4 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Update metrics (aggregated)')
df5 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Industry')
df6 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Seniority')
                            


# default rangeslider/graph values
min_value = '2020-01-01'
max_value = '2020-12-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
date_mark = {i: dates[i] for i in range(0, 12)}

# date slider labels
def set_rangeslider(minValue, maxValue):
    print("enter set_rangeSlider", minValue, maxValue)
    df['Date'] = pd.to_datetime(df.Date)
    dates = pd.date_range(minValue, maxValue, freq='MS').strftime("%Y-%b").tolist()
    # print(dates)
    date_mark = {i: dates[i] for i in range(0, 12)}
    # print(date_mark)
    return date_mark, dates



# navbar definition
sticky_navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Years", header=True),
                dbc.DropdownMenuItem("2020", href='/apps/year2020'),
                dbc.DropdownMenuItem("2021", href='/apps/year2021'),
                dbc.DropdownMenuItem("2022", href='/apps/year2022'),
                dbc.DropdownMenuItem("2023", href='/apps/year2023'),
            ],
            nav=True,
            in_navbar=True,
            label="Years",
        ),
    ],
    brand="Nashville Public Library Foundation",
    brand_href='https://nplf.org/',
    color="dark",
    dark=True,
    sticky="top",
)

# app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sticky_navbar,
    html.Div(id='page-content'),
])

# page navigation ---------------------------------------------------------

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print("pathname = ", pathname)
    if pathname == '/apps/year2021':
        return year2021.app.layout
    elif pathname == '/apps/year2022':
        return year2022.app.layout
    elif pathname == '/apps/year2023':
        return year2023.app.layout
    else:
        return year2020.app.layout

# first section -- Twitter ------------------------------------------------

@app.callback(Output('g7', 'figure'), [Input('slider-one', 'value'), Input('slider-one', 'marks')])
def update_graph(X, dates):

    dates = list(dates.values())

    df2 = df[(df.Date >= dates[X[0]]) & (df.Date <= dates[X[1]])]
    trace_1 = go.Scatter(x=df2.Date, y=df2['impressions'],
                        mode='lines+markers',
                        name='Impressions')
    trace_2 = go.Scatter(x=df2.Date, y=df2['engagement rate'],
                        mode='lines+markers',
                        name='Engagement rate')
    trace_3 = go.Scatter(x=df2.Date, y=df2['detail expands'],
                        mode='lines+markers',
                        name='Detail expands')
    trace_4 = go.Scatter(x=df2.Date, y=df2['likes'],
                        mode='lines+markers',
                        name='Likes')
    trace_5 = go.Scatter(x=df2.Date, y=df2['media views'],
                        mode='lines+markers',
                        name='Media views')
    trace_6 = go.Scatter(x=df2.Date, y=df2['media engagements'],
                        mode='lines+markers',
                        name='Media engagements')
    fig1 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6], layout=twitterLayout)
    return fig1

# second section -- Facebook ------------------------------------------------

@app.callback(Output('g9', 'figure'), [Input('slider-two', 'value'), Input('slider-two', 'marks')])
def update_graph_2(X, dates):

    dates = list(dates.values())

    df2 = df1[(df1.Date >= dates[X[0]]) & (df1.Date <= dates[X[1]])]
    trace_1 = go.Scatter(x=df2.Date, y=df2['Lifetime Post Total Reach'],
                                mode='lines+markers',
                                name='Lifetime Post Total Reach')
    trace_2 = go.Scatter(x=df2.Date, y=df2['Lifetime Post Total Impressions'],
                                mode='lines+markers',
                                name='Lifetime Post Total Impressions')
    trace_3 = go.Scatter(x=df2.Date, y=df2['Lifetime Engaged Users'],
                                mode='lines+markers',
                                name='Lifetime Engaged Users')
    trace_4 = go.Scatter(x=df2.Date, y=df2['Lifetime Matched Audience Targeting Consumers on Post'],
                                mode='lines+markers',
                                name='Lifetime Targeting Consumers on Post')
    trace_5 = go.Scatter(x=df2.Date, y=df2['Lifetime Matched Audience Targeting Consumptions on Post'],
                                mode='lines+markers',
                                name='Lifetime Targeting Consumptions on Post')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5], layout=facebookLayout)
    return fig2

# third section -- LinkedIn ------------------------------------------------

@app.callback(Output('g10', 'figure'), [Input('slider-three', 'value'), Input('slider-three', 'marks')])
def update_graph_3(X, dates):

    dates = list(dates.values())

    new_data = df4[(df4.Date >= dates[X[0]]) & (df4.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=df4['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=df4['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=df4['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=df4['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=df4['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=df4['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=df4['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=df4['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)
    return fig2

if __name__ == '__main__':
    app.run_server(debug=True)
