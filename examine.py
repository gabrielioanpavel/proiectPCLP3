import pandas as pd
import matplotlib.pyplot as plt

def listData(df: pd.DataFrame) -> list:
    dataList = []
    dup = False
    dataList.append(len(df.columns))                # Numar de coloane
    dataList.append(len(df))                        # Numar de linii
    dataList.append([str(i) for i in df.dtypes])    # Lista cu tipuri de date
    dataList.append(sum(df.count()))                # Numar de valori lipsa
    for i in df.duplicated():
        if i == True:
            dup = False
            break
    dataList.append(dup)                            # Daca exista duplicate
    return dataList

# Procente supravietuitori
def prcS(df: pd.DataFrame):
    y = df['Survived'].sum()
    l = len(df['Survived'])
    return round(y/l*100, 2), round((l-y)/l*100, 2)

# Procente clase
def prcPclass(df: pd.DataFrame):
    c1 = sum(df['Pclass'] == 1)
    c2 = sum(df['Pclass'] == 2)
    c3 = sum(df['Pclass'] == 3)
    l = len(df['Pclass'])
    return round(c1/l*100, 2), round(c2/l*100, 2), round(c3/l*100, 2)

# Procente sexe
def prcSex(df: pd.DataFrame):
    m = sum(df['Sex'] == 'male')
    f = sum(df['Sex'] == 'female')
    l = len(df['Sex'])
    return round(m/l*100, 2), round(f/l*100, 2)