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
            if row["Survived"] == 0:
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