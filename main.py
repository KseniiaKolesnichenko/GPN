import pandas as pd
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

print(df.head())
print(df.tail())
