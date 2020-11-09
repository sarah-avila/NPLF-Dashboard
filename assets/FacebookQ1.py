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


excel_file = '../Facebook Posts Q1.xlsx'
df = pd.read_excel(excel_file)
print(df)

fig = make_subplots(rows=4, cols=2, column_widths=[0.5, 0.5],
                    subplot_titles=("Lifetime Post Total Reach","Lifetime Post Total Reach","Lifetime Post Paid Reach",
                                    "Lifetime Post Total Impressions","Lifetime Post Organic Impressions","Lifetime Post Paid Impressions",
                                    "Lifetime Engaged Users","Lifetime Matched Audience Targeting Consumptions on Post"))



fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Post Total Reach'], mode='lines+markers', line_color="#9467bd"),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Post Paid Reach'], mode='lines+markers', line_color="#9467bd"),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Post Total Impressions'], mode='lines+markers', line_color="#9467bd"),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Post Organic Impressions'], mode='lines+markers', line_color="#9467bd"),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Post Paid Impressions'], mode='lines+markers', line_color="#9467bd"),
    row=3, col=2
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Engaged Users'], mode='lines+markers', line_color="#9467bd"),
    row=4, col=1
)
fig.add_trace(
    go.Scatter(x=df['Posted'] , y = df[ 'Lifetime Matched Audience Targeting Consumptions on Post'], mode='lines+markers', line_color="#9467bd"),
    row=4, col=2
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
        text="Facebook Page Quarter 1",
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
