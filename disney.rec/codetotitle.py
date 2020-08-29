import pandas as pd

def CodetoTitle(code):

    data = pd.read_csv('movies_title.csv', encoding='utf-8', names=['title', 'code'])
    data_index = data
    data_index = data_index.set_index('code', drop = True, append=False, inplace=False)
    print(data_index.loc[code, 'title'])
    
code = int(input())
CodetoTitle(code)
