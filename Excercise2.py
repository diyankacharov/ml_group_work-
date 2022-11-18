import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# %%
# read text file
url = 'https://git.rwth-aachen.de/jonas.schulte/ml_group_work/-/raw/LsgNicholas/Data/train_FD001.txt'

data = pd.read_csv(url, sep=" ", header=None,
                   names=["Engine", "Cycle", "Altitude", "MachNumber", "TRA", "T2", "T24", "T30", "T50", "P2", "P15",
                          "P30", "Nf", "Nc", "epr", "Ps30", "phi", "NRf", "NRc", "BPR", "farB", "htBleed", "Nf_dmd",
                          "PCNfR_dmd", "W31", "W32", "NaN", "NaN2"])

df = data.drop(columns=["NaN", "NaN2"])

# %%
fig = plt.figure(figsize=[15,20])
sensor_number = 1
for param in df.columns[5:27]:
    sbp = plt.subplot(7,3,sensor_number)
    df[param].hist()
    sbp.set_title(param)
    plt.tight_layout()
    sensor_number+=1

fig.show()
# %%
description = df.describe()
# Columns 1:5 are not sensor data
# sensors T2, P2, P15, Nf, epr, NRf, BPR, farB, Nf_dmd, PCNfR_dmd are constant
# %%


# %%
sensor_data = df.iloc[:, 5:26]
sensor_data = sensor_data.drop(columns= ['T2', 'P2', 'P15', 'epr', 'farB', 'Nf_dmd', 'PCNfR_dmd'])

# %%