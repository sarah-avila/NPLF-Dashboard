import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server
import dash_bootstrap_components as dbc

nav_menu= dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pages", header=True),
                dbc.DropdownMenuItem("Page 1", href="/page-a"),
                dbc.DropdownMenuItem("Page 1", href="/page-b"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    nav_menu,

    html.Div( [html.Div( [html.H6('A')], id = 'page-a' ),
               html.Div( [html.H6('B')], id = 'page-b' )],
              style = {'display': 'block'})
])