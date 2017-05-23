import random

def add_random_column(row_dict):
    row_dict['random_column'] = random.randint(1,100)
    return row_dict