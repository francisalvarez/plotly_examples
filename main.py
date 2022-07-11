import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def load_data():
    dat = pd.read_csv('sample.csv')
    return dat

def create_figure(df, x_col, y_cols, color_list):
    fig = go.Figure()
    for ii, y_col in enumerate(y_cols):
        color = color_list[ii]
        fig.add_trace(
            go.Line(
                x=df[x_col], y=df[y_col], mode='lines+markers', name=y_col, color=color[ii]
            )
        )
    return fig

def create_plotly_color_pallete(n_values, color_pallette_name):
    """
    https://stackoverflow.com/questions/68081450/how-to-create-discrete-colormap-with-n-colors-using-plotly
    color_pallette_name: Plasma
    """
    colors = px.colors.sample_colorscale(color_pallette_name, [n / (n_values - 1) for n in range(n_values)])
    return colors

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dat = load_data()
    # fig = px.line(dat, x="county", y="segment_1")
    # plot(fig)

    x_col = 'county'
    y_cols = ['segment_1', 'segment_2', 'segment_3']
    col_pallete = create_plotly_color_pallete(len(y_cols), "Plasma")
    fig = create_figure(dat, x_col, y_cols, col_pallete)
    fig.update_layout(template='plotly_white')
    plot(fig)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
