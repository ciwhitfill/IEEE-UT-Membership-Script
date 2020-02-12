# %%
import pandas as pd
# %%
DUES = pd.read_csv('data/Dues.csv')
SPARK = pd.DataFrame()
# %%
for index, person in DUES.iterrows():
    print(person['EID'].lower())


# %%
