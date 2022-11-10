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
