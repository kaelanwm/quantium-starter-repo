from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

#Load your data
df = pd.read_csv(r"C:\Users\Owner\Onedrive\03_Coding\quantium-starter-repo\data\pink_morsel_sales.csv")

# Clean the sales column by removing $ and converting to float
df["sales"] = df["sales"].replace('[\\$,]', '', regex=True).astype(float)

# see https://plotly.com/python/px-arguments/ for more options
df = df.sort_values("date")
    
# Create a line chart
Fig = px.line(df, x="date", y="sales", title="Soul Foods Sales Over Time")
Fig.update_layout(xaxis_title='Date', yaxis_title='Sales')

app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Analysis'),

    html.Div(children='''
        Analyzing sales before and after the Pink Morsel Price Increase (January 15,2021)
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=Fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)