# %%
# import some packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import seaborn as sns

# creat a pandas Data Frame from training data
df = pd.read_csv('train_FD001.txt', sep=' ', header=None)
df = df.drop(columns=[26, 27])

# rename the columns
data_header = {0: 'Engine', 1: 'Cycle', 2: 'Altitude', 3: 'MachNumber', 4: 'TRA', 5: 'T2', 6: 'T24', 7: 'T30', 8: 'T50',
               9: 'P2', 10: 'P15', 11: 'P30', 12: 'Nf', 13: 'Nc', 14: 'epr', 15: 'Ps30', 16: 'phi', 17: 'NRf',
               18: 'NRc', 19: 'BPR', 20: 'farB', 21: 'htBleed', 22: 'Nf_dmd', 23: 'PCNfR_dmd', 24: 'W31', 25: 'W32'}

df = df.rename(columns=data_header)

describe = df.describe()

# %%
# plot a histogram for each sensor
fig = plt.figure(figsize=[15, 20])
sensor_number = 1

for param in df.columns[5:26]:
    sbp = plt.subplot(7, 3, sensor_number)
    df[param].hist()
    sbp.set_title(param)
    plt.tight_layout()
    sensor_number += 1

plt.show()
#%%
# selecting only the sensor data
sensor_data = df.iloc[:,5:26] # df.iloc[rows,columns]

# only evaluate correlations on sensor data that is not constant
sensor_data = sensor_data.drop(['T2', 'P2', 'P15', 'epr', 'farB', 'Nf_dmd', 'PCNfR_dmd'], axis=1)
correlation = sensor_data.corr(method='pearson')
#%%
# creating a heatmap with seaborn package
fig = plt.figure(figsize=[10,10])
sb.heatmap(correlation, vmin=-1, vmax=1, center=0, cmap='seismic', annot=True)

plt.show()
