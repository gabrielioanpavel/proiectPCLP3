import pandas as pd
import matplotlib.pyplot as plt
from examine import *

df = pd.read_csv('Titanic Dataset/train.csv')
print(listData(df))
print(prcS(df))
print(prcPclass(df))
print(prcSex(df))
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