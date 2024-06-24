import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#################### Read data ####################

data_path = 'medical_examination.csv'

try:
    with open(data_path, 'r') as f:
        first_line = f.readline().strip()
except FileNotFoundError:
    print(f"Error: File '{data_path}' not found!")
    exit()

column_names = first_line.split(',')

df = pd.read_csv(data_path, names=column_names, skiprows=1)

#################### Functions ####################

def bmi(weight, height):
    BMI = weight / (height ** 2)
    return 0 if BMI < 25 else 1

def normalise(data):
    if data == 1:
        return 0
    if data > 1:
        return 1
    raise ValueError("Wrong data - should be 1 or more")

def clean_and_filter_data(df):
    cleaned_df = df[df['ap_lo'] <= df['ap_hi']]
    cleaned_df = cleaned_df.dropna(subset=['ap_lo', 'ap_hi'])
    
    height_lower_quantile = cleaned_df['height'].quantile(0.025)
    height_upper_quantile = cleaned_df['height'].quantile(0.975)
    weight_lower_quantile = cleaned_df['weight'].quantile(0.025)
    weight_upper_quantile = cleaned_df['weight'].quantile(0.975)
    
    filtered_df = cleaned_df[(cleaned_df['height'] >= height_lower_quantile) & 
                             (cleaned_df['height'] <= height_upper_quantile) & 
                             (cleaned_df['weight'] >= weight_lower_quantile) & 
                             (cleaned_df['weight'] <= weight_upper_quantile)]
    
    filtered_df = filtered_df.reset_index(drop=True)
    return filtered_df

df = clean_and_filter_data(df)

#################### Manipulating Data ####################

df["overweight"] = df.apply(lambda row: bmi(row['weight'], row["height"] / 100), axis=1)
df["cholesterol"] = df["cholesterol"].apply(lambda x: normalise(x))
df["gluc"] = df["gluc"].apply(lambda x: normalise(x))


corr = df.corr()

#################### Generate a mask for the upper triangle ####################
mask = np.triu(np.ones_like(corr, dtype=bool))

#################### Set up the matplotlib figure ####################
fig, ax = plt.subplots(figsize=(11, 9))

#################### Plot the heatmap ####################
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, ax=ax)

plt.savefig('heatmap.png')
plt.show()

#################### Draw functions ####################

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    fig.savefig('catplot.png')

    return fig

draw_cat_plot()
