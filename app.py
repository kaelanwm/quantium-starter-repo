from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

#Load your data
df = pd.read_csv(r"C:\Users\Owner\Onedrive\03_Coding\quantium-starter-repo\data\pink_morsel_sales.csv")


# see https://plotly.com/python/px-arguments/ for more options
df = df.sort_values("date")
    

app.layout = html.Div(style={'backgroundColor': '#1e3a5f', 'padding': '20px'}, children=[
    html.H1(children='Soul Foods Sales Analysis', style={'color': 'white'}),

    html.Div(children='''
        Analyzing sales before and after the Pink Morsel Price Increase (January 15, 2021)
    ''', style={'color': 'white'}),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        style={'color': 'white'}
    ),

    dcc.Graph(id='sales-graph')
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)

def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(filtered_df, x='date', y='sales', title='Soul Foods Sales Over Time')
    fig.update_traces(line_color='#2ecc71')  # Green line
    fig.update_layout(
        xaxis_title='Date', 
        yaxis_title='Sales',
        paper_bgcolor='#1e3a5f',  # Background behind chart
        plot_bgcolor='#1e3a5f',   # Chart area background
        font_color='white'        # All text white
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)