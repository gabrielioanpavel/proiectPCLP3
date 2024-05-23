import pandas as pd
from examine import *

df = pd.read_csv('Titanic Dataset/train.csv')
print(listData(df))