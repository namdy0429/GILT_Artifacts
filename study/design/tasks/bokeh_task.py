from math import log, sqrt
import calendar
import numpy as np
import pandas as pd

from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

type_color = dict([
    ("Income",   "#277da1"),
    ("Expense",  "#f94144"),
    ("Profit",   "#43aa8b")
])

restaurants = ["Cafe", "Bistro", "Food Truck", "Pub"]

income_data = [[27, 31, 28, 80, 89, 90, 123, 186, 109, 241, 2, 68],
                [112, 153, 783, 889, 982, 929, 681, 785, 200, 281, 301, 287],
                [132, 85, 82, 133, 95, 92, 130, 109, 70, 71, 131, 90],
                [68, 64, 37, 52, 67, 43, 48, 33, 35, 44, 46, 59]]
expense_data = [[19, 18, 10, 40, 43, 44, 65, 87, 98, 132, 28, 43],
                [80, 92, 245, 315, 432, 472, 241, 358, 81, 83, 176, 135],
                [75, 50, 72, 33, 63, 45, 62, 79, 89, 91, 90, 73],
                [21, 20, 23, 24, 18, 16, 22, 26, 14, 17, 13, 28]]


headers = list(calendar.month_name)[1:]
plots = []

for i, restaurant in enumerate(restaurants):
    df = pd.DataFrame(columns=['Income', 'Expense'])
    data = {"Income": income_data[i],
            "Expense": expense_data[i]}

    df = pd.DataFrame(data)
    df["Profit"]  = df["Income"] - df["Expense"]
    df["Month"] = headers

    width = 800
    height = 800
    inner_radius = 90
    outer_radius = 300 - 10

    minr = 0
    maxr = 1000
    a = (outer_radius - inner_radius) / (maxr - minr)
    b = outer_radius - maxr * a

    def rad(y_val):
        return a * y_val + b

    big_angle = 2.0 * np.pi / (len(df) + 1)
    small_angle = big_angle / 7

    p = figure(width=width, height=height, title=restaurant,
        x_axis_type='auto', y_axis_type='auto',
        x_range=(-420, 420), y_range=(-420, 420),
        min_border=0, outline_line_color="black",
        background_fill_color="#f0e1d2")

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle
    p.annular_wedge(
        0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color="#aeaeb8"
    )

    p.annular_wedge(0, 0, inner_radius, rad(df.Income),
                    -big_angle+angles+5*small_angle, -big_angle+angles+6*small_angle,
                    color=type_color['Income'])
    p.annular_wedge(0, 0, inner_radius, rad(df.Expense),
                    -big_angle+angles+3*small_angle, -big_angle+angles+4*small_angle,
                    color=type_color['Expense'])
    p.annular_wedge(0, 0, inner_radius, rad(df.Profit),
                    -big_angle+angles+1*small_angle, -big_angle+angles+2*small_angle,
                    color=type_color['Profit'])

    labels = np.arange(0, 1050, 100)
    radii = a * labels + b
    p.circle(0, 0, radius=radii, fill_color=None, line_color="white")

    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                    -big_angle+angles, -big_angle+angles, color="black")

    xr = radii[-1]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[-1]*np.sin(np.array(-big_angle/2 + angles))
    label_angle=np.array(-big_angle/2+angles)
    label_angle[label_angle < -np.pi/2] += np.pi 
    p.text(xr, yr, df.Month, angle=label_angle,
        text_font_size="12px", text_align="left", text_baseline="middle")

    p.rect([-40, -40, -40], [18, 0, -18], width=30, height=13,
        color=list(type_color.values()))
    p.text([-15, -15, -15], [18, 0, -18], text=list(type_color),
        text_font_size="12px", text_align="left", text_baseline="middle")

    plots.append(p)

grid = gridplot(plots, ncols=1, width=500, height=500)
show(grid)