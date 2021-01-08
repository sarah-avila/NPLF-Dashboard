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
from apps import general, second, third

## INSERT CODE
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
                dbc.DropdownMenuItem("Years", header=True),
                dbc.DropdownMenuItem("First", href='/apps/general'),
                dbc.DropdownMenuItem("Second", href='/apps/second'),
                dbc.DropdownMenuItem("Third", href='/apps/third'),
                dbc.DropdownMenuItem("Fourth", href="#"),
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
        dbc.Button("Overview", href='/apps/second'),
        dbc.Button("Reach", href='/apps/third'),
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
###

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sticky_navbar,
    badge,
    vertical_navbar,
    html.Div(id='page-content'),
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

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/second':
        return second.app.layout
    elif pathname == '/apps/third':
        return third.app.layout
    else:
        return general.app.layout

if __name__ == '__main__':
    app.run_server(debug=True)