import pandas as pd
import random

def printed(list):
    print(f'Index  | Robot | Human')
    for idx, value in enumerate(list):
        if idx < 10:
            if value == 'robot':
                print(f'0{idx}     |   1   |   0   ')
            else:
                print(f'0{idx}     |   0   |   1   ')
        else:
            if value == 'robot':
                print(f'{idx}     |   1   |   0   ')
            else:
                print(f'{idx}     |   0   |   1   ')

def createList():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})
    return lst

printed(createList())