# %%
# import some packages
import pandas as pd
import matplotlib.pyplot as plt
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
sensor_data = df.iloc[:, 5:26]

# only evaluate correlations on sensor data that is not constant
sensor_data = sensor_data.drop(['T2', 'P2', 'P15', 'epr', 'farB', 'Nf_dmd', 'PCNfR_dmd'], axis=1)
correlation = sensor_data.corr(method='pearson')
#%%
# creating a heatmap with seaborn package
fig = plt.figure(figsize=[12, 10])
sns.heatmap(correlation, vmin=-1, vmax=1, center=0, cmap='seismic', annot=True)

plt.show()
#%%
# calculate maximum cycles per engine

df_max_cycles = df[['Engine', 'Cycle']].groupby(['Engine']).max()

df_max_cycles = df_max_cycles.rename(columns={'Cycle': 'Max_Cycles'})

# plot histogram
df_max_cycles.hist(column=['Max_Cycles'])

fig1 = plt.figure()
df_max_cycles.boxplot(column=['Max_Cycles'])
#%%
# merge the max_cycles value to the dataframe
df_rul = df.merge(df_max_cycles, left_on='Engine', right_index=True)

# calculation of remaining useful life

df_rul['RUL'] = df_rul['Max_Cycles'] - df_rul['Cycle']


df_rul.head()
#%%
# Calculate the correlation
target_correlation = df_rul.corr(method='pearson')  # you could also use spearman
target_correlation = target_correlation.loc['RUL']
#%%
target_corr_spear = df_rul.corr(method='spearman')
target_corr_spear = target_corr_spear.loc['RUL']
#%%
# plot the course of the sensors Ps30 and phi for the first three engines
n_engines = 3

plt.figure(figsize=(15, 5))
sbp = plt.subplot(1, 2, 1)
for jj in range(1, 1+n_engines):
    df_rul_jj = df_rul[df_rul['Engine'] == jj]
    plt.plot(df_rul_jj['Cycle'], df_rul_jj['Ps30'])
    plt.legend(range(1, 1+n_engines))
    plt.xlabel('Cycles')
    plt.ylabel('Ps30')

sbp = plt.subplot(1, 2, 2)
for jj in range(1, 1+n_engines):
    df_rul_jj = df_rul[df_rul['Engine'] == jj]
    plt.plot(df_rul_jj['RUL'], df_rul_jj['Ps30'])
    plt.legend(range(1, 1+n_engines))
    plt.xlabel('RUL')
    plt.ylabel('Ps30')

plt.figure(figsize=(15, 5))

sbp = plt.subplot(1, 2, 1)
for jj in range(1, 1+n_engines):
    df_rul_jj = df_rul[df_rul['Engine'] == jj]
    plt.plot(df_rul_jj['Cycle'], df_rul_jj['phi'])
    plt.legend(range(1, 1+n_engines))
    plt.xlabel('Cycles')
    plt.ylabel('phi')

sbp = plt.subplot(1, 2, 2)
for jj in range(1, 1+n_engines):
    df_rul_jj = df_rul[df_rul['Engine'] == jj]
    plt.plot(df_rul_jj['RUL'], df_rul_jj['phi'])
    plt.legend(range(1, 1+n_engines))
    plt.xlabel('RUL')
    plt.ylabel('phi')
#%%
# scatter plots to visualize the correlation between the sensors and the RUL

plt.figure()
plt.scatter(df_rul['Ps30'], df_rul['RUL'])
plt.xlabel('Ps30')
plt.ylabel('RUL')


plt.figure()
plt.scatter(df_rul['phi'], df_rul['RUL'])
plt.xlabel('phi')
plt.ylabel('RUL')
#%%
# correlation for the first 100 cycles for sensor Ps30
df_rul_start = df_rul[df_rul['Cycle'] <= 100]

df_rul_start_RUL = df_rul_start['RUL']
df_rul_start_Ps30 = df_rul_start['Ps30']
corr_start = df_rul_start_RUL.corr(df_rul_start_Ps30)

# correlation for the last 100 cycles for sensor Ps30
df_rul_end = df_rul[df_rul['RUL'] <= 100]

df_rul_end_RUL = df_rul_end['RUL']
df_rul_end_Ps30 = df_rul_end['Ps30']
corr_end = df_rul_end_RUL.corr(df_rul_end_Ps30)
