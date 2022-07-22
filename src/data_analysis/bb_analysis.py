from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import global_vars as gv


data = pd.read_csv("data/boom_bikes_14-01-2022-RAW.csv", delimiter=gv.DELIMITER)
data[['Bike count']] = data[['cnt']]
data[['Time instant']] = data[['instant']]
            
a = sns.lineplot(
            data=data,
            x = 'Time instant',
            y = 'Bike count',
            )

a.set_title(f"Bike count over time")
path = f"plots/bb/input_data_analysis/cnt_to_instant.pdf"
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
data.mnth = data.mnth.map(number_map)
data[['Month']] = data[['mnth']]

g = sns.boxplot(
            x='Month',
            y='Bike count',
            data=data
            )

for item in g.get_xticklabels():
            item.set_rotation(25)
g.set_title(f"Bike count per month")
path = f"plots/bb/input_data_analysis/bikes_per_month.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

number_map = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tueday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
    }
data.weekday = data.weekday.map(number_map)
data[['Day of the week']] = data[['weekday']]

g = sns.boxplot(
            x='Day of the week',
            y='Bike count',
            data=data
            )

for item in g.get_xticklabels():
            item.set_rotation(25)
g.set_title(f"Bike count per day of the week")
path = f"plots/bb/input_data_analysis/bikes_per_weekday.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

data[['Working day']] = data[['workingday']]

g = sns.boxplot(
            x='Working day',
            y='Bike count',
            data=data
            )

g.set_title(f"Bike count on working days")
path = f"plots/bb/input_data_analysis/bikes_per_workingday.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

data[['Holiday']] = data[['holiday']]

g = sns.boxplot(
            x='Holiday',
            y='Bike count',
            data=data
            )

g.set_title(f"Bike count on holidays")
path = f"plots/bb/input_data_analysis/bikes_per_holiday.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()




