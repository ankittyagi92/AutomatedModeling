import random
import pyspark

def add_random_column(row):

    row_dict = row.asDict()

    row_dict['random_column'] = random.randint(1,100)

    row = pyspark.sql.Row(**row_dict)

    return row