import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly.graph_objects as go
import plotly
from plotly.subplots import make_subplots


excel_file = 'Facebook Page Q2.xlsx'
df = pd.read_excel(excel_file)
print(df)

fig = make_subplots(rows=3, cols=2, column_widths=[0.5, 0.5],
                    subplot_titles=("Weekly Total Impressions", "Weekly Page Engaged Users", "Weekly Viral Reach",
                                    "Weekly Reach of Page Posts","Weekly Organic impressions","Weekly Page Consumptions"))



fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Weekly Page Engaged Users'], mode='lines+markers', line_color="#9467bd"),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Weekly Viral Reach'], mode='lines+markers', line_color="#ef5a41"),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Weekly Reach Of Page Posts'], mode='lines+markers', line_color="#ef5a41"),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Weekly Organic impressions'], mode='lines+markers', line_color="#ef5a41"),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Weekly Page Consumptions'], mode='lines+markers', line_color="#ef5a41"),
    row=3, col=2
)

fig.update_layout(
autosize=False,
    width=2000,
    height=1500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=20
    ),
    paper_bgcolor="LightSteelBlue",
    title=go.layout.Title(
        text="Facebook Page Quarter 2",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Daily Page Engaged Users",
            font=dict(
                family="Comissioner, sans-serif",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Date",
            font=dict(
                family="Comissioner, sans-serif",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)
fig.show()



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


app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
            html.H3('Facebook Page Quarter 2'),
            dcc.Graph(
                id='g7',
                figure=data,
        )], className="heading bottom"),

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

    # html.Div([
    #         html.H3('Summary'),
    #         dcc.Graph(
    #             id='g7',
    #             figure=fig7,
    #     )], className="heading bottom"),

    html.Div([
        html.H5('Source: Nashville Public Library Foundation Official Records')
    ], className="source")
],  className="container",)

if __name__ == "__main__":
    app.run_server(debug=True)
