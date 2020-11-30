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


excel_file = 'NPLF Twitter Q1andQ2.xlsx'
#df = pd.read_excel(excel_file)
df = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = [0,1,2,3,4,5])
df2 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter April')
df3 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter May')
df4 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter June')
df5 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter July')
df6 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter August')
df7 = pd.read_excel('NPLF Twitter Q1andQ2.xlsx', sheet_name = 'NPLF Twitter September')
print(df)

#fig = make_subplots(rows=2, cols=2, column_widths=[0.5, 0.5],
#                    subplot_titles=("Engagements in April", "Engagements in May", "engagements in June",))

fig1 = px.bar(df2, x=df2.Date, y=df2.engagements, title = "Engagements in April")


fig2 = px.bar(df3, x=df3.Date, y=df3.engagements, title = "Engagements in May")


fig3 = px.bar(df4, x=df4.Date, y=df4.engagements, title = "Engagements in June")


fig4 = px.bar(df2, x=df2.Date, y=df2.likes, title = "Likes in April")


fig5 = px.bar(df3, x=df3.Date, y=df3.likes, title = "Likes in May")


fig5 = px.bar(df4, x=df4.Date, y=df4.likes, title = "Likes in June")


fig6 = px.bar(df2, x=df2.Date, y=df2.impressions, title = "Impressions in April")


fig7 = px.bar(df3, x=df3.Date, y=df3.impressions, title = "Impressions in May")


fig8 = px.bar(df4, x=df4.Date, y=df4.impressions, title = "Impressions in June")

trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]
trace4 = fig4['data'][0]
trace5 = fig5['data'][0]
trace6 = fig6['data'][0]
trace7 = fig7['data'][0]
trace8 = fig8['data'][0]

fig = make_subplots(rows=8, cols=1, shared_xaxes=False,  subplot_titles=("Engagements in April", "Engagements in May", "Engagements in June", "Likes in April", "Likes in May", "Likes in June", "Impressions in April" , "Impressions in May", "Impressions in June" ))
fig.update_layout(height=2700, width=1300, title_text="Twitter")
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=2, col=1)
fig.add_trace(trace3, row=3, col=1)
fig.add_trace(trace4, row=4, col=1)
fig.add_trace(trace5, row=5, col=1)
fig.add_trace(trace6, row=6, col=1)
fig.add_trace(trace7, row=7, col=1)
fig.add_trace(trace8, row=8, col=1)

fig.show()




#fig.add_trace(
#    go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#9467bd"),
#    row=1, col=2
#)
#fig.add_trace(
#   go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#ef5a41"),
#    row=2, col=1
#)
#fig.add_trace(
#    go.Scatter(x=df['Date'] , y = df[ 'engagements'], mode='lines+markers', line_color="#ef5a41"),
 #   row=2, col=2
#)




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

