import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join


DATA_DIR = './data'
files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]

df = pd.DataFrame()
for f in files:
    file = pd.read_csv(join(DATA_DIR, f),  skip_blank_lines=True)
    file['University'] = f.split('.csv')[0]
    try:
        df = df.append(file, ignore_index=True)
    except IndexError:
        df = file

df = df.dropna()

# у ячеек с неизвестным значением стоит -. Заменяем все прочерки на -1
#df = df.replace(to_replace=r'^-$', value=-1, regex=True)
#df = df.apply(pd.to_numeric, errors='ignore')

#tags = set()
#a = df['Topic Cluster name'].str.split(',', expand=True).values.astype(str).ravel('K')
# делаем for иначе не умещаемся по памяти
#for tag in a:
#    tags.add(tag)

#print('Всего уникальных тегов:', len(tags))

# тут где-то будет краш по памяти
#for tag in np.array(list(tags)):
#    print(tag)
#    df[tag] = 0

#df = pd.concat([df, sorted(df['Topic Cluster name'].str.split(',', expand=True))], axis=1)
#print(df.columns.values)

a = input('Введите значение All Science Journal Classification (ASJC) field name: \n')
part1 = df[df['All Science Journal Classification (ASJC) field name'].str.contains(a)]
#Ввод чувствителен к регистру! Можно вбивать любое количество совпадающих символов
print((part1))

b = input('Введите значение Topic Cluster name: \n')
part2 = part1[part1['Topic Cluster name'].str.contains(b)]
print((part2))

c = input('Введите значение Topic name: \n')
part3 = part2[part2['Topic name'].str.contains(c)]
print((part3))

# у ячеек с неизвестным значением стоит -. Заменяем все прочерки на -1
part3 = part3.replace(to_replace=r'^-$', value=-1, regex=True)
part3 = part3.apply(pd.to_numeric, errors='ignore')

part3s=part3.sort_values('Citations', ascending=False) #сортировка по убыванию по столбцу "Citations"
# (можно заменить на др. столбец)
print(part3s)
