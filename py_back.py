# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# %%
df_b = pd.read_csv('ipl_ball_by_ball.csv')
df_o = pd.read_csv('ipl_matches.csv')


# %%
df_o.columns


# %%
df_o.head()

# %% [markdown]
# At this point we now know that our data is loaded well. 
# Let's check out the analysis we can perform :
# For example, I want to see which umpires have featured the most

# %%
fig, ax = plt.subplots()
df_o['umpire1'].value_counts().plot(ax=ax, kind='barh', color='red')
ax.invert_yaxis()
fig.set_size_inches(12, 8)
fig.savefig('umpire1_frequency.png', dpi=100)


# %%
fig, ax = plt.subplots()
df_o['umpire2'].value_counts().plot(ax=ax, kind='barh', color='green')
ax.invert_yaxis()
fig.set_size_inches(12, 8)
fig.savefig('umpire2_frequency.png', dpi=100)


# %%
fig, ax = plt.subplots()
count_umpires = df_o.groupby(['umpire1', 'umpire2']).size() 
count_umpires = count_umpires.sort_values(ascending=False)
count_umpires_t5 = count_umpires.head(10)
count_umpires_t5.plot(ax=ax, color='blue', kind='barh')
ax.invert_yaxis()
fig.set_size_inches(12, 8)
fig.savefig('umpire_pair_frequency.png', dpi=100)

# %% [markdown]
# In case it is not apparent already, the last graph represents the most featured pairs among umpires throughout the history of IPL.
# Surprisingly enough, the top 2 umpires in individual category are not fielded together much.

