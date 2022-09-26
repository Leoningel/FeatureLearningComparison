from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import global_vars as gv


data = pd.read_csv("data/daily_website_visitors/daily_website_visitors3.csv", delimiter=gv.DELIMITER)
data[['Visits']] = data[['target']].astype(float)
data[['Day']] = data[['instant']]

# -----------------------------

number_map = {
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
        7 : "Saturday",
        1 : "Sunday",
    }
data = data.sort_values(by='Day.Of.Week')
data[['bla']] = data[['Day.Of.Week']]
data.bla = data.bla.map(number_map)
data[['Day of the week']] = data[['bla']]

g = sns.barplot(
            x='Day of the week',
            y='Visits',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

for item in g.get_xticklabels():
            item.set_rotation(25)
g.set_title(f"Visits per day of the week")
path = f"plots/website_visitors/data_analysis/visits_per_day.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

number_map = {
        1   : "January",
        2   : "February",
        3   : "March",
        4   : "April",
        5   : "May",
        6   : "June",
        7   : "July",
        8   : "August",
        9   : "September",
        10  : "October",
        11  : "November",
        12  : "December",
    }
data = data.sort_values(by='Month')
data.Month = data.Month.map(number_map)

g = sns.barplot(
            x='Month',
            y='Visits',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

for item in g.get_xticklabels():
            item.set_rotation(25)
g.set_title(f"Visits per month")
path = f"plots/website_visitors/data_analysis/visits_per_month.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

