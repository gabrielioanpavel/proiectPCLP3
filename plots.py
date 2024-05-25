import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from examine import *

def pies(df: pd.DataFrame):
    survivors = np.array(prcS(df))
    classes = np.array(prcPclass(df))
    sex = np.array(prcSex(df))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.pie(survivors, labels=['Da', 'Nu'])
    ax1.set_title('Rata de supravietuire')
    ax2.pie(classes, labels=['Clasa 1', 'Clasa 2', 'Clasa 3'])
    ax2.set_title('Clase Pasageri')
    ax3.pie(sex, labels=['Barbat', 'Femeie'])
    ax3.set_title('Repartitie pe sex')
    plt.show()

def histograms(df: pd.DataFrame):
    for col in df:
        if df[col].dtype == object:
            continue
        x = np.array(df[col])
        plt.hist(x)
        plt.title(col)
        plt.xlabel('Valori')
        plt.ylabel('Numar de oameni')
        plt.show()

def agesPlot(df: pd.DataFrame, ageList):
    fig, ax = plt.subplots()
    ax.set_title('Repartizarea pasagerilor pe categorii de varsta')
    ax.set_xlabel('Categorii de varsta')
    ax.set_ylabel('Varsta')
    ax.bar(['0 - 20', '21 - 40', '41 - 60', '60+'], ageList)
    plt.show()