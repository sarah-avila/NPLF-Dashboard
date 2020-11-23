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


excel_file = 'NPLF LinkedIn Q1.xlsx'
#df = pd.read_excel(excel_file)

df = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = [0,1,2,3,4])
df1 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Company size')
df3 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Update metrics (aggregated)')
df2 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Industry')
df4 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Seniority')

print(df)

#fig = make_subplots(rows=2, cols=2, column_widths=[0.5, 0.5],
#                    subplot_titles=("Engagements in April", "Engagements in May", "engagements in June",))


fig1 = px.bar(df2, y=df2.Industry, x=df2["Total views"], )
fig2 = px.bar(df3, x=df3.Date, y=df3["Impressions (total)"])
fig3 = px.bar(df3, x=df3.Date, y=df3["Impressions (organic)"])
fig4 = px.bar(df3, x=df3.Date, y=df3["Reactions (total)"])
fig5 = px.bar(df3, x=df3.Date, y=df3["Reactions (organic)"])
fig6 = px.bar(df3, x=df3.Date, y=df3["Comments (total)"])
fig7 = px.bar(df3, x=df3.Date, y=df3["Comments (organic)"])
fig8 = px.bar(df3, x=df3.Date, y=df3["Engagement rate (total)"])
fig9 = px.bar(df3, x=df3.Date, y=df3["Engagement rate (organic)"])
fig10 = px.bar(df1, y=df1["Total views"], x=df1["Company size"])
fig11 = px.bar(df4, y=df4["Total views"], x=df4["Seniority"])
#fig4.show()
#fig1 = go.Figure(data=[
#    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
#    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
#fig1.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', barmode ='group', title_text= 'Indsutry')
trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]
trace4 = fig4['data'][0]
trace5 = fig5['data'][0]
trace6 = fig6['data'][0]
trace7 = fig7['data'][0]
trace8 = fig8['data'][0]
trace9 = fig9['data'][0]
trace10 = fig10['data'][0]
trace11 = fig11['data'][0]


fig = make_subplots(rows=11, cols=1, shared_xaxes=False, subplot_titles=("Industry", "Impressions (total)", "Impressions (organic)", "Reactions (total)", "Reactions (organic)", "Comments (total)", "Comments (organic)", "Engagement rate (total)", "Engagement rate (organic)", "Company Size", "Seniority"))
fig.update_layout(height= 3500, width= 1200, title_text="Linkedin Quarter 1")
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=2, col=1)
fig.add_trace(trace3, row=3, col=1)
fig.add_trace(trace4, row=4, col=1)
fig.add_trace(trace5, row=5, col=1)
fig.add_trace(trace6, row=6, col=1)
fig.add_trace(trace7, row=7, col=1)
fig.add_trace(trace8, row=8, col=1)
fig.add_trace(trace9, row=9, col=1)
fig.add_trace(trace10, row=10, col=1)
fig.add_trace(trace11, row=11, col=1)
fig.show()
fig12 = plot.Figure()
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Impressions (total)'],
                    mode='lines+markers', line_color="#ef5a41",
                    name='Linkedin Activity Summary'))
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Reactions (total)'],
                    mode='lines+markers', line_color="#00cc96", name='Reactions (total)'))
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Industry'],
                    mode='lines+markers', line_color="#9467bd",name='Indsutry'))
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Engagement rate (total)'],
                    mode='lines+markers', line_color="#ffa15a", name='Engagement rate (total)'))
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Company size'],
                    mode='lines+markers', line_color="#1cd3f3", name='Company Size'))
fig12.add_trace(plot.Scatter(x=df['Date'], y=df['Comments (total)'],
                    mode='lines+markers', name='Comments (total)'))
fig12.show()




#fig4 = px.bar(df2, x=df2.Date, y=df2.Impressions(total), title = "Likes in April")
#fig4.show()






