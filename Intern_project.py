
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

#reading the csv file using pandas
df = pd.read_csv("passenger.csv")
print(df.head(7))

df.dropna(axis=0,inplace=True)
print(df)

print(df.info())
print(df.describe())

df.plot(x ='Date', y='School', kind='line'),
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

Corr_Matrix = round(df.corr(),2)
print(Corr_Matrix)