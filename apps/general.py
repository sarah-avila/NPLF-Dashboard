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

df = pd.read_excel('Temporary Dataset -- VandyHacks Summer 2020.xlsx')

layout = plot.Layout(
    title="Facebook"
)

fig1 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Advertising'], mode='lines+markers', ))
fig2 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Facebook Reach'], mode='lines+markers', line_color="#ef5a41"))
fig3 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Google Analytics'], mode='lines+markers', line_color="#00cc96"))
fig4 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Twitter Reach'], mode='lines+markers', line_color="#9467bd"))
fig5 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['LinkedIn Reach'], mode='lines+markers', line_color="#ffa15a"))
fig6 = plot.Figure(data=plot.Scatter(x=df['Date'], y=df['Email Marketing'], mode='lines+markers', line_color="#1cd3f3"))
fig7 = plot.Figure()

fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Advertising'],
                    mode='lines+markers',
                    name='Facebook Advertising'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Facebook Reach'],
                    mode='lines+markers', name='Facebook Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Google Analytics'],
                    mode='lines+markers', name='Google Analytics'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Twitter Reach'],
                    mode='lines+markers', name='Twitter Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['LinkedIn Reach'],
                    mode='lines+markers', name='LinkedIn Reach'))
fig7.add_trace(plot.Scatter(x=df['Date'], y=df['Email Marketing'],
                    mode='lines+markers', name='Email Marketing'))


# navbar definition
sticky_navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Time Frame", header=True),
                dbc.DropdownMenuItem("Weekly", href="#"),
                dbc.DropdownMenuItem("Monthly", href="#"),
                dbc.DropdownMenuItem("Quarterly", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Overview",
        ),
        dbc.NavItem(dbc.NavLink("MoM", href="#")),
        dbc.NavItem(dbc.NavLink("Summary", href="#")),
    ],
    brand="Nashville Public Library Foundation",
    color="dark",
    dark=True,
    sticky="top",
)


badge = html.Div(
    [
       dbc.Badge("NPLF Marketing Dashboard"),
    ],
    className="badge",
)

# button group definitions
vertical_navbar = dbc.ButtonGroup(
    [
        dcc.Link("Overview", href="/second"),
        dbc.Button("Reach", href="/third"),
        dbc.Button("Impressions"),
        dbc.Button("Visits"),
        dbc.Button("Leads"),
        dbc.Button("Customers by Marketing"),
        dbc.Button("Conversions"),
        
    ],
    vertical=True,
    className="navbar-vertical",
)

# date slider labels
df['Date'] = pd.to_datetime(df.Date)
dates = ['05-01-2020', '05-04-2020', '05-07-2020', '05-10-2020', '05-13-2020']
date_mark = {i : dates[i] for i in range(0, 5)}

# horizontal_navbar = dbc.ButtonGroup(
#     [
#          dbc.DropdownMenu(
#             [dbc.DropdownMenuItem("Weekly"), dbc.DropdownMenuItem("Monthly"), dbc.DropdownMenuItem("Quarterly")],
#             label="Overview",
#             group=True,
#         ),
#         dbc.Button("MoM"),
#         dbc.Button("Summary"),
        
#     ],
#     className="navbar-horizontal",
# )

# app and layout definition
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.Div([
        html.Div([
                html.H3('Summary of May 1 - 13, 2020'),
                dcc.Graph(
                    id='g7',
                    figure=fig7,
            )], className="heading top"),


        # range slider
                html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'slider',
                                    marks = date_mark,
                                    min = 0,
                                    max = 4,
                                    value = [0, 4]) 
                        ], style = {'width' : '100%',
                                    'fontSize' : '20px',
                                    'padding-left' : '360px',
                                    'display': 'inline-block'}),
    ], className="container"), 
])

if __name__ == '__main__':
    app.run_server(debug=True)