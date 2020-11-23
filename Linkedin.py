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
df3 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Update metrics (aggregated)')
df2 = pd.read_excel('NPLF LinkedIn Q1.xlsx', sheet_name = 'Industry')

print(df)

#fig = make_subplots(rows=2, cols=2, column_widths=[0.5, 0.5],
#                    subplot_titles=("Engagements in April", "Engagements in May", "engagements in June",))


fig1 = px.bar(df2, y=df2.Industry, x=df2["Total views"], title = "Engagements in April")
fig2 = px.bar(df3, y=df3.Date, x=df3["Impressions (total)"], title = "Likes in April")
fig3 = px.bar(df3, y=df3.Date, x=df3["Reactions (total)"], title = "Likes in April")
#fig4.show()
#fig1 = go.Figure(data=[
#    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
#    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
#fig1.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', barmode ='group', title_text= 'Indsutry')
trace1 = fig1['data'][0]
trace2 = fig2['data'][0]
trace3 = fig3['data'][0]

fig = make_subplots(rows=3, cols=1, shared_xaxes=False)
fig.update_layout(height=3000, width=1200, title_text="Linkedin")
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=2, col=1)
fig.add_trace(trace3, row=3, col=1)

fig.show()




#fig4 = px.bar(df2, x=df2.Date, y=df2.Impressions(total), title = "Likes in April")
#fig4.show()






