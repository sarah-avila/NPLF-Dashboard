import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as plot
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

from app import app
from app import server 
from apps import second, third, general

# app and layout definition
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('General', href='/apps/general'),
        dcc.Link('Second Page', href='/apps/second'),
        dcc.Link('Third Page', href='/apps/third'),
    ], className="row"),
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/second':
        return second.app.layout
    if pathname == '/apps/third':
        return third.app.layout
    else:
        return general.app.layout

if __name__ == '__main__':
    app.run_server(debug=True)
