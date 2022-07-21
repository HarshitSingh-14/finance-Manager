from math import pi

import pandas as pd
from bokeh.embed import components
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Blues256, Category20c
from bokeh.plotting import figure , output_file, show
from bokeh.themes import built_in_themes
from bokeh.transform import cumsum, factor_cmap
from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar
import pandas as pd

# Resolve..


# http://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vbar.html#bokeh.models.VBar   -> need sol
def plot_bar_chart(x, y_o):
    print(x)
    y=[]
    for count, ele in enumerate(y_o):
        y.append(count)
    source = ColumnDataSource(dict(x=x, top=y))
    # Add plot
    p = Plot(
        # title="ExpensesVsCategory",
        plot_width=1000,
        # x_axis_label="Amount",
    )
    # Render glyph
    blues = []
    for i in range(15):
        blues.append(Blues256[i * 16])
    glyph=VBar(
        x="x",
        top="top",
        bottom=0,
        width=0.5,
        fill_color="#b3de69",
        source=source,
    )
    p.add_glyph(source, glyph)
    #
    xaxis = LinearAxis()
    p.add_layout(xaxis, 'below')

    yaxis = LinearAxis()
    p.add_layout(yaxis, 'left')

    p.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    p.add_layout(Grid(dimension=1, ticker=yaxis.ticker))



    # p.x_range.start = 0
    p.add_tools(HoverTool(tooltips=[("CATEGORY", "@y"), ("AMOUNT", "@right{1.11}")]))

    curdoc().add_root(p)
    script, div = components(p)

    return (script, div)








# https://docs.bokeh.org/en/latest/docs/gallery/pie_chart.html
def plot_pie_chart(x):

    curdoc().theme = "dark_minimal"


    data = pd.Series(x).reset_index(name="value").rename(columns={"index": "category"})
    data["angle"] = data["value"] / data["value"].sum() * 2 * pi
    # Colour out of range
    if len(x) > 2:
        data["color"] = Category20c[len(x)]
    elif len(x) > 1:
        data["color"] = ["#3182bd", "#e6550d"]
    else:
        data["color"] = ["#3182bd"]

    p = figure(
        plot_width=1000,
        title="Expense Vs Item Pie Chart",
        tools="hover",
        tooltips="@category: @value{1.11}",
        x_range=(-0.5, 1.0),
    )


    p.wedge(
        x=0,
        y=1,
        radius=0.4,
        start_angle=cumsum("angle", include_zero=True),
        end_angle=cumsum("angle"),
        line_color="white",
        fill_color="color",
        legend_field="category",
        source=data,
    )
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    curdoc().add_root(p)
    script, div = components(p)
    return (script, div)

