
# Proiect PCLP3

Pavel Gabriel-Ioan 313CC

## Scurta descriere a programului

Programul incepe prin a prelua datele din setul de antrenare `train.csv` si a le pune
intr-un dataset `pandas`. Urmatorul pas este examinarea datelor. Acest lucru se face
cu ajutorul functiilor din `examine.py` si din `plots.py` (fiecare functie este descrisa mai jos).
Examinarea decurge in felul urmator: se calculeaza informatiile despre dataframe, procentajele
pentru numarul de oameni care au supravietuit/murit, pentru numarul de pasageri
din fiecare clasa si pentru numarul de barbati/femei. Toate datele sunt afisate pe
ecran, alaturi de cate un pie chart pentru fiecare set de procentaje. In urma finalizarii
examinarii dataframe-ului, se construiesc histograme pentru fiecare coloana numerica
din tabel si se afiseaza pe ecran (se foloseste functia `histograms()` din `plots.py`).
In continuare, calculeaza si afiseaza pe ecran coloanele cu valori lipsa, numarul si
proportia valorilor lipsa din acestea si procentul acestora pentru fiecare dintre
cele doua clase, cu ajutorul functiilor `nullCols()` si `prcNullCols()` din `examine.py`.

## Descriere functii

### examine.py

>**`listData(df)`** - Construieste o lista ce contine informatii despre dataframe:
>
>- *Numarul de coloane*
>- *Numarul de linii*
>- *O lista cu tipurile de date*
>- *Numarul de valori lipsa*
>- *Numarul de duplicate*
>
>**`nullColID(df)`** - Identifica coloanele care contin valori lipsa.
>
>**`prcS(df)`** - Calculeaza procentul de oameni care au supravietuit si oameni care nu au supravietuit.
>
>**`prcPclass(df)`** - Calculeaza procentul de pasageri pentru fiecare clasa
>
>**`prcSex(df)`** - Calculeaza procentul de barbati si de femei.
>
>**`prcNullCols(df)`** - Calculeaza procentele valorilor lipsa ale fiecare coloana
care contine astfel de elemente pentru fiecare dintre cele doua clase (coloana Survived).
>
>**`nullCols(df)`** - Calculeaza numarul si proportia valorilor lipsa din coloanele
care contin astfel de elemente.

### plots.py

>**`pies(df)`** - Folosind array-uri `numpy`, plot-uri `matplotlib` construieste si functii din `examine`
construieste pie chart-uri pentru procentajele pentru numarul de oameni care au
supravietuit/murit, pentru numarul de pasageri din fiecare clasa si pentru numarul
de barbati/femei.
>
>**`histograms(df)`** - Parcurge pe rand fiecare coloana din dataframe, verifica daca
este numerica si, daca da, ii construieste o histograma.
