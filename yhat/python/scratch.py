'''
Created on Feb 1, 2015

@author: kruser
'''
import pandas as pd
df = pd.read_csv('/users/kruser/git/stats-scratchpad/yhat/data/cs-training.csv')
pd.value_counts(df.NumberOfDependents).plot(kind='bar')