import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read in data
private_df = pd.read_csv('private_ev_charging.csv')
public_df = pd.read_csv('public_ev_charging.csv')
sales_df = pd.read_csv('ev_sales.csv')

# merge tables to keep rows with complete information
merged_df = private_df.merge(public_df, how='outer', indicator=True)
merged_df = merged_df[merged_df['_merge'] == 'both']
merged_df.drop(columns=['_merge'], inplace=True)

merged_df = merged_df.merge(sales_df, how='left', on='year')
merged_df.groupby('year')['sales'].sum()

# number of vehicles sold in 2018
ev_sales_2018 = 361315

# trends between public ports, private ports and sales
fig, ax = plt.subplots()
sns.lineplot(data=merged_df, x='year', y='private_ports', label='Private Ports')
sns.lineplot(data=merged_df, x='year', y='public_ports', label='Public Ports')
sns.lineplot(data=merged_df, x='year', y='sales', label='Total Sales', linestyle='--')

ax.set_title('EV Ports and Sales Over Time')
ax.set(xlabel='Year', ylabel='Count')

plt.show()
