import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from collections import Counter
from examine import *
from plots import *

def fillEmpty(df: pd.DataFrame):
    emp = nullColID(df)
    for col in emp:
        if df[col].dtype != object:
            df1 = df[df['Survived'] == 1]
            avgA = df1[col].sum() / df1[col].count()
            df1 = df[df['Survived'] == 0]
            avgD = df1[col].sum() / df1[col].count()
            for index, row in df.iterrows():
                if pd.isnull(row[col]):
                    if row['Survived'] == 1:
                        df.at[index, col] = avgA
                    else:
                        df.at[index, col] = avgD
                    pass
        else:
            df1 = df[df['Survived'] == 1]
            x = np.array(df1[col])
            freq = Counter(x)
            del freq[np.nan]
            avgA = max(freq, key=freq.get)
            df1 = df[df['Survived'] == 0]
            x = np.array(df1[col])
            freq = Counter(x)
            del freq[np.nan]
            avgD = max(freq, key=freq.get)
            for index, row in df.iterrows():
                if pd.isnull(row[col]):
                    if row['Survived'] == 1:
                        df.at[index, col] = avgA
                    else:
                        df.at[index, col] = avgD

df = pd.read_csv('../../Titanic Dataset/train.csv')

# Examinare dataframe
print(f"Date generale despre dataframe:\n{listData(df)}\n")
print(f"Procentaje supravietuitori (da/nu): \n{prcS(df)}\n")
print(f"Procentaje clase pasageri(C1/C2/C3): {prcPclass(df)}\n")
print(f"Procentaje sexe (Barbati/Femei): {prcSex(df)}\n")

# Construire grafice pentru procentaje
pies(df)

# Construire histograme
histograms(df)

print(f"Coloane cu valori lipsa:\n{np.matrix(nullCols(df))}\n")
print(f"Procente valori lipsa pentru supravietuitori:\n{np.matrix(prcNullCols(df))}\n")

ageList, ages = detAges(df)
print(f'Numar de pasageri pe categorii de varsta: {ageList}\n')
df.insert(6, "Age category", ages)
df.to_csv('../Date/cerinta5.csv')
agesPlot(df, ageList)

print(f"Numarul de barbati supravietuitori (in functie de categoria de varsta): {detMaleSurv(df)}\n")
maleSurvivalRate(df)

print(f"Procentul de copii aflati la bord este de {prcChildren(df)}%.\n")
caSurvialRate(df)

print(f'Fiecare coloana cu numarul de valori nenule, inainte de completare:\n{df.count()}\n')
fillEmpty(df)
df.to_csv('../Date/cerinta8.csv')
print(f'Fiecare coloana cu numarul de valori nenule, dupa completare:\n{df.count()}\n')

ok = titles(df)
if ok == len(df):
    print('Toate titlurile corespund cu sexul persoanei respective.\n')
else:
    print('Nu toate titlurile corespund cu sexul persoanei respective.')
titleGenderPlot(df)

sa, sf = familySurvival(df)
print(f'{sa}% din oamenii care au fost singuri au supravietuit')
print(f'{sf}% din oamenii care au fost cu familia au supravietuit')
print('Concluzie: oamenii care au fost cu familia au avut sanse putin mai mari de supravietuire')

tcsPlot(df)
print('Analizand graficul, putem observa ca, pentru primii 100 de pasageri, tariful a crescut cu clasa, iar cei mai multi supravietuitori sunt in clasa a doua.')