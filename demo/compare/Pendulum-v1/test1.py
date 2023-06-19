import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['axes.unicode_minus'] = False

data = {
    0: pd.read_csv("PPO.csv", usecols=['Step', 'Value']),
    1: pd.read_csv("SCAPPO.csv", usecols=['Step', 'Value']),
    2: pd.read_csv("DDPG.csv", usecols=['Step', 'Value']),
    3: pd.read_csv("TRPO.csv", usecols=['Step', 'Value']),
}

label = ['PPO', 'DDPG', 'SCAPPO', 'TRPO']

df = []
for i in range(len(data)):
    df.append(pd.DataFrame(data[i]))
    df[i]['algo'] = label[i]
df = pd.concat(df)
df.index = range(len(df))


# def smooth(data, sm=1):
#     smooth_data = []
#     if sm > 1:
#         for d in data:
#             z = np.ones(len(d))
#             y = np.ones(sm) * 1.0
#             d = np.convolve(y, d, "same") / np.convolve(y, z, "same")
#             smooth_data.append(d)
#     return smooth_data
#
#
# df = smooth(df, 20)

sns.lineplot(x='Step', y='Value', hue="algo", data=df, style="algo", err_style="band")
plt.xlabel('Episode', fontsize=12)
plt.ylabel('Ten episodes average rewards', fontsize=12)
plt.show()
