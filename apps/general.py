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
        dbc.Button("Overview", href="/apps/second"),
        dbc.Button("Reach", href="/apps/second"),
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
    sticky_navbar,
    badge,
    vertical_navbar,
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


        html.Div([
            html.Div([
                html.H3('Facebook Advertising'),
                dcc.Graph(
                    id='g1',
                    figure=fig1)], 
            className="heading"),

            html.Div([
                html.H3('Facebook Reach'),
                dcc.Graph(
                    id='g2', figure=fig2)], 
            className="heading"),
        ], 
        className="row top"),

        html.Div([
            html.Div([
                html.H3('Google Analytics'),
                dcc.Graph(
                    id='g3',
                    figure=fig3)],
            className="heading"),

            html.Div([
                html.H3('Twitter Reach'),
                dcc.Graph(
                    id='g4', 
                    figure=fig4)], 
                    className="heading")],
            className="row"),

        html.Div([
            html.Div([
                html.H3('LinkedIn Reach'),
                dcc.Graph(
                    id='g5',
                    figure=fig5)],
            className="heading"),

            html.Div([
                html.H3('Email Marketing'),
                dcc.Graph(
                    id='g6', 
                    figure=fig6)], 
            className="heading")],
        className="row"),

        html.Div([
            html.H5('Source: Nashville Public Library Foundation Official Records')
        ], className="source")
    ], 
    className="container"),
])

# Step 5. Add callback functions
@app.callback(Output('g7', 'figure'),
             [Input('slider', 'value')])
def update_figure(X):
    df2 = df[(df.Date >= dates[X[0]]) & (df.Date <= dates[X[1]])]
    trace_1 = plot.Scatter(x = df2.Date, y = df2['Google Analytics'],
                        name = 'Google Analytics',
                        line = dict(width = 2,
                                    color = '#00cc96'))
    trace_2 = plot.Scatter(x = df2.Date, y = df2['Facebook Advertising'],
                        name = 'Facebook Advertising',
                        line = dict(width = 2,
                                    color = '#FF5733'))
    trace_3 = plot.Scatter(x = df2.Date, y = df2['Facebook Reach'],
                        name = 'Facebook Reach',
                        line = dict(width = 2,
                                    color = '#D7BDE2'))
    trace_4 = plot.Scatter(x = df2.Date, y = df2['Twitter Reach'],
                        name = 'Twitter Reach',
                        line = dict(width = 2,
                                    color = '#9467bd'))
    trace_5 = plot.Scatter(x = df2.Date, y = df2['LinkedIn Reach'],
                        name = 'LinkedIn Reach',
                        line = dict(width = 2,
                                    color = '#ffa15a'))
    trace_6 = plot.Scatter(x = df2.Date, y = df2['Email Marketing'],
                        name = 'Email Marketing',
                        line = dict(width = 2,
                                    color = '#1cd3f3'))
    fig = plot.Figure(data = [trace_1, trace_2, trace_3, trace_4, trace_5, trace_6], layout = layout)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
