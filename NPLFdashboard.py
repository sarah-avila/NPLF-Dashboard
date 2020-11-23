import plotly
import plotly.graph_objects as go
import pandas as pd

excel_file = 'Facebook Page Q2.xlsx'
df = pd.read_excel(excel_file)
print(df)
data = [go.Scatter( x=df['Date'] , y = df[ 'Daily Page Engaged Users'])]
fig = go.Figure(data)
fig.show()
