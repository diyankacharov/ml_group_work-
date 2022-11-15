import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
# read text file
url = 'https://git.rwth-aachen.de/jonas.schulte/ml_group_work/-/raw/LsgNicholas/Data/train_FD001.txt'

data = pd.read_csv(url, sep=" ", header=None,
                   names=["Engine", "Cycle", "Altitude", "MachNumber", "TRA", "T2", "T24", "T30", "T50", "P2", "P15",
                          "P30", "Nf", "Nc", "epr", "Ps30", "phi", "NRf", "NRc", "BPR", "farB", "htBleed", "Nf_dmd",
                          "PCNfR_dmd", "W31", "W32", "NaN", "NaN2"])


# print out data as well as basic statistical information
# print(data.describe(percentiles=[.25, .5, .75]))
print(data)
#%%
# create a second data frame which only includes the operating conditions
# op_conditions = data[["Engine", "Cycle", "Altitude", "MachNumber", "TRA"]]


# print(op_conditions.describe(percentiles=[.25, .5, .75]))

#
# plot the distribution of different operational parameters
# plt.scatter(op_conditions[["Cycle"]],op_conditions[["Altitude"]])
# plt.scatter(op_conditions[["Cycle"]],op_conditions[["MachNumber"]])
# plt.scatter(op_conditions[["Engine"]],op_conditions[["Altitude"]])
# plt.scatter(op_conditions[["Engine"]],op_conditions[["MachNumber"]])
# plt.scatter(op_conditions[["Engine"]],op_conditions[["TRA"]])
# The assumption of constant operating conditions is fulfilled since there are only slight deviances which can be
# attributed to rounding errors (&numerical)
#

# gets data from one engine and returns a dataframe
def get_engine_data(df, engine):
    d = df.loc[df["Engine"] == engine]
    add_rul(d)
    return d
    # return df.loc[df["Engine"] == engine]


# add the remaining cycles as a column
def add_rul(df):
    length = df.shape[0]
    rul = []
    for a in range(length):
        rul.append((length - a - 1) * -1)
    df.insert(2, "RUL", rul, True)


# plots the data of a provided selection of engines
#x_var is usually "Cycle" or "RUL"; y_var can be any of the sensors
def plotdata(df, x_var, y_var, engine_selection):
    for i in engine_selection:
        engine_data = get_engine_data(df, i)
        plt.plot(engine_data[[x_var]], engine_data[[y_var]])

    plt.show()


# plotdata(data, "RUL", "T50", range(0, 10))
def corrolate(df, var1, var2, engine_no):
    enginedat = get_engine_data(df, engine_no)
    x = enginedat[var1]
    y = enginedat[var2]
    print(x.corr(y))


def show_distribution(df):
    verteilung = []
    j = max(data["Engine"]) + 1
    for i in range(1, j):
        en = get_engine_data(df, i)
        verteilung.append(en.shape[0])
    print(verteilung)
    plt.hist(x=verteilung, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.xlabel('Maximum number of Cycles')
    plt.ylabel('Number of Engines')
    plt.title('Distribution of Lifetime')
    plt.show()

# max(data["Engine"])

show_distribution(data)

