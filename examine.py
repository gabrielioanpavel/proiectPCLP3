import pandas as pd

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
    dataList.append(dup)                            # Numar de duplicate
    return dataList