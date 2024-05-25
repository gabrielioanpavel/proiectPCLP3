import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from examine import *
from plots import *

df = pd.read_csv('Titanic Dataset/train.csv')

# Examinare dataframe
print(f"Date generale despre dataframe:\n{listData(df)}\n")
print(f"Procentaje supravietuitori (da/nu): \n{prcS(df)}\n")
print(f"Procentaje clase pasageri: {prcPclass(df)}\n")
print(f"Procentaje sexe: {prcSex(df)}\n")

# Construire grafice pentru procentaje
pies(df)

# Construire histograme
histograms(df)

print(f"Coloane cu valori lipsa:\n{np.matrix(nullCols(df))}\n")
print(f"Procente valori lipsa pentru supravietuitori:\n{np.matrix(prcNullCols(df))}\n")

ageList, ages = detAges(df)
df.insert(6, "Age category", ages)
agesPlot(df, ageList)