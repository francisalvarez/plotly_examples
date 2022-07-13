import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

class PlotlyTemplate:
    def __init__(self,
                 xaxis_title, yaxis_title, title, legend_title,
                 font_family="calibri",
                 font_color="black",
                 layout='plotly_white',
                 ):
        self.color_palette = ["#003f5c",
                              "#2f4b7c",
                              "#665191",
                              "#a05195",
                              "#d45087",
                              "#f95d6a",
                              "#ff7c43",
                              "#ffa600"
                              ]

        self.layout_config = {'template': layout,
                              'xaxis_title': xaxis_title,
                              'yaxis_title': yaxis_title,
                              'title': title,
                              'legend_title': legend_title,
                              'font_family': font_family,
                              'font_color': font_color,
        }

        def format_tick_labels(fig):
            # percent
            fig.update_layout(yaxis_tickformat=',.0%')
            # get rid of "k" in thousandths
            fig.update_layout(yaxis_tickformat='000')


if __name__ == "__main__":

    df = pd.DataFrame(
        {'name': ['a1', 'a2', 'a3'],
         'price': [35000, 40000, 30000],
         'base': [5000, 1000, 2000]}
    )
    df['price_rel'] = 1
    df['base_rel'] = df['base'] / df['price']


    pl = PlotlyTemplate(xaxis_title='MSRP',
                        yaxis_title='Dollars ($)',
                        title='Insert Title Here',
                        legend_title='Legend Title Here',
                        font_family="calibri",
                        font_color="black",
                        )
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['name'],
                         y=df['price'],
                         name='Price',
                         marker_color=pl.color_palette[0]
                         ))
    fig.add_trace(go.Bar(x=df['name'],
                         y=df['base'],
                         name='Base',
                         marker_color=pl.color_palette[1]
                         ))

    # Add annotation
    for idx, r in df.iterrows():
        fig.add_annotation(x=r['name'], y=r['price'], text=r['price'], bgcolor="white",
                           font=dict(color=pl.color_palette[0]),
                           xshift=-2, yshift=0, xanchor="right", showarrow=False)

    fig.update_layout(**pl.layout_config)
    fig.update_layout(yaxis_tickformat='000')
    plot(fig)