import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

if __name__ == "__main__":
    side_by_side_bar = False
    stacked_bar = False
    relative_bar = True

    df = pd.DataFrame(
        {'name': ['a1', 'a2', 'a3'],
         'price': [35000, 40000, 30000],
         'base': [5000, 1000, 2000]}
    )
    df['price_rel'] = 1
    df['base_rel'] = df['base'] / df['price']

    if side_by_side_bar:
        fig = go.Figure(data=[
            go.Bar(name='base', x=df['name'], y=df['base'], marker_color='green'),
            go.Bar(name='price', x=df['name'], y=df['price'], marker_color='orange')
        ])
        # Change the bar mode
        fig.update_layout(barmode='group',
                          template='plotly_white')
        fig.update_xaxes(title='Categories')
        fig.update_yaxes(title='Price ($)')
        fig.show()

    if stacked_bar:

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['name'],
                             y=df['price'],
                             name='Price',
                             marker_color='green'
                             ))
        fig.add_trace(go.Bar(x=df['name'],
                             y=df['base'],
                             name='Base',
                             marker_color='orange'
                             ))
        fig.update_layout(title="Title",
                          barmode='overlay',
                          template='plotly_white')
        fig.update_xaxes(title='Categories')
        fig.update_yaxes(title='Price ($)')
        plot(fig)

    if relative_bar:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['name'],
                             y=df['price_rel'],
                             name='Price',
                             marker_color='green'
                             ))
        fig.add_trace(go.Bar(x=df['name'],
                             y=df['base_rel'],
                             name='Base',
                             marker_color='orange'
                             ))
        fig.update_layout(title="Title",
                          barmode='overlay',
                          template='plotly_white')
        fig.update_xaxes(title='Categories')
        fig.update_yaxes(title='Price ($)', tickformat= ',.0%')
        plot(fig)