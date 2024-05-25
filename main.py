import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from examine import *
from plots import *

df = pd.read_csv('Titanic Dataset/train.csv')

# Examinare dataframe
print(listData(df))
print(prcS(df))
print(prcPclass(df))
print(prcSex(df))

# Construire grafice pentru procentaje
pies(df)

# Construire histograme
histograms(df)

print(nullCols(df))
print(prcNullCols(df))