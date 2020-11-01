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


excel_file = 'ConsolidatedLinkedin.xlsx'
df = pd.read_excel(excel_file)
print(df)

fig = make_subplots(rows=1, cols=2, column_widths=[0.5, 0.5])
fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Impressions(organic)'], mode='lines+markers', line_color="#ef5a41"),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['Date'] , y = df[ 'Impressions(total)'], mode='lines+markers', line_color="#9467bd"),
    row=1, col=2
)
fig.update_layout(
autosize=False,
    width=2000,
    height=500,
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
            text="",
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
                family="",
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

