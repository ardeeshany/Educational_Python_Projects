# Data Wrangling
# base + {pandas}

import seaborn as sns
import pandas as pd
data = sns.load_dataset("penguins")

# data info
pd.set_option("display.max_columns", 4)
data.transpose()
pd.set_option("display.max_columns", 10**6)

data.head()
data.info()
data.describe()

data.dtypes
data.shape

data.columns
data.index

data.values


# Arrange ---------------------------------------------------
## dplyr::arrange()
data.sort_values(['bill_depth_mm', 'bill_length_mm'], 
  ascending=[False, True])


# column selection ------------------------------------------
## dplyr::select()
data
data.bill_depth_mm # = data['bill_depth_mm']
data[['bill_depth_mm']] # a DataFrame with 1 column
data[['bill_depth_mm', 'species']]  # reorder column

fav_cols = ['species', 'sex']
data[fav_cols]
data[data.columns.difference(fav_cols)]


data.loc[:, 'bill_depth_mm']; data.loc[:, ['bill_depth_mm']]
data.iloc[:, 3]; data.iloc[:, [1]] ; data.iloc[:, 0:2] 

# a logical vector for columns
is_cols_in = (data.dtypes == 'float64').values
data.loc[:, is_cols_in] #check with conditions with length = number of cols

# detect a pattern for creating a logical vector
col_logs = [('bill' in i) for i in data.columns]
data.loc[:, col_logs]

# select columns with a condition on .all() or .any() on rows
num_data_cols = data.columns[data.dtypes == 'float64']
data2 = data.loc[:, num_data_cols]
col_logs = [(data2[cols] > 100).any() for cols in num_data_cols]
data2.loc[:, col_logs]

# detect a pattern using .str
col_logs = data.columns.str.contains('s') # startswith, endswith, isnumeric
data.loc[:, col_logs]




# Row Filteration ---------------------------------------
## dplyr::filter()

row_logs1 = data.bill_depth_mm > 15                  # numeric
row_logs2 = data.species.str.startswith('Ad')        # string
row_logs3 = data.island.isin(['Torgersen', 'Dream']) # categorical
row_logs4 = row_logs1 & row_logs2

data.loc[row_logs, :]



# create a new column
## dplyr::mutate()

data["new"] = 2 # Add a new col
data["new3"] = 2 # Add a new col
data["new2"] = data["new"] + data.bill_depth_mm + min(data.bill_length_mm)



# group by and summarise
## dplyr::group_by() + dplyr::summarise()
data_nonmiss = data.dropna()
data_nonmiss.groupby('sex')['bill_length_mm'].max()
summarise_data = data_nonmiss.groupby(['species', 'sex'])[['bill_length_mm']].agg([np.mean, np.max])
summarise_data.iloc[:, 3]


## summarise without groupby
data_nonmiss.bill_depth_mm.agg([np.min, np.mean, np.max])

## pivot_table
## Special format to visualize a groupby(+2 var) + summarise
data_nonmiss.pivot_table(values="bill_length_mm",
                         index= ["species"],
                         columns="sex",
                         aggfunc=np.mean,
                         margins=True)


# data cleaning and dealing with missing values
## tidyr::drop_na(); dplyr::distinct()
data.drop_duplicates(subset=['new', 'new3'])
data.sex.unique()
data.sex.value_counts(normalize=True, dropna=False)


data.isna()              # missing = NaN
data.isna().any()        # if there is at least one missing values
data.isna().sum()        # num of missing values for each column

data.dropna()            # at least one row value is zerp
data.dropna(how = 'all') # all row values are na
data.dropna(axis = 'columns') # columns with at least one na values

data.fillna("Missing")




# working with indexes
## ~ rownames
data.index
data = data.set_index('species')
data = data.set_index(['species', 'sex'])
# data = data.reset_index()

data.sort_index(ascending=[False, True])

