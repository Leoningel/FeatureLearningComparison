from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import global_vars as gv


data = pd.read_csv("data/credit_g.csv", delimiter=gv.DELIMITER)
data[['Risk']] = data[['target']].astype(str)
data[['Time instant']] = data[['instant']]

# -----------------------------

g = sns.countplot(
            x='Risk',
            data=data,
            # shrink=.8,
            order=["0", "1"],
            )

g.set_xticks([0, 1])
g.set_title(f"Risk distribution")
path = f"plots/credit/input_data_analysis/credit_distribution.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

data[['Risk']] = data[['target']]

# -----------------------------

number_map = {
        0 : "No history",
        1 : "Good",
        2 : "Fine",
        3 : "Not good",
        4 : "Bad",
    }
data = data.sort_values(by='credit_history')
data.credit_history = data.credit_history.map(number_map)
data[['Credit history']] = data[['credit_history']]

g = sns.barplot(
            x='Credit history',
            y='Risk',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

g.set_title(f"Risk for credit history")
path = f"plots/credit/input_data_analysis/risk_for_credit_hist.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

number_map = {
        0 : "Unemployed",
        1 : "Unskilled",
        2 : "Skilled",
        3 : "Highly-skilled",
    }
data = data.sort_values(by='job')
data.job = data.job.map(number_map)
data[['Job']] = data[['job']]

g = sns.barplot(
            x='Job',
            y='Risk',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

g.set_title(f"Risk for jobs")
path = f"plots/credit/input_data_analysis/risk_for_jobs.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

number_map = {
        0 : "Rent",
        1 : "Own",
        2 : "For free",
    }
data = data.sort_values(by='housing')
data.housing = data.housing.map(number_map)
data[['Housing']] = data[['housing']]

g = sns.barplot(
            x='Housing',
            y='Risk',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

g.set_title(f"Risk for housing")
path = f"plots/credit/input_data_analysis/risk_for_housing.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------

number_map = {
        0 : "Male divorced",
        1 : "Female",
        2 : "Male single",
        3 : "Male married",
        4 : "Female single",
    }
data = data.sort_values(by='personal_status')
data.personal_status = data.personal_status.map(number_map)
data[['Personal status']] = data[['personal_status']]
# divorced_men = data[data['Personal status'] == "Male divorced"]
# women = data[data['Personal status'] == "Female divorced/married"]
# single_men = data[data['Personal status'] == "Male single"]
# married_men = data[data['Personal status'] == "Male married"]
# print(f"Average risk divorced men: {divorced_men[['target']].sum()/len(divorced_men[['target']].values)}")
# print(f"Average risk women: {women[['target']].sum()/len(women[['target']].values)}")
# print(f"Average risk single men: {single_men[['target']].sum()/len(single_men[['target']].values)}")
# print(f"Average risk married men: {married_men[['target']].sum()/len(married_men[['target']].values)}")

g = sns.barplot(
            x='Personal status',
            y='Risk',
            data=data,
            ci=None,
            # multiple='dodge',
            # shrink=.8,
            # order=["0", "1"],
            )

g.set_title(f"Risk for Personal status")
path = f"plots/credit/input_data_analysis/risk_for_personal_status.pdf"
plt.savefig(path)
print(f"Saved figure to {path}.")
plt.close()

# -----------------------------


