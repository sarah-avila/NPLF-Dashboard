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
from pages import year2020, year2021, year2022, year2023, year2024
from dash.dependencies import Input, Output
import numpy as np


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'NashvillePLFoundation@gmail.com': 'Foundation2018'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# Excel Sheets -----------------------

# Twitter
df_twitter_2020 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx')
df_twitter_2021 = pd.read_excel('NPLF Twitter 2021.xlsx')
df_twitter_2022 = pd.read_excel('NPLF Twitter 2022.xlsx')
df_twitter_2023 = pd.read_excel('NPLF Twitter 2023.xlsx')
df_twitter_2024 = pd.read_excel('NPLF Twitter 2024.xlsx')

# Facebook
df_facebook_2020 = pd.read_excel('Facebook Posts Q1andQ2.xlsx')
df_facebook_2021 = pd.read_excel('FacebookPosts2021.xlsx')
df_facebook_2022 = pd.read_excel('FacebookPosts2022.xlsx')
df_facebook_2023 = pd.read_excel('FacebookPosts2023.xlsx')
df_facebook_2024 = pd.read_excel('FacebookPosts2024.xlsx')

# LinkedIn
df_linkedin_2020 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Update metrics (aggregated)')
df_linkedin_2021 = pd.read_excel('NPLF Linkedin 2021.xlsx', sheet_name = 'Update metrics (aggregated)')
df_linkedin_2022 = pd.read_excel('NPLF Linkedin 2022.xlsx', sheet_name = 'Update metrics (aggregated)')
df_linkedin_2023 = pd.read_excel('NPLF Linkedin 2023.xlsx', sheet_name = 'Update metrics (aggregated)')
df_linkedin_2024 = pd.read_excel('NPLF Linkedin 2024.xlsx', sheet_name = 'Update metrics (aggregated)')


# Twitter Layout
twitterLayout = go.Layout(
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


# Facebook Layout
facebookLayout = go.Layout(
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



# LinkedIn Layout
linkedinLayout = go.Layout(
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
                            

# default rangeslider/graph values
min_value = '2020-01-01'
max_value = '2021-01-01'
dates = pd.date_range(min_value, max_value, freq='MS').strftime("%Y-%b").tolist()
print("dateee", dates)
date_mark = {i: dates[i] for i in range(0, 13)}


# navbar definitions
NPLF_LOGO = "https://nplf.org/content/uploads/2016/01/logo.png"
HELP_DOC = "https://docs.google.com/document/d/1y3fmjIyPUOn91nWUKN5uu8ILPQiEXNRv2yqhxcBHE1I/edit?pli=1"

logo_navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=NPLF_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Nashville Public Library Foundation", href="https://nplf.org/", className="ml-2")),
                    dbc.Col(dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Years", header=True),
                            dbc.DropdownMenuItem("2020", href='/pages/year2020'),
                            dbc.DropdownMenuItem("2021", href='/pages/year2021'),
                            dbc.DropdownMenuItem("2022", href='/pages/year2022'),
                            dbc.DropdownMenuItem("2023", href='/pages/year2023'),
                            dbc.DropdownMenuItem("2024", href='/pages/year2024'),
                        ],
                        label="Years",
                        color="light", 
                        className="m-1",
                    ), style={'margin-left' :'1000px', 'margin-right' : '50px'}),
                    dbc.Col(dbc.Button("Help", href=HELP_DOC, color="light", className="mr-1"),)  
                ],
                align="center",
                no_gutters=True,
            ),
        ),
    ],
    dark=True,
    color="darkblue",
    sticky="top", 
)

# app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    logo_navbar,
    html.Div(id='page-content'),
])


# page navigation ---------------------------------------------------------

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/year2021':
        return year2021.app.layout
    elif pathname == '/pages/year2022':
        return year2022.app.layout
    elif pathname == '/pages/year2023':
        return year2023.app.layout
    elif pathname == '/pages/year2024':
        return year2024.app.layout
    else:
        return year2020.app.layout

#                                                 ---------------------- 2020 PAGE -------------------------

# first section -- Twitter -----------------------

@app.callback(Output('twitter_2020', 'figure'), [Input('twitter-2020', 'value'), Input('twitter-2020', 'marks')])
def update_graph(X, dates):

    dates = list(dates.values())

    df2 = df_twitter_2020[(df_twitter_2020.Date >= dates[X[0]]) & (df_twitter_2020.Date <= dates[X[1]])]
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

# second section -- Facebook -----------------------

@app.callback(Output('facebook_2020', 'figure'), [Input('facebook-2020', 'value'), Input('facebook-2020', 'marks')])
def update_graph_2(X, dates):

    dates = list(dates.values())

    df2 = df_facebook_2020[(df_facebook_2020.Date >= dates[X[0]]) & (df_facebook_2020.Date <= dates[X[1]])]
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

# third section -- LinkedIn -----------------------

@app.callback(Output('linkedin_2020', 'figure'), [Input('linkedin-2020', 'value'), Input('linkedin-2020', 'marks')])
def update_graph_3(X, dates):

    dates = list(dates.values())

    new_data = df_linkedin_2020[(df_linkedin_2020.Date >= dates[X[0]]) & (df_linkedin_2020.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=new_data['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=new_data['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)

    return fig2

#                                                 ---------------------- 2021 PAGE -------------------------

# first section -- Twitter -----------------------

@app.callback(Output('twitter_2021', 'figure'), [Input('twitter-2021', 'value'), Input('twitter-2021', 'marks')])
def update_graph_4(X, dates):

    dates = list(dates.values())

    df2 = df_twitter_2021[(df_twitter_2021.Date >= dates[X[0]]) & (df_twitter_2021.Date <= dates[X[1]])]
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

# second section -- Facebook -----------------------

@app.callback(Output('facebook_2021', 'figure'), [Input('facebook-2021', 'value'), Input('facebook-2021', 'marks')])
def update_graph_5(X, dates):

    dates = list(dates.values())

    df2 = df_facebook_2021[(df_facebook_2021.Date >= dates[X[0]]) & (df_facebook_2021.Date <= dates[X[1]])]
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

# third section -- LinkedIn -----------------------

@app.callback(Output('linkedin_2021', 'figure'), [Input('linkedin-2021', 'value'), Input('linkedin-2021', 'marks')])
def update_graph_6(X, dates):

    dates = list(dates.values())

    new_data = df_linkedin_2021[(df_linkedin_2021.Date >= dates[X[0]]) & (df_linkedin_2021.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=new_data['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=new_data['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)

    return fig2

#                                                 ---------------------- 2022 PAGE -------------------------

# first section -- Twitter -----------------------

@app.callback(Output('twitter_2022', 'figure'), [Input('twitter-2022', 'value'), Input('twitter-2022', 'marks')])
def update_graph_7(X, dates):

    dates = list(dates.values())

    df2 = df_twitter_2022[(df_twitter_2022.Date >= dates[X[0]]) & (df_twitter_2022.Date <= dates[X[1]])]
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

# second section -- Facebook -----------------------

@app.callback(Output('facebook_2022', 'figure'), [Input('facebook-2022', 'value'), Input('facebook-2022', 'marks')])
def update_graph_8(X, dates):

    dates = list(dates.values())

    df2 = df_facebook_2022[(df_facebook_2022.Date >= dates[X[0]]) & (df_facebook_2022.Date <= dates[X[1]])]
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

# third section -- LinkedIn -----------------------

@app.callback(Output('linkedin_2022', 'figure'), [Input('linkedin-2022', 'value'), Input('linkedin-2022', 'marks')])
def update_graph_9(X, dates):

    dates = list(dates.values())

    new_data = df_linkedin_2022[(df_linkedin_2022.Date >= dates[X[0]]) & (df_linkedin_2022.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=new_data['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=new_data['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)

    return fig2

#                                                 ---------------------- 2023 PAGE -------------------------

# first section -- Twitter -----------------------

@app.callback(Output('twitter_2023', 'figure'), [Input('twitter-2023', 'value'), Input('twitter-2023', 'marks')])
def update_graph_10(X, dates):

    dates = list(dates.values())

    df2 = df_twitter_2023[(df_twitter_2023.Date >= dates[X[0]]) & (df_twitter_2023.Date <= dates[X[1]])]
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

# second section -- Facebook -----------------------

@app.callback(Output('facebook_2023', 'figure'), [Input('facebook-2023', 'value'), Input('facebook-2023', 'marks')])
def update_graph_11(X, dates):

    dates = list(dates.values())

    df2 = df_facebook_2023[(df_facebook_2023.Date >= dates[X[0]]) & (df_facebook_2023.Date <= dates[X[1]])]
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

# third section -- LinkedIn -----------------------

@app.callback(Output('linkedin_2023', 'figure'), [Input('linkedin-2023', 'value'), Input('linkedin-2023', 'marks')])
def update_graph_12(X, dates):

    dates = list(dates.values())

    new_data = df_linkedin_2023[(df_linkedin_2023.Date >= dates[X[0]]) & (df_linkedin_2023.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=new_data['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=new_data['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)

    return fig2

#                           ---------------------- 2024 PAGE -------------------------
# first section -- Twitter -----------------------
@app.callback(Output('twitter_2024', 'figure'), [Input('twitter-2024', 'value'), Input('twitter-2024', 'marks')])
def update_graph_7(X, dates):

    dates = list(dates.values())

    df2 = df_twitter_2024[(df_twitter_2024.Date >= dates[X[0]]) & (df_twitter_2024.Date <= dates[X[1]])]
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
# second section -- Facebook -----------------------

@app.callback(Output('facebook_2024', 'figure'), [Input('facebook-2024', 'value'), Input('facebook-2024', 'marks')])
def update_graph_11(X, dates):

    dates = list(dates.values())

    df2 = df_facebook_2024[(df_facebook_2024.Date >= dates[X[0]]) & (df_facebook_2024.Date <= dates[X[1]])]
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

# third section -- LinkedIn -----------------------

@app.callback(Output('linkedin_2024', 'figure'), [Input('linkedin-2024', 'value'), Input('linkedin-2024', 'marks')])
def update_graph_12(X, dates):

    dates = list(dates.values())

    new_data = df_linkedin_2024[(df_linkedin_2024.Date >= dates[X[0]]) & (df_linkedin_2024.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (organic)'],
                                mode='lines+markers',
                                name= 'Impressions (organic)')
    trace_2 = plot.Scatter(x=new_data.Date, y=new_data['Impressions (sponsored)'],
                                mode='lines+markers', name='Impressions (sponsored)')
    trace_3 = plot.Scatter(x=new_data.Date, y=new_data['Unique impressions (organic)'],
                                mode='lines+markers', name='Unique impressions (organic)')
    trace_4 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (organic)'],
                                mode='lines+markers', name='Clicks (organic)')
    trace_5 = plot.Scatter(x=new_data.Date, y=new_data['Clicks (sponsored)'],
                                mode='lines+markers', name='Clicks (sponsored)')
    trace_6 = plot.Scatter(x=new_data.Date, y=new_data['Reactions (organic)'],
                                mode='lines+markers', name='Reactions (organic)')
    trace_7 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (organic)'],
                                mode='lines+markers', name='Engagement rate (organic)')
    trace_8 = plot.Scatter(x=new_data.Date, y=new_data['Engagement rate (sponsored)'],
                                mode='lines+markers', name='Engagement rate (sponsored)')
    fig2 = go.Figure(data=[trace_1, trace_2, trace_3, trace_4, trace_5, trace_6, trace_7, trace_8], layout=linkedinLayout)

    return fig2



if __name__ == '__main__':
    app.run_server(debug=True)
