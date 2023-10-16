import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv("Top 30 Country.csv")

df.set_index("Date", inplace=True)

# print(df.head())

# print(df.dtypes)

df = df.cumsum(axis=0)

# df.to_csv("Top 30 Countries Cummulative Sum.csv")

bcr.bar_chart_race(
    df=df,
    bar_size=0.90,
    period_length=250,
    period_label={"x": 0.99, "y": 0.30, "ha": "right", "va": "center"},
    period_summary_func=lambda v, r: {
        "x": 0.99,
        "y": 0.18,
        "s": f"Total Immigrants: {v.nlargest(30).sum():,.0f}",
        "ha": "right",
        "size": 8,
    },
    figsize=(7, 5),
    cmap="accent",
    title="Immigrants to Canada by Country",
    title_size="medium",
    bar_label_size=6,
    tick_label_size=7,
    bar_kwargs={"alpha": 0.5},
)
