import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Identifica coloanele ce contin valori lipsa
def nullColID(df: pd.DataFrame):
    l = len(df)
    emp = []
    for col in df:
        nNulls = df[col].count()
        if nNulls == l:
            continue
        emp.append(col)
    return emp

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
    
# Procente valori lipsa pentru supravietuitori
def prcNullCols(df: pd.DataFrame):
    emp = nullColID(df)
    arr = []
    for col in emp:
        temp = []
        temp.append(col)
        l0 = l1 = n0 = n1 = 0
        for index, row in df.iterrows():
            if row['Survived'] == 0:
                l0 += 1
                if pd.isnull(row[col]):
                    n0 += 1
            else:
                l1 += 1
                if pd.isnull(row[col]):
                    n1 += 1
        temp.append(round(n0/l0*100, 2))
        temp.append(round(n1/l1*100, 2))
        arr.append(temp)
    return arr

# Calculeaza procentul de copii aflati la bord
def prcChildren(df: pd.DataFrame):
    c = sum(df['Age'] < 18)
    t = len(df)
    return round(c/t*100, 2)

# Numarul si proportia valorilor lipsa pentru fiecare coloana
def nullCols(df: pd.DataFrame):
    l = len(df)
    emp = nullColID(df)
    arr = []
    for col in emp:
        nNulls = df[col].count()
        temp = []
        nulls = l - nNulls
        temp.append(col)
        temp.append(nulls)
        temp.append(round(nulls/nNulls*100, 2))
        arr.append(temp)
    return arr

# Determina numarul de oameni incadrati in fiecare categorie de varsa si construieste
# o lista pentru a fi folosita in adaugarea noii coloane in dataframe
def detAges(df: pd.DataFrame):
    a1 = a2 = a3 = a4 = ukn = 0
    ages = []
    for index, row in df.iterrows():
        if pd.isnull(row['Age']):
            ukn += 1
            ages.append(np.nan)
            continue
        if row['Age'] <= 20:
            a1 += 1
            ages.append(0)
            continue
        if row['Age'] > 20 and row['Age'] <= 40:
            a2 += 1
            ages.append(1)
            continue
        if row['Age'] > 40 and row['Age'] <= 60:
            a3 += 1
            ages.append(2)
            continue
        if row['Age'] > 60:
            a4 += 1
            ages.append(3)
            continue
    return [a1, a2, a3, a4], ages

# Determina numarul de barbati supravietuitori
def detMaleSurv(df: pd.DataFrame):
    a1 = sum((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Age'] <= 20))
    a2 = sum((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Age'] > 20) & (df['Age'] <= 40))
    a3 = sum((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Age'] > 40) & (df['Age'] <= 60))
    a4 = sum((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Age'] > 60))
    return a1, a2, a3, a4

# Determina rata de supraviatuire a copiilor si a barbatilor
def detChildAdultSurvivalRate(df: pd.DataFrame):
    c = sum((df['Age'] < 18) & (df['Survived'] == 1))
    a = sum((df['Age'] >= 18) & (df['Survived'] == 1))
    tc = sum(df['Age'] < 18)
    ta = sum(df['Age'] >= 18)
    return round(c/tc*100, 2), round(a/ta*100, 2)