
# Proiect PCLP3

Pavel Gabriel-Ioan 313CC

## Explicatii pe cerinte

### Cerinta 1

Citesc informatiile din `train.csv` si aplic functia `listData(df)` din `examine.py`.
Aceasta construieste o lista cu toate informatiile cerute: numarul de coloane, numarul
de linii, o lista cu tipurile de date, numarul de valori lipsa si daca exista duplicate.

### Cerinta 2

Se folosesc functiile `prcS(df)`, `prcPclass(df)` si `prcSex(df)` pentru a determina
procentul peroanelor care au supravietuit si care nu au supravietuit, procentul
pasagerilor pentru fiecare tip de clasa, respectiv procentul barbatilor si al
femeilor. Aceste functii se afla in `examine.py`. Functia `pies(df)` din `plots.py`
realizeaza graficele pentru a reprezenta datele calculate mai devreme.

### Cerinta 3

Functia `histograms(df)` parcurge toate coloanele numerice din dataframe si construieste
o histograma pentru fiecare in parte.

### Cerinta 4

Functia `nullColID(df)` identifica coloanele ce contin valori lipsa. Pentru numarul
si proportia valorilor lipsa din coloane se foloseste functia `nullCols(df)`. Procentul
acestora pentru fiecare dintre cele doua clase se determina cu ajutorul functiei
`prcNullCols(df)`.

### Cerinta 5

Numarul de pasageri din fiecare categorie de varsta este determinat cu ajutorul functiei
`detAges(df)`. Coloana suplimentara se introduce in urma executarii functiei anterior
mentionate. Graficul pentru aceste date se realizeaza cu ajutorul functiei `agesPlot(df)`.

### Cerinta 6

Numarul de barbati care au supravietuit pentru fiecare dintre cele 4 categorii este
calculat cu ajutorul functiei `detMaleSurv(df)`. Graficul ce evidentiaza modul in care
varsta influenteaza rata de supravietuire a barbatilor este construit de functia
`maleSurvivalRate(df)`.

### Cerinta 7

Procentul copiilor aflati la bord este calculat de functia `prcChildren(df)`. Graficul
care evidentiata rata de supravietuire pentru copii si pentru adulti este realizat de
functia `caSurvivalRate(df)`.

### Cerinta 8

Valorile lipsa din dataframe sunt completate cu ajutorul functiei `fillEmpty(df)` din
`main.py`.

### Cerinta 9

Am folosit urmatorul cod pentru a gasi toate titlurile prezente in coloana 'Names':

```python
t = []
    for index, row in df.iterrows():
        p = row['Name'].split(',')
        p = p[1].strip().split(' ')
        for i in p:
            if i.endswith('.'):
                tit = i
                break
        try:
            i = t.index(tit)
        except ValueError:
            i = -1
        if i == -1:
            t.append(tit)
```

Am construit manual un dictionar cu toate titlurile si am verificat pentru fiecare
persoana daca sexul atribuit corespunde cu titlul. Afisez daca tuturor le corespunde
tilul cu sexul si graficul asociat. Am folosit functiile `titles(df)` si `titleGenderPlot(df)`.

## Descriere functii

### main.py

>**`fillEmpty(df)`** - Completeaza valorile lipsa din dataframe cu cele obtinute pentru
media pasagerilor care fac parte din aceeasi clasa.

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
>**`prcChildren(df)`** - Calculeaza procentul de copii aflati la bord
>
>**`nullCols(df)`** - Calculeaza numarul si proportia valorilor lipsa din coloanele
care contin astfel de elemente.
>
>**`detAges(df)`** - Determina numarul de oameni incadrati in fiecare categorie
de varsa si construieste o lista pentru a fi folosita in adaugarea noii coloane
in dataframe.
>
>**`detMaleSurv(df)`** - Determina numarul de barbati supravietuitori pentru fiecare
categorie de varsta.
>
>**`detChildAdultSurvivalRate(df)`** - Determina rata de supraviatuire a copiilor si a barbatilor
>
>**`titles(df)`** - Numara cati oameni au titlul corespunzator cu sexul si cati nu.

### plots.py

>**`pies(df)`** - Folosind array-uri `numpy`, plot-uri `matplotlib` construieste si functii din `examine`
construieste pie chart-uri pentru procentajele pentru numarul de oameni care au
supravietuit/murit, pentru numarul de pasageri din fiecare clasa si pentru numarul
de barbati/femei.
>
>**`histograms(df)`** - Parcurge pe rand fiecare coloana din dataframe, verifica daca
este numerica si, daca da, ii construieste o histograma.
>
>**`agesPlot(df, ageList)`** - Construieste graficul ce reprezinta repartitia pe categorii de varsta
a pasagerilor.
>
>**`maleSurvivalRate(df)`** - Construieste un grafic ce reprezinta cum influenteaza varsta procentul
de supravietuire al barbatilor.
>
>**`caSurvivalRate(df)`** - Construieste un grafic ce reprezinta ratele de supravietuire pentru
copii si adulti
>**`titleGenderPlot(df)`** - Construieste un garfic asociat numarului de oameni carora le corespunde
titlul cu sexul si carora nu.
>
