import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
# df = pd.read_csv("UNSW_NB15_testing-set.csv", header=None)
# print(df)
# print(df[3])
# df.to_csv("filenext.csv")

miss_va = pd.read_csv("miss_value.csv",header=None)
x = miss_va.values #convert thanh mang
print(miss_va)
imp = Imputer(missing_values=np.nan, strategy="most_frequent")
imp.fit(x)
result = imp.transform(x)
print(result)
