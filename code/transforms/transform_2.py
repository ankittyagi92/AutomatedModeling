import numpy as np
import pandas as pd

def add_random_column(frame):
    sLength = len(frame[1:])
    frame['random_column'] = pd.Series(np.random.randn(sLength))