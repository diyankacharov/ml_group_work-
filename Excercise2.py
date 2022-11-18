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

data = data.drop(columns=["NaN", "NaN2"])


plt.figure()
data[['Altitude']].boxplot()
plt.figure()
data[["MachNumber"]].boxplot()


# %%